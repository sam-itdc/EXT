#!/usr/bin/env python3
"""
Script to update military rank badges menu links across all pages
Updates the "軍職徽章" link to point to ranking.html
"""

import os
import re
from pathlib import Path

def update_ranking_link_in_file(file_path, relative_path_to_ranking):
    """Update the military rank badges link in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find the military rank badges menu item
        pattern = r'<li><a href="[^"]*">軍職徽章</a></li>'
        replacement = f'<li><a href="{relative_path_to_ranking}">軍職徽章</a></li>'
        
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
    
    # Define file paths and their corresponding relative paths to ranking.html
    files_to_update = [
        # page-about directory files
        ('page-about/introduction.html', '../page-scoutinfo/ranking.html'),
        ('page-about/patrons.html', '../page-scoutinfo/ranking.html'),
        ('page-about/structure.html', '../page-scoutinfo/ranking.html'),
        ('page-about/departments.html', '../page-scoutinfo/ranking.html'),
        ('page-about/groups.html', '../page-scoutinfo/ranking.html'),
        ('page-about/history.html', '../page-scoutinfo/ranking.html'),
        
        # page-scoutinfo directory files
        ('page-scoutinfo/apply.html', 'ranking.html'),
        ('page-scoutinfo/award.html', 'ranking.html'),
        ('page-scoutinfo/mop.html', 'ranking.html'),
        ('page-scoutinfo/wood-badge.html', 'ranking.html'),
        
        # Root directory template files
        ('left-sidebar.html', 'page-scoutinfo/ranking.html'),
        ('right-sidebar.html', 'page-scoutinfo/ranking.html'),
        ('no-sidebar.html', 'page-scoutinfo/ranking.html'),
        ('promise.html', 'page-scoutinfo/ranking.html'),
        ('menu-template.html', 'page-scoutinfo/ranking.html'),
    ]
    
    print("🎖️ Updating military rank badges menu links...")
    print("=" * 50)
    
    for file_path, ranking_path in files_to_update:
        full_path = base_dir / file_path
        
        if full_path.exists():
            if update_ranking_link_in_file(full_path, ranking_path):
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
    
    print(f"\n🎯 Military rank badges menu links updated successfully!")
    print(f"   All pages now link to ranking.html")

if __name__ == "__main__":
    main()

