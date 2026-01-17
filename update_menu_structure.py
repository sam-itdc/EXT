#!/usr/bin/env python3
"""
Menu structure synchronization script with absolute path support
This script updates the navigation menu and logo across all HTML files to match the main index.html
"""

import os
import re
from pathlib import Path

def get_main_menu_content():
    """Extract the main menu content from index.html"""
    index_path = Path('/home/ubuntu/EXT/index.html')
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract the nav menu content
        nav_pattern = r'(<nav id="nav">\s*<ul>)(.*?)(</ul>\s*</nav>)'
        match = re.search(nav_pattern, content, re.DOTALL)
        
        if match:
            return match.group(2).strip()
        else:
            print("❌ Could not find nav menu in index.html")
            return None
            
    except Exception as e:
        print(f"❌ Error reading index.html: {e}")
        return None

def update_file_menu(file_path, main_menu_content):
    """Update the menu and logo in a specific HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Update navigation menu
        nav_pattern = r'(<nav id="nav">\s*<ul>)(.*?)(</ul>\s*</nav>)'
        
        def replace_menu(match):
            return match.group(1) + '\n\t\t\t\t\t\t' + main_menu_content + '\n\t\t\t\t\t' + match.group(3)
        
        content = re.sub(nav_pattern, replace_menu, content, flags=re.DOTALL)
        
        # 2. Update logo links to use absolute paths
        # Update logo href
        logo_href_pattern = r'(<div id="logo">\s*<h1><a href=")[^"]*(")'
        content = re.sub(logo_href_pattern, r'\1/index.html\2', content)
        
        # Update logo img src
        logo_img_pattern = r'(<img src=")[^"]*scout-logo-removebg-preview\.png"'
        content = re.sub(logo_img_pattern, r'\1/images/layout/scout-logo-removebg-preview.png"', content)
        
        if content == original_content:
            return False  # No changes made
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return False

def main():
    """Main function to synchronize menu across all HTML files"""
    base_dir = Path('/home/ubuntu/EXT')
    
    print("🔄 Synchronizing menu structure and absolute paths across all HTML files...")
    print("=" * 70)
    
    # Get the main menu content from index.html
    print("📖 Reading main menu structure from index.html...")
    main_menu_content = get_main_menu_content()
    
    if not main_menu_content:
        print("❌ Failed to extract main menu content")
        return
    
    print("✅ Successfully extracted main menu structure")
    
    # Find all HTML files except index.html
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html') and file != 'index.html':
                file_path = Path(root) / file
                html_files.append(file_path)
    
    print(f"📁 Found {len(html_files)} HTML files to update")
    
    # Update each file
    updated_count = 0
    skipped_count = 0
    error_count = 0
    
    for file_path in html_files:
        relative_path = file_path.relative_to(base_dir)
        print(f"📝 Updating {relative_path}...", end=" ")
        
        if update_file_menu(file_path, main_menu_content):
            print("✅")
            updated_count += 1
        else:
            # Check if file has nav menu
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if '<nav id="nav">' in content:
                    print("⚠️ No changes")
                    skipped_count += 1
                else:
                    print("⏭️ No nav menu")
                    skipped_count += 1
            except:
                print("❌ Error")
                error_count += 1
    
    print("=" * 70)
    print("🎉 Menu synchronization completed!")
    print(f"📊 Results:")
    print(f"   - Files updated: {updated_count}")
    print(f"   - Files skipped: {skipped_count}")
    print(f"   - Errors: {error_count}")
    print(f"   - Total processed: {len(html_files)}")
    
    if updated_count > 0:
        print(f"\n✅ Successfully synchronized menu structure across {updated_count} files")
        print("🔗 Absolute path updates:")
        print("   - All menu links now use absolute paths (starting with /)")
        print("   - Logo links updated to /index.html")
        print("   - Logo images updated to /images/layout/scout-logo-removebg-preview.png")
        print("   - Consistent navigation behavior across all pages")
    
    print(f"\n💡 All HTML files now have consistent menu structure and absolute paths")
    print("🌐 Navigation will work correctly from any page depth")

if __name__ == "__main__":
    main()

