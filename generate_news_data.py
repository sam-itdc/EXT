#!/usr/bin/env python3
"""
Automation script to generate news and newsletter data from markdown files
This script parses news.md and newsletters.md and updates relevant HTML files
"""

import re
import json
from datetime import datetime
from pathlib import Path

def parse_newsletters_md(file_path):
    """Parse newsletters.md file and extract newsletter items"""
    newsletter_items = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split content by newsletter items (each starts with "- ")
        items = re.split(r'\n(?=- )', content.strip())
        
        for item in items:
            if not item.strip():
                continue
                
            lines = item.strip().split('\n')
            if len(lines) < 2:
                continue
                
            # Parse each line
            title = lines[0].replace('- ', '').strip()
            link = lines[1].replace('  - ', '').strip()
            
            # Keywords are optional (3rd line)
            keywords = ""
            if len(lines) >= 3:
                keywords = lines[2].replace('  - ', '').strip()
            
            newsletter_item = {
                'title': title,
                'link': link,
                'keywords': keywords
            }
            
            newsletter_items.append(newsletter_item)
    
    except Exception as e:
        print(f"Error parsing newsletters.md: {e}")
        return []
    
    return newsletter_items

def generate_newsletter_javascript_data(newsletter_items):
    """Generate JavaScript data array from newsletter items"""
    js_items = []
    
    for item in newsletter_items:
        js_item = f"""				{{
					title: "{item['title']}",
					link: "{item['link']}",
					keywords: "{item['keywords']}"
				}}"""
        js_items.append(js_item)
    
    newline = '\n'
    js_data = f"""			// Newsletter data - This will be automatically generated from newsletters.md
			const newsletterData = [
{(','+newline).join(js_items)}
			];"""
    
    return js_data

def update_newsletters_html(html_file_path, newsletter_data_js):
    """Update newsletters.html with new newsletter data"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the newsletterData section
        pattern = r'(// Newsletter data - This will be automatically generated from newsletters\.md\s*const newsletterData = \[)[^;]+(;)'
        replacement = newsletter_data_js + '\n\t\t\t'
        
        updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        if updated_content == content:
            print("Warning: Could not find newsletterData section to update in newsletters.html")
            return False
        
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
        
    except Exception as e:
        print(f"Error updating newsletters.html: {e}")
        return False

def update_index_html_newsletters(html_file_path, newsletter_data_js):
    """Update index.html with new newsletter data"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the newsletterData section in index.html
        pattern = r'(// Newsletter data - This will be automatically generated from newsletters\.md\s*const newsletterData = \[)[^;]+(;)'
        
        # Adjust the JavaScript data for index.html (different indentation)
        index_js_data = newsletter_data_js.replace('\t\t\t', '\t\t\t\t')
        
        replacement = index_js_data + '\n\t\t\t\t'
        
        updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        if updated_content == content:
            print("Warning: Could not find newsletterData section to update in index.html")
            return False
        
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
        
    except Exception as e:
        print(f"Error updating index.html newsletters: {e}")
        return False

def parse_news_md(file_path):
    """Parse news.md file and extract news items"""
    news_items = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split content by news items (each starts with "- ")
        items = re.split(r'\n(?=- )', content.strip())
        
        for item in items:
            if not item.strip():
                continue
                
            lines = item.strip().split('\n')
            if len(lines) < 4:
                continue
                
            # Parse each line
            title = lines[0].replace('- ', '').strip()
            category = lines[1].replace('  - ', '').strip()
            link = lines[2].replace('  - ', '').strip()
            date_time = lines[3].replace('  - ', '').strip()
            
            # Keywords are optional (5th line)
            keywords = ""
            if len(lines) >= 5:
                keywords = lines[4].replace('  - ', '').strip()
            
            # Map category to category key
            category_key_map = {
                '訓練班消息': 'training',
                '活動消息': 'activity',
                '國際活動': 'international',
                '總會通告': 'general',
                '服務通告': 'service'
            }
            
            category_key = category_key_map.get(category, 'general')
            
            news_item = {
                'title': title,
                'category': category,
                'categoryKey': category_key,
                'link': link,
                'date': date_time,
                'keywords': keywords
            }
            
            news_items.append(news_item)
    
    except Exception as e:
        print(f"Error parsing news.md: {e}")
        return []
    
    return news_items

def generate_javascript_data(news_items):
    """Generate JavaScript data array from news items"""
    js_items = []
    
    for item in news_items:
        js_item = f"""				{{
					title: "{item['title']}",
					category: "{item['category']}",
					categoryKey: "{item['categoryKey']}",
					link: "{item['link']}",
					date: "{item['date']}",
					keywords: "{item['keywords']}"
				}}"""
        js_items.append(js_item)
    
    newline = '\n'
    js_data = f"""			// News data - This will be automatically generated from news.md
			const newsData = [
{(','+newline).join(js_items)}
			];"""
    
    return js_data

