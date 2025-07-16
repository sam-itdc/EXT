#!/usr/bin/env python3
"""
Script to update all pages with the new announcements menu structure
Changes "活動" to "通告" and updates all menu links
"""

import os
import re
from pathlib import Path

def update_menu_in_file(file_path, base_path=""):
    """Update the menu in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Determine the correct relative path for announcements.html
        if base_path == "page-about":
            announcements_path = "../announcements.html"
            mop_path = "../page-scoutinfo/mop.html"
        elif base_path == "page-scoutinfo":
            announcements_path = "../announcements.html"
            mop_path = "mop.html"
        else:  # root directory
            announcements_path = "announcements.html"
            mop_path = "page-scoutinfo/mop.html"
        
        # Pattern to match the activities menu section
        activities_pattern = r'(<li><!--活動-->.*?<a href="#">活動</a>.*?<ul>)(.*?)(</ul>.*?</li>)'
        
        # New announcements menu structure
        new_menu_items = f'''
										<li><a href="{announcements_path}?category=training">訓練班消息</a></li>
										<li><a href="{announcements_path}?category=activity">活動消息</a></li>
										<li><a href="{announcements_path}?category=international">國際活動</a></li>
										<li><a href="{mop_path}">MOP 和平使者計劃</a></li>
										<li><a href="{announcements_path}?category=general">總會通告</a></li>
										<li><a href="{announcements_path}?category=service">服務通告</a></li>
									'''
        
        # Replace the activities menu with announcements menu
        def replace_menu(match):
            return f'<li><!--通告-->\n\t\t\t\t\t\t\t\t\t<a href="#">通告</a>\n\t\t\t\t\t\t\t\t\t<ul>{new_menu_items}</ul>\n\t\t\t\t\t\t\t\t</li>'
        
        content = re.sub(activities_pattern, replace_menu, content, flags=re.DOTALL)
        
        # Check if any changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    base_dir = Path('/home/ubuntu/EXT')
    
    print("🔄 Updating announcements menu across all pages...")
    print("=" * 60)
    
    # Define directories and their files
    directories = {
        "page-about": [
            "introduction.html", "patrons.html", "structure.html", 
            "departments.html", "groups.html", "history.html", 
            "forms.html", "emblem.html"
        ],
        "page-scoutinfo": [
            "award.html", "badge.html", "ranking.html", "uniform.html",
            "cub.html", "scout.html", "venture.html", "wood-badge.html",
            "apply.html", "mop.html"
        ],
        "": [  # root directory
            "patrons.html", "structure.html", "introduction.html",
            "departments.html", "groups.html"
        ]
    }
    
    updated_files = []
    skipped_files = []
    
    for dir_name, files in directories.items():
        dir_path = base_dir / dir_name if dir_name else base_dir
        
        print(f"\\n📁 Processing {dir_name if dir_name else 'root'} directory:")
        
        for file_name in files:
            file_path = dir_path / file_name
            
            if file_path.exists():
                if update_menu_in_file(file_path, dir_name):
                    print(f"   ✅ Updated: {file_name}")
                    updated_files.append(str(file_path.relative_to(base_dir)))
                else:
                    print(f"   ⚠️  No changes: {file_name}")
                    skipped_files.append(str(file_path.relative_to(base_dir)))
            else:
                print(f"   ❌ Not found: {file_name}")
                skipped_files.append(str(file_path.relative_to(base_dir)))
    
    print("\\n" + "=" * 60)
    print("📊 Update Summary:")
    print(f"   ✅ Successfully updated: {len(updated_files)} files")
    print(f"   ⚠️  Skipped/Not found: {len(skipped_files)} files")
    
    if updated_files:
        print("\\n📝 Updated files:")
        for file_path in updated_files:
            print(f"   - {file_path}")
    
    if skipped_files:
        print("\\n⚠️  Skipped files:")
        for file_path in skipped_files:
            print(f"   - {file_path}")
    
    print("\\n🎉 Menu update completed!")
    print("\\n💡 Changes made:")
    print("   - Changed '活動' to '通告' in all menus")
    print("   - Updated menu links to point to announcements.html with category filters")
    print("   - Preserved 'MOP 和平使者計劃' link")
    print("   - Applied intelligent relative path handling")

if __name__ == "__main__":
    main()

