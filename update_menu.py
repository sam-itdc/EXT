import os
import re

# 讀取菜單模板
with open('menu-template.html', 'r', encoding='utf-8') as f:
    new_menu = f.read()

# 獲取所有需要更新的HTML文件
html_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') and file not in ['index.html', 'menu-template.html']:
            html_files.append(os.path.join(root, file))

print(f"找到 {len(html_files)} 個需要更新的HTML文件")

updated_count = 0
for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 查找並替換菜單部分
        # 匹配 <nav id="nav"> 到 </nav> 的內容
        nav_pattern = r'<nav id="nav">.*?</nav>'
        
        if re.search(nav_pattern, content, re.DOTALL):
            # 替換菜單
            new_content = re.sub(nav_pattern, new_menu, content, flags=re.DOTALL)
            
            # 寫回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"已更新: {file_path}")
            updated_count += 1
        else:
            print(f"未找到菜單: {file_path}")
    
    except Exception as e:
        print(f"處理 {file_path} 時出錯: {e}")

print(f"總共更新了 {updated_count} 個文件")
