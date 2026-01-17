#!/usr/bin/env python3
"""
Script to remove activity calendar menu item from all pages
Removes the "活動行事曆" menu item from the activities menu
"""

import os
import re
from pathlib import Path

def remove_activity_calendar_from_file(file_path):
    """Remove the activity calendar menu item from a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find and remove the activity calendar menu item
        # This will match the entire line containing the activity calendar link
        pattern = r'\s*<li><a href="[^"]*">活動行事曆</a></li>\s*\n?'
        
        # Remove the activity calendar menu item
        updated_content = re.sub(pattern, '', content)
        
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
    
    # Define all files that need to be updated
    files_to_update = [
        # page-about directory files
        'page-about/introduction.html',
        'page-about/patrons.html',
        'page-about/structure.html',
        'page-about/departments.html',
        'page-about/groups.html',
        'page-about/history.html',
        
        # page-scoutinfo directory files
        'page-scoutinfo/apply.html',
        'page-scoutinfo/award.html',
        'page-scoutinfo/mop.html',
        'page-scoutinfo/wood-badge.html',
        'page-scoutinfo/ranking.html',
        'page-scoutinfo/uniform.html',
        'page-scoutinfo/badge.html',
        
        # Root directory template files
        'left-sidebar.html',
        'right-sidebar.html',
        'no-sidebar.html',
        'promise.html',
        'menu-template.html',
    ]
    
    print("📅 Removing activity calendar menu item...")
    print("=" * 50)
    
    for file_path in files_to_update:
        full_path = base_dir / file_path
        
        if full_path.exists():
            if remove_activity_calendar_from_file(full_path):
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
    
    print(f"\n🎯 Activity calendar menu item removed successfully!")
    print(f"   The '活動行事曆' menu item has been removed from all pages")

if __name__ == "__main__":
    main()

