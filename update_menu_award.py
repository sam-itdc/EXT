#!/usr/bin/env python3
import os
import re

def update_award_links():
    """更新所有頁面中的獎勵制度鏈接"""
    
    # 定義需要更新的文件和對應的路徑
    files_to_update = {
        # page-about 目錄中的文件
        'page-about/structure.html': '../page-scoutinfo/award.html',
        'page-about/departments.html': '../page-scoutinfo/award.html', 
        'page-about/groups.html': '../page-scoutinfo/award.html',
        'page-about/history.html': '../page-scoutinfo/award.html',
        'page-about/introduction.html': '../page-scoutinfo/award.html',
        'page-about/patrons.html': '../page-scoutinfo/award.html',
        
        # page-scoutinfo 目錄中的文件
        'page-scoutinfo/apply.html': 'award.html',
        'page-scoutinfo/award.html': 'award.html',
        'page-scoutinfo/mop.html': 'award.html',
        'page-scoutinfo/wood-badge.html': 'award.html',
        
        # 根目錄中的文件
        'left-sidebar.html': 'page-scoutinfo/award.html',
        'menu-template.html': 'page-scoutinfo/award.html',
        'no-sidebar.html': 'page-scoutinfo/award.html',
        'promise.html': 'page-scoutinfo/award.html',
        'right-sidebar.html': 'page-scoutinfo/award.html'
    }
    
    updated_files = []
    
    for file_path, award_link in files_to_update.items():
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 查找並替換獎勵制度鏈接
                old_pattern = r'<li><a href="#">獎勵制度</a></li>'
                new_link = f'<li><a href="{award_link}">獎勵制度</a></li>'
                
                if re.search(old_pattern, content):
                    updated_content = re.sub(old_pattern, new_link, content)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    
                    updated_files.append(file_path)
                    print(f"✅ 已更新: {file_path}")
                else:
                    print(f"⚠️  未找到獎勵制度鏈接: {file_path}")
                    
            except Exception as e:
                print(f"❌ 更新失敗: {file_path} - {e}")
        else:
            print(f"⚠️  文件不存在: {file_path}")
    
    print(f"\n總共更新了 {len(updated_files)} 個文件:")
    for file_path in updated_files:
        print(f"  - {file_path}")
    
    print("\n獎勵制度鏈接更新完成！")

if __name__ == "__main__":
    print("開始更新獎勵制度鏈接...")
    update_award_links()

