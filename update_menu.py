#!/usr/bin/env python3
import os
import re
import glob

def get_new_menu_for_page_about():
    """為 page-about 目錄下的頁面生成新菜單"""
    return '''						<nav id="nav">
							<ul>
								<li><!--關於我們-->
									<a href="#">關於我們</a>
									<ul>
										<li><a href="introduction.html">總會簡史及本會簡介</a></li>
										<li><a href="patrons.html">會內人員</a></li>
										<li><a href="#">組織架構</a></li>
										<li><a href="departments.html">部門簡介</a></li>
										<li><a href="groups.html">旅部簡介</a></li>
										<li><a href="#">入會辦法</a></li>
										<li><a href="#">更新會員證</a></li>
										<li><a href="#">內部表格</a></li>
									</ul>
								</li>
								<li><!--童軍運動簡介-->
									<a href="#">童軍運動簡介</a>
									<ul>
										<li><a href="../history.html">澳門童軍發展史</a></li>
										<li><a href="../promise.html">誓詞銘言</a></li>
										<li><a href="#">會章會徽</a></li>
										<li><a href="#">徽章介紹</a></li>
										<li><a href="#">制服介紹</a></li>
										<li><a href="#">軍職徽章</a></li>
										<li><a href="#">獎勵制度</a></li>
									</ul>
								</li>
								<li><!--支部簡介-->
									<a href="#">支部簡介</a>
									<ul>
										<li><a href="#">幼童軍</a></li>
										<li><a href="#">童軍</a></li>
										<li><a href="#">深資童軍</a></li>
										<li><a href="#">成年領袖</a></li>
										<li>
											<a href="#">參考資料</a>
											<ul>
												<li><a href="#">標準步操及禮儀</a></li>
												<li><a href="#">貝登堡略傳</a></li>
												<li><a href="#">三指記號</a></li>
												<li><a href="#">生活禮節</a></li>
												<li><a href="#">出版刊物</a></li>
												<li><a href="#">童軍月刊</a></li>
											</ul>
										</li>
									</ul>
								</li>
								<li><!--活動-->
									<a href="#">活動</a>
									<ul>
										<li><a href="#">訓練班消息</a></li>
										<li><a href="#">活動消息</a></li>
										<li><a href="#">國際活動</a></li>
										<li><a href="../page-scoutinfo/mop.html">MOP 和平使者計劃</a></li>
										<li><a href="#">活動行事曆</a></li>
										<li><a href="#">總會通告</a></li>
										<li><a href="#">服務通告</a></li>
									</ul>
								</li>
								<li><!--加入童軍行列-->
									<a href="#">加入童軍</a>
									<ul>
										<li><a href="../page-scoutinfo/apply.html">童軍招募方式</a></li>
										<li><a href="../page-scoutinfo/wood-badge.html">成年領袖招募</a></li>
									</ul>
								</li>
							</ul>
						</nav>'''

def get_new_menu_for_page_scoutinfo():
    """為 page-scoutinfo 目錄下的頁面生成新菜單"""
    return '''						<nav id="nav">
							<ul>
								<li><!--關於我們-->
									<a href="#">關於我們</a>
									<ul>
										<li><a href="../page-about/introduction.html">總會簡史及本會簡介</a></li>
										<li><a href="../page-about/patrons.html">會內人員</a></li>
										<li><a href="#">組織架構</a></li>
										<li><a href="../page-about/departments.html">部門簡介</a></li>
										<li><a href="../page-about/groups.html">旅部簡介</a></li>
										<li><a href="#">入會辦法</a></li>
										<li><a href="#">更新會員證</a></li>
										<li><a href="#">內部表格</a></li>
									</ul>
								</li>
								<li><!--童軍運動簡介-->
									<a href="#">童軍運動簡介</a>
									<ul>
										<li><a href="../history.html">澳門童軍發展史</a></li>
										<li><a href="../promise.html">誓詞銘言</a></li>
										<li><a href="#">會章會徽</a></li>
										<li><a href="#">徽章介紹</a></li>
										<li><a href="#">制服介紹</a></li>
										<li><a href="#">軍職徽章</a></li>
										<li><a href="#">獎勵制度</a></li>
									</ul>
								</li>
								<li><!--支部簡介-->
									<a href="#">支部簡介</a>
									<ul>
										<li><a href="#">幼童軍</a></li>
										<li><a href="#">童軍</a></li>
										<li><a href="#">深資童軍</a></li>
										<li><a href="#">成年領袖</a></li>
										<li>
											<a href="#">參考資料</a>
											<ul>
												<li><a href="#">標準步操及禮儀</a></li>
												<li><a href="#">貝登堡略傳</a></li>
												<li><a href="#">三指記號</a></li>
												<li><a href="#">生活禮節</a></li>
												<li><a href="#">出版刊物</a></li>
												<li><a href="#">童軍月刊</a></li>
											</ul>
										</li>
									</ul>
								</li>
								<li><!--活動-->
									<a href="#">活動</a>
									<ul>
										<li><a href="#">訓練班消息</a></li>
										<li><a href="#">活動消息</a></li>
										<li><a href="#">國際活動</a></li>
										<li><a href="mop.html">MOP 和平使者計劃</a></li>
										<li><a href="#">活動行事曆</a></li>
										<li><a href="#">總會通告</a></li>
										<li><a href="#">服務通告</a></li>
									</ul>
								</li>
								<li><!--加入童軍行列-->
									<a href="#">加入童軍</a>
									<ul>
										<li><a href="apply.html">童軍招募方式</a></li>
										<li><a href="wood-badge.html">成年領袖招募</a></li>
									</ul>
								</li>
							</ul>
						</nav>'''

