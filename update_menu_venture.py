#!/usr/bin/env python3
"""
Script to update venture scout menu links across all pages
Changes all references from # to page-scoutinfo/venture.html
"""

import os
import re
from pathlib import Path

def update_venture_link_in_file(file_path, relative_path_to_venture):
    """Update the venture scout menu item link in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find and update the venture scout menu item
        pattern = r'<li><a href="#">深資童軍</a></li>'
        replacement = f'<li><a href="{relative_path_to_venture}">深資童軍</a></li>'
        
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
    
    # Define file paths and their corresponding relative paths to page-scoutinfo/venture.html
    files_to_update = [
        # page-about directory files
        ('page-about/introduction.html', '../page-scoutinfo/venture.html'),
        ('page-about/patrons.html', '../page-scoutinfo/venture.html'),
        ('page-about/structure.html', '../page-scoutinfo/venture.html'),
        ('page-about/departments.html', '../page-scoutinfo/venture.html'),
        ('page-about/groups.html', '../page-scoutinfo/venture.html'),
        ('page-about/history.html', '../page-scoutinfo/venture.html'),
        ('page-about/forms.html', '../page-scoutinfo/venture.html'),
        ('page-about/emblem.html', '../page-scoutinfo/venture.html'),
        
        # page-scoutinfo directory files (excluding venture.html itself)
        ('page-scoutinfo/apply.html', 'venture.html'),
        ('page-scoutinfo/award.html', 'venture.html'),
        ('page-scoutinfo/mop.html', 'venture.html'),
        ('page-scoutinfo/wood-badge.html', 'venture.html'),
        ('page-scoutinfo/ranking.html', 'venture.html'),
        ('page-scoutinfo/uniform.html', 'venture.html'),
        ('page-scoutinfo/badge.html', 'venture.html'),
        ('page-scoutinfo/cub.html', 'venture.html'),
        ('page-scoutinfo/scout.html', 'venture.html'),
        
        # Root directory template files
        ('left-sidebar.html', 'page-scoutinfo/venture.html'),
        ('right-sidebar.html', 'page-scoutinfo/venture.html'),
        ('no-sidebar.html', 'page-scoutinfo/venture.html'),
        ('promise.html', 'page-scoutinfo/venture.html'),
        ('menu-template.html', 'page-scoutinfo/venture.html'),
    ]
    
    print("🎯 Updating venture scout menu links...")
    print("=" * 50)
    
    for file_path, venture_path in files_to_update:
        full_path = base_dir / file_path
        
        if full_path.exists():
            if update_venture_link_in_file(full_path, venture_path):
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
    
    print(f"\n🎯 Venture scout menu links updated successfully!")
    print(f"   '深資童軍' now links to page-scoutinfo/venture.html")

if __name__ == "__main__":
    main()

