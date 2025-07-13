#!/usr/bin/env python3
"""
Script to update badge introduction menu links across all pages
Updates the "徽章介紹" link to point to badge.html
"""

import os
import re
from pathlib import Path

def update_badge_link_in_file(file_path, relative_path_to_badge):
    """Update the badge introduction link in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find the badge introduction menu item
        pattern = r'<li><a href="[^"]*">徽章介紹</a></li>'
        replacement = f'<li><a href="{relative_path_to_badge}">徽章介紹</a></li>'
        
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
    
    # Define file paths and their corresponding relative paths to badge.html
    files_to_update = [
        # page-about directory files
        ('page-about/introduction.html', '../page-scoutinfo/badge.html'),
        ('page-about/patrons.html', '../page-scoutinfo/badge.html'),
        ('page-about/structure.html', '../page-scoutinfo/badge.html'),
        ('page-about/departments.html', '../page-scoutinfo/badge.html'),
        ('page-about/groups.html', '../page-scoutinfo/badge.html'),
        ('page-about/history.html', '../page-scoutinfo/badge.html'),
        
        # page-scoutinfo directory files
        ('page-scoutinfo/apply.html', 'badge.html'),
        ('page-scoutinfo/award.html', 'badge.html'),
        ('page-scoutinfo/mop.html', 'badge.html'),
        ('page-scoutinfo/wood-badge.html', 'badge.html'),
        ('page-scoutinfo/ranking.html', 'badge.html'),
        ('page-scoutinfo/uniform.html', 'badge.html'),
        
        # Root directory template files
        ('left-sidebar.html', 'page-scoutinfo/badge.html'),
        ('right-sidebar.html', 'page-scoutinfo/badge.html'),
        ('no-sidebar.html', 'page-scoutinfo/badge.html'),
        ('promise.html', 'page-scoutinfo/badge.html'),
        ('menu-template.html', 'page-scoutinfo/badge.html'),
    ]
    
    print("🏅 Updating badge introduction menu links...")
    print("=" * 50)
    
    for file_path, badge_path in files_to_update:
        full_path = base_dir / file_path
        
        if full_path.exists():
            if update_badge_link_in_file(full_path, badge_path):
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
    
    print(f"\n🎯 Badge introduction menu links updated successfully!")
    print(f"   All pages now link to badge.html")

if __name__ == "__main__":
    main()

