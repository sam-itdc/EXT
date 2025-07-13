#!/usr/bin/env python3
"""
Script to update cub scout menu links to new path page-scoutinfo/cub.html
Changes all references from old paths to page-scoutinfo/cub.html
"""

import os
import re
from pathlib import Path

def update_cub_path_in_file(file_path, relative_path_to_cub):
    """Update the cub scout menu item path in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find and update the cub scout menu item
        # Handle both old paths: cub.html and ../cub.html
        patterns_and_replacements = [
            (r'<li><a href="cub\.html">幼童軍</a></li>', f'<li><a href="{relative_path_to_cub}">幼童軍</a></li>'),
            (r'<li><a href="\.\.\/cub\.html">幼童軍</a></li>', f'<li><a href="{relative_path_to_cub}">幼童軍</a></li>')
        ]
        
        updated_content = content
        changed = False
        
        for pattern, replacement in patterns_and_replacements:
            new_content = re.sub(pattern, replacement, updated_content)
            if new_content != updated_content:
                updated_content = new_content
                changed = True
        
        # Only write if content changed
        if changed:
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
    
    # Define file paths and their corresponding relative paths to page-scoutinfo/cub.html
    files_to_update = [
        # page-about directory files
        ('page-about/introduction.html', '../page-scoutinfo/cub.html'),
        ('page-about/patrons.html', '../page-scoutinfo/cub.html'),
        ('page-about/structure.html', '../page-scoutinfo/cub.html'),
        ('page-about/departments.html', '../page-scoutinfo/cub.html'),
        ('page-about/groups.html', '../page-scoutinfo/cub.html'),
        ('page-about/history.html', '../page-scoutinfo/cub.html'),
        ('page-about/forms.html', '../page-scoutinfo/cub.html'),
        ('page-about/emblem.html', '../page-scoutinfo/cub.html'),
        
        # page-scoutinfo directory files (excluding cub.html itself)
        ('page-scoutinfo/apply.html', 'cub.html'),
        ('page-scoutinfo/award.html', 'cub.html'),
        ('page-scoutinfo/mop.html', 'cub.html'),
        ('page-scoutinfo/wood-badge.html', 'cub.html'),
        ('page-scoutinfo/ranking.html', 'cub.html'),
        ('page-scoutinfo/uniform.html', 'cub.html'),
        ('page-scoutinfo/badge.html', 'cub.html'),
        
        # Root directory template files
        ('left-sidebar.html', 'page-scoutinfo/cub.html'),
        ('right-sidebar.html', 'page-scoutinfo/cub.html'),
        ('no-sidebar.html', 'page-scoutinfo/cub.html'),
        ('promise.html', 'page-scoutinfo/cub.html'),
        ('menu-template.html', 'page-scoutinfo/cub.html'),
    ]
    
    print("🐻 Updating cub scout menu paths...")
    print("=" * 50)
    
    for file_path, cub_path in files_to_update:
        full_path = base_dir / file_path
        
        if full_path.exists():
            if update_cub_path_in_file(full_path, cub_path):
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
    
    print(f"\n🎯 Cub scout menu paths updated successfully!")
    print(f"   '幼童軍' now links to page-scoutinfo/cub.html")

if __name__ == "__main__":
    main()

