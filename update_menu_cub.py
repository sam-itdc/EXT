#!/usr/bin/env python3
"""
Script to update cub scout menu links across all pages
Changes "幼童軍" link from "#" to "cub.html"
"""

import os
import re
from pathlib import Path

def update_cub_menu_in_file(file_path, relative_path_to_cub):
    """Update the cub scout menu item in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find and update the cub scout menu item
        pattern = r'<li><a href="#">幼童軍</a></li>'
        replacement = f'<li><a href="{relative_path_to_cub}">幼童軍</a></li>'
        
        # Update the content
        updated_content = re.sub(pattern, replacement, content)
        
        # Only write if content changed
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            return True
        return False
        
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    base_dir = Path('/home/ubuntu/EXT')
    updated_files = []
    
    # Define file paths and their corresponding relative paths to cub.html
    files_to_update = [
        # page-about directory files
        ('page-about/introduction.html', '../cub.html'),
        ('page-about/patrons.html', '../cub.html'),
        ('page-about/structure.html', '../cub.html'),
        ('page-about/departments.html', '../cub.html'),
        ('page-about/groups.html', '../cub.html'),
        ('page-about/history.html', '../cub.html'),
        ('page-about/forms.html', '../cub.html'),
        ('page-about/emblem.html', '../cub.html'),
        
        # page-scoutinfo directory files
        ('page-scoutinfo/apply.html', '../cub.html'),
        ('page-scoutinfo/award.html', '../cub.html'),
        ('page-scoutinfo/mop.html', '../cub.html'),
        ('page-scoutinfo/wood-badge.html', '../cub.html'),
        ('page-scoutinfo/ranking.html', '../cub.html'),
        ('page-scoutinfo/uniform.html', '../cub.html'),
        ('page-scoutinfo/badge.html', '../cub.html'),
        
        # Root directory template files
        ('left-sidebar.html', 'cub.html'),
        ('right-sidebar.html', 'cub.html'),
        ('no-sidebar.html', 'cub.html'),
        ('promise.html', 'cub.html'),
        ('menu-template.html', 'cub.html'),
    ]
    
    print("🐻 Updating cub scout menu items...")
    print("=" * 50)
    
    for file_path, cub_path in files_to_update:
        full_path = base_dir / file_path
        
        if full_path.exists():
            if update_cub_menu_in_file(full_path, cub_path):
                updated_files.append(file_path)
                print(f"✅ Updated: {file_path}")
            else:
                print(f"⚪ No change: {file_path}")
        else:
            print(f"❌ Not found: {file_path}")
    
    print("=" * 50)
    print(f"📊 Summary:")
    print(f"   Total files updated: {len(updated_files)}")
    print(f"   Files processed: {len(files_to_update)}")
    
    if updated_files:
        print(f"\n📁 Updated files:")
        for file_path in updated_files:
            print(f"   - {file_path}")
    
    print(f"\n🎯 Cub scout menu items updated successfully!")
    print(f"   '幼童軍' now links to cub.html")

if __name__ == "__main__":
    main()

