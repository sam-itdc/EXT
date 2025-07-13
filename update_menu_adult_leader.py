#!/usr/bin/env python3
"""
Script to update adult leader menu links across all pages
Changes all references from # to page-scoutinfo/wood-badge.html
"""

import os
import re
from pathlib import Path

def update_adult_leader_link_in_file(file_path, relative_path_to_wood_badge):
    """Update the adult leader menu item link in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find and update the adult leader menu item
        pattern = r'<li><a href="#">成年領袖</a></li>'
        replacement = f'<li><a href="{relative_path_to_wood_badge}">成年領袖</a></li>'
        
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
    
    # Define file paths and their corresponding relative paths to page-scoutinfo/wood-badge.html
    files_to_update = [
        # page-about directory files
        ('page-about/introduction.html', '../page-scoutinfo/wood-badge.html'),
        ('page-about/patrons.html', '../page-scoutinfo/wood-badge.html'),
        ('page-about/structure.html', '../page-scoutinfo/wood-badge.html'),
        ('page-about/departments.html', '../page-scoutinfo/wood-badge.html'),
        ('page-about/groups.html', '../page-scoutinfo/wood-badge.html'),
        ('page-about/history.html', '../page-scoutinfo/wood-badge.html'),
        ('page-about/forms.html', '../page-scoutinfo/wood-badge.html'),
        ('page-about/emblem.html', '../page-scoutinfo/wood-badge.html'),
        
        # page-scoutinfo directory files (excluding wood-badge.html itself)
        ('page-scoutinfo/apply.html', 'wood-badge.html'),
        ('page-scoutinfo/award.html', 'wood-badge.html'),
        ('page-scoutinfo/mop.html', 'wood-badge.html'),
        ('page-scoutinfo/ranking.html', 'wood-badge.html'),
        ('page-scoutinfo/uniform.html', 'wood-badge.html'),
        ('page-scoutinfo/badge.html', 'wood-badge.html'),
        ('page-scoutinfo/cub.html', 'wood-badge.html'),
        ('page-scoutinfo/scout.html', 'wood-badge.html'),
        ('page-scoutinfo/venture.html', 'wood-badge.html'),
        
        # Root directory template files
        ('left-sidebar.html', 'page-scoutinfo/wood-badge.html'),
        ('right-sidebar.html', 'page-scoutinfo/wood-badge.html'),
        ('no-sidebar.html', 'page-scoutinfo/wood-badge.html'),
        ('promise.html', 'page-scoutinfo/wood-badge.html'),
        ('menu-template.html', 'page-scoutinfo/wood-badge.html'),
    ]
    
    print("👨‍🏫 Updating adult leader menu links...")
    print("=" * 50)
    
    for file_path, wood_badge_path in files_to_update:
        full_path = base_dir / file_path
        
        if full_path.exists():
            if update_adult_leader_link_in_file(full_path, wood_badge_path):
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
    
    print(f"\n👨‍🏫 Adult leader menu links updated successfully!")
    print(f"   '成年領袖' now links to page-scoutinfo/wood-badge.html")

if __name__ == "__main__":
    main()

