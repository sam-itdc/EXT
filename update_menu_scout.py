#!/usr/bin/env python3
"""
Script to update scout menu links across all pages
Changes all references from # to page-scoutinfo/scout.html
"""

import os
import re
from pathlib import Path

def update_scout_link_in_file(file_path, relative_path_to_scout):
    """Update the scout menu item link in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find and update the scout menu item
        pattern = r'<li><a href="#">童軍</a></li>'
        replacement = f'<li><a href="{relative_path_to_scout}">童軍</a></li>'
        
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
    
    # Define file paths and their corresponding relative paths to page-scoutinfo/scout.html
    files_to_update = [
        # page-about directory files
        ('page-about/introduction.html', '../page-scoutinfo/scout.html'),
        ('page-about/patrons.html', '../page-scoutinfo/scout.html'),
        ('page-about/structure.html', '../page-scoutinfo/scout.html'),
        ('page-about/departments.html', '../page-scoutinfo/scout.html'),
        ('page-about/groups.html', '../page-scoutinfo/scout.html'),
        ('page-about/history.html', '../page-scoutinfo/scout.html'),
        ('page-about/forms.html', '../page-scoutinfo/scout.html'),
        ('page-about/emblem.html', '../page-scoutinfo/scout.html'),
        
        # page-scoutinfo directory files (excluding scout.html itself)
        ('page-scoutinfo/apply.html', 'scout.html'),
        ('page-scoutinfo/award.html', 'scout.html'),
        ('page-scoutinfo/mop.html', 'scout.html'),
        ('page-scoutinfo/wood-badge.html', 'scout.html'),
        ('page-scoutinfo/ranking.html', 'scout.html'),
        ('page-scoutinfo/uniform.html', 'scout.html'),
        ('page-scoutinfo/badge.html', 'scout.html'),
        ('page-scoutinfo/cub.html', 'scout.html'),
        
        # Root directory template files
        ('left-sidebar.html', 'page-scoutinfo/scout.html'),
        ('right-sidebar.html', 'page-scoutinfo/scout.html'),
        ('no-sidebar.html', 'page-scoutinfo/scout.html'),
        ('promise.html', 'page-scoutinfo/scout.html'),
        ('menu-template.html', 'page-scoutinfo/scout.html'),
    ]
    
    print("🏕️ Updating scout menu links...")
    print("=" * 50)
    
    for file_path, scout_path in files_to_update:
        full_path = base_dir / file_path
        
        if full_path.exists():
            if update_scout_link_in_file(full_path, scout_path):
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
    
    print(f"\n🎯 Scout menu links updated successfully!")
    print(f"   '童軍' now links to page-scoutinfo/scout.html")

if __name__ == "__main__":
    main()