def update_announcements_html(html_file_path, news_data_js):
    """Update news.html with new news data"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the newsData section
        pattern = r'(// News data - This will be automatically generated from news\.md\s*const newsData = \[)[^;]+(;)'
        replacement = news_data_js + '\n\t\t\t'
        
        updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        if updated_content == content:
            print("Warning: Could not find newsData section to update in news.html")
            return False
        
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
        
    except Exception as e:
        print(f"Error updating news.html: {e}")
        return False

def update_index_html(html_file_path, news_data_js):
    """Update index.html with new news data"""
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the newsData section in index.html
        pattern = r'(// 通告數據 - 從 news\.md 同步\s*const newsData = \[)[^;]+(;)'
        
        # Adjust the JavaScript data for index.html (different indentation)
        index_js_data = news_data_js.replace('			// News data - This will be automatically generated from news.md', '				// 通告數據 - 從 news.md 同步')
        index_js_data = index_js_data.replace('\t\t\t', '\t\t\t\t')
        
        replacement = index_js_data + '\n\t\t\t\t'
        
        updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        if updated_content == content:
            print("Warning: Could not find newsData section to update in index.html")
            return False
        
        with open(html_file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        return True
        
    except Exception as e:
        print(f"Error updating index.html: {e}")
        return False

def main():
    """Main function to process news.md and newsletters.md and update HTML files"""
    base_dir = Path('/home/ubuntu/EXT')
    news_md_path = base_dir / 'news.md'
    newsletters_md_path = base_dir / 'newsletters.md'
    announcements_html_path = base_dir / 'news.html'
    newsletters_html_path = base_dir / 'newsletters.html'
    index_html_path = base_dir / 'index.html'
    
    print("📰 Generating data from news.md and newsletters.md...")
    print("=" * 60)
    
    # Process news data
    print("📢 Processing news data...")
    if news_md_path.exists():
        print(f"📖 Reading news data from: {news_md_path}")
        news_items = parse_news_md(news_md_path)
        
        if news_items:
            print(f"✅ Found {len(news_items)} news items:")
            for i, item in enumerate(news_items, 1):
                print(f"   {i}. {item['title']} ({item['category']})")
            
            # Generate JavaScript data
            print(f"🔧 Generating news JavaScript data...")
            news_js_data = generate_javascript_data(news_items)
            
            # Update news.html
            if announcements_html_path.exists():
                print(f"📝 Updating {announcements_html_path}...")
                if update_announcements_html(announcements_html_path, news_js_data):
                    print("✅ Successfully updated news.html")
                else:
                    print("❌ Failed to update news.html")
            else:
                print(f"❌ Error: {announcements_html_path} not found")
            
            # Update index.html with news data
            if index_html_path.exists():
                print(f"📝 Updating {index_html_path} with news data...")
                if update_index_html(index_html_path, news_js_data):
                    print("✅ Successfully updated index.html with news data")
                else:
                    print("❌ Failed to update index.html with news data")
            else:
                print(f"❌ Error: {index_html_path} not found")
        else:
            print("❌ No news items found or error parsing news.md")
    else:
        print(f"❌ Error: {news_md_path} not found")
    
    print("\n" + "=" * 60)
    
    # Process newsletter data
    print("📖 Processing newsletter data...")
    if newsletters_md_path.exists():
        print(f"📖 Reading newsletter data from: {newsletters_md_path}")
        newsletter_items = parse_newsletters_md(newsletters_md_path)
        
        if newsletter_items:
            print(f"✅ Found {len(newsletter_items)} newsletter items:")
            for i, item in enumerate(newsletter_items, 1):
                print(f"   {i}. {item['title']}")
            
            # Generate JavaScript data
            print(f"🔧 Generating newsletter JavaScript data...")
            newsletter_js_data = generate_newsletter_javascript_data(newsletter_items)
            
            # Update newsletters.html
            if newsletters_html_path.exists():
                print(f"📝 Updating {newsletters_html_path}...")
                if update_newsletters_html(newsletters_html_path, newsletter_js_data):
                    print("✅ Successfully updated newsletters.html")
                else:
                    print("❌ Failed to update newsletters.html")
            else:
                print(f"❌ Error: {newsletters_html_path} not found")
            
            # Update index.html with newsletter data
            if index_html_path.exists():
                print(f"📝 Updating {index_html_path} with newsletter data...")
                if update_index_html_newsletters(index_html_path, newsletter_js_data):
                    print("✅ Successfully updated index.html with newsletter data")
                else:
                    print("❌ Failed to update index.html with newsletter data")
            else:
                print(f"❌ Error: {index_html_path} not found")
        else:
            print("❌ No newsletter items found or error parsing newsletters.md")
    else:
        print(f"❌ Error: {newsletters_md_path} not found")
    
    print("=" * 60)
    print("🎉 Data generation completed!")
    
    # Final statistics
    if 'news_items' in locals() and news_items:
        print(f"📊 News Statistics:")
        print(f"   - Total news items: {len(news_items)}")
        
        # Count by category
        category_counts = {}
        for item in news_items:
            category = item['category']
            category_counts[category] = category_counts.get(category, 0) + 1
        
        for category, count in category_counts.items():
            print(f"   - {category}: {count} items")
        
        # Count general announcements specifically
        general_count = category_counts.get('總會通告', 0)
        print(f"\n📢 Latest News Display:")
        print(f"   - 總會通告項目: {general_count} 個")
        if general_count > 0:
            print(f"   - 主頁將顯示最新 {min(general_count, 10)} 個總會通告")
        else:
            print(f"   - 主頁將顯示 '沒有通告'")
    
    if 'newsletter_items' in locals() and newsletter_items:
        print(f"\n📖 Newsletter Statistics:")
        print(f"   - Total newsletter items: {len(newsletter_items)}")
        print(f"   - 主頁將顯示最新 {min(len(newsletter_items), 6)} 個月刊")
    
    print(f"\n💡 To update content:")
    print(f"   1. Edit {news_md_path} or {newsletters_md_path}")
    print(f"   2. Run this script: python3 generate_news_data.py")
    print(f"   3. All relevant HTML files will be automatically updated")

if __name__ == "__main__":
    main()