def get_new_menu_for_root():
    """為根目錄下的頁面生成新菜單"""
    return '''						<nav id="nav">
							<ul>
								<li><!--關於我們-->
									<a href="#">關於我們</a>
									<ul>
										<li><a href="page-about/introduction.html">總會簡史及本會簡介</a></li>
										<li><a href="page-about/patrons.html">會內人員</a></li>
										<li><a href="#">組織架構</a></li>
										<li><a href="page-about/departments.html">部門簡介</a></li>
										<li><a href="page-about/groups.html">旅部簡介</a></li>
										<li><a href="#">入會辦法</a></li>
										<li><a href="#">更新會員證</a></li>
										<li><a href="#">內部表格</a></li>
									</ul>
								</li>
								<li><!--童軍運動簡介-->
									<a href="#">童軍運動簡介</a>
									<ul>
										<li><a href="history.html">澳門童軍發展史</a></li>
										<li><a href="promise.html">誓詞銘言</a></li>
										<li><a href="#">會章會徽</a></li>
										<li><a href="#">徽章介紹</a></li>
										<li><a href="#">制服介紹</a></li>
										<li><a href="#">軍職徽章</a></li>
										<li><a href="#">獎勵制度</a></li>
									</ul>
								</li>
								<li><!--支部簡介-->
									<a href="#">支部簡介</a>
									<ul>
										<li><a href="#">幼童軍</a></li>
										<li><a href="#">童軍</a></li>
										<li><a href="#">深資童軍</a></li>
										<li><a href="#">成年領袖</a></li>
										<li>
											<a href="#">參考資料</a>
											<ul>
												<li><a href="#">標準步操及禮儀</a></li>
												<li><a href="#">貝登堡略傳</a></li>
												<li><a href="#">三指記號</a></li>
												<li><a href="#">生活禮節</a></li>
												<li><a href="#">出版刊物</a></li>
												<li><a href="#">童軍月刊</a></li>
											</ul>
										</li>
									</ul>
								</li>
								<li><!--活動-->
									<a href="#">活動</a>
									<ul>
										<li><a href="#">訓練班消息</a></li>
										<li><a href="#">活動消息</a></li>
										<li><a href="#">國際活動</a></li>
										<li><a href="page-scoutinfo/mop.html">MOP 和平使者計劃</a></li>
										<li><a href="#">活動行事曆</a></li>
										<li><a href="#">總會通告</a></li>
										<li><a href="#">服務通告</a></li>
									</ul>
								</li>
								<li><!--加入童軍行列-->
									<a href="#">加入童軍</a>
									<ul>
										<li><a href="page-scoutinfo/apply.html">童軍招募方式</a></li>
										<li><a href="page-scoutinfo/wood-badge.html">成年領袖招募</a></li>
									</ul>
								</li>
							</ul>
						</nav>'''

def update_menu_in_file(file_path, new_menu):
    """更新文件中的菜單"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 使用正則表達式找到並替換菜單部分
        pattern = r'<nav id="nav">.*?</nav>'
        
        if re.search(pattern, content, re.DOTALL):
            updated_content = re.sub(pattern, new_menu, content, flags=re.DOTALL)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"✅ 已更新: {file_path}")
            return True
        else:
            print(f"⚠️  未找到菜單: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 錯誤處理 {file_path}: {e}")
        return False

def main():
    """主函數"""
    print("開始更新菜單結構...")
    
    updated_files = []
    
    # 更新 page-about 目錄下的文件
    page_about_files = glob.glob("page-about/*.html")
    for file_path in page_about_files:
        if update_menu_in_file(file_path, get_new_menu_for_page_about()):
            updated_files.append(file_path)
    
    # 更新 page-scoutinfo 目錄下的文件
    page_scoutinfo_files = glob.glob("page-scoutinfo/*.html")
    for file_path in page_scoutinfo_files:
        if update_menu_in_file(file_path, get_new_menu_for_page_scoutinfo()):
            updated_files.append(file_path)
    
    # 更新根目錄下的其他 HTML 文件（除了 index.html）
    root_files = [f for f in glob.glob("*.html") if f != "index.html"]
    for file_path in root_files:
        if update_menu_in_file(file_path, get_new_menu_for_root()):
            updated_files.append(file_path)
    
    print(f"\n總共更新了 {len(updated_files)} 個文件:")
    for file_path in updated_files:
        print(f"  - {file_path}")
    
    print("\n菜單更新完成！")

if __name__ == "__main__":
    main()

