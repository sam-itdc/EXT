#!/usr/bin/env python3
"""
Script to update forms menu items across all pages
Changes "內部表格" to "表格" and updates links to forms.html
"""

import os
import re
from pathlib import Path

def update_forms_menu_in_file(file_path, relative_path_to_forms):
    """Update the forms menu item in a single HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find and update the internal forms menu item
        # This will match both the text and the link
        pattern = r'<li><a href="[^"]*">內部表格</a></li>'
        replacement = f'<li><a href="{relative_path_to_forms}">表格</a></li>'
        
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
    
    # Define file paths and their corresponding relative paths to forms.html
    files_to_update = [
        # page-about directory files
        ('page-about/introduction.html', 'forms.html'),
        ('page-about/patrons.html', 'forms.html'),
        ('page-about/structure.html', 'forms.html'),
        ('page-about/departments.html', 'forms.html'),
        ('page-about/groups.html', 'forms.html'),
        ('page-about/history.html', 'forms.html'),
        
        # page-scoutinfo directory files
        ('page-scoutinfo/apply.html', '../page-about/forms.html'),
        ('page-scoutinfo/award.html', '../page-about/forms.html'),
        ('page-scoutinfo/mop.html', '../page-about/forms.html'),
        ('page-scoutinfo/wood-badge.html', '../page-about/forms.html'),
        ('page-scoutinfo/ranking.html', '../page-about/forms.html'),
        ('page-scoutinfo/uniform.html', '../page-about/forms.html'),
        ('page-scoutinfo/badge.html', '../page-about/forms.html'),
        
        # Root directory template files
        ('left-sidebar.html', 'page-about/forms.html'),
        ('right-sidebar.html', 'page-about/forms.html'),
        ('no-sidebar.html', 'page-about/forms.html'),
        ('promise.html', 'page-about/forms.html'),
        ('menu-template.html', 'page-about/forms.html'),
    ]
    
    print("📋 Updating forms menu items...")
    print("=" * 50)
    
    for file_path, forms_path in files_to_update:
        full_path = base_dir / file_path
        
        if full_path.exists():
            if update_forms_menu_in_file(full_path, forms_path):
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
    
    print(f"\n🎯 Forms menu items updated successfully!")
    print(f"   '內部表格' has been renamed to '表格' and links to forms.html")

if __name__ == "__main__":
    main()

