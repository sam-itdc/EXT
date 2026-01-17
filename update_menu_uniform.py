#!/usr/bin/env python3
"""
Script to update uniform introduction menu links across all pages
Updates the "制服介紹" link to point to uniform.html
"""

import os
import re
from pathlib import Path

def update_uniform_link_in_file(file_path, relative_path_to_uniform):
    """Update the uniform introduction link in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find the uniform introduction menu item
        pattern = r'<li><a href="[^"]*">制服介紹</a></li>'
        replacement = f'<li><a href="{relative_path_to_uniform}">制服介紹</a></li>'
        
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
    
    # Define file paths and their corresponding relative paths to uniform.html
    files_to_update = [
        # page-about directory files
        ('page-about/introduction.html', '../page-scoutinfo/uniform.html'),
        ('page-about/patrons.html', '../page-scoutinfo/uniform.html'),
        ('page-about/structure.html', '../page-scoutinfo/uniform.html'),
        ('page-about/departments.html', '../page-scoutinfo/uniform.html'),
        ('page-about/groups.html', '../page-scoutinfo/uniform.html'),
        ('page-about/history.html', '../page-scoutinfo/uniform.html'),
        
        # page-scoutinfo directory files
        ('page-scoutinfo/apply.html', 'uniform.html'),
        ('page-scoutinfo/award.html', 'uniform.html'),
        ('page-scoutinfo/mop.html', 'uniform.html'),
        ('page-scoutinfo/wood-badge.html', 'uniform.html'),
        ('page-scoutinfo/ranking.html', 'uniform.html'),
        
        # Root directory template files
        ('left-sidebar.html', 'page-scoutinfo/uniform.html'),
        ('right-sidebar.html', 'page-scoutinfo/uniform.html'),
        ('no-sidebar.html', 'page-scoutinfo/uniform.html'),
        ('promise.html', 'page-scoutinfo/uniform.html'),
        ('menu-template.html', 'page-scoutinfo/uniform.html'),
    ]
    
    print("👕 Updating uniform introduction menu links...")
    print("=" * 50)
    
    for file_path, uniform_path in files_to_update:
        full_path = base_dir / file_path
        
        if full_path.exists():
            if update_uniform_link_in_file(full_path, uniform_path):
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
    
    print(f"\n🎯 Uniform introduction menu links updated successfully!")
    print(f"   All pages now link to uniform.html")

if __name__ == "__main__":
    main()

