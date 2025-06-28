# 菜單連結修復建議清單

## 🚀 立即可修復的連結 (22個項目)

### 1. 童軍運動簡介 → 童軍分類
```html
<!-- 當前 -->
<li><a href="#">幼童軍</a></li>
<li><a href="#">童軍</a></li>
<li><a href="#">深資童軍</a></li>
<li><a href="#">成年領袖</a></li>

<!-- 建議修復為 -->
<li><a href="page-scoutinfo/cub.html">幼童軍</a></li>
<li><a href="page-scoutinfo/scout.html">童軍</a></li>
<li><a href="page-scoutinfo/venture.html">深資童軍</a></li>
<li><a href="page-scoutinfo/apply-adult.html">成年領袖</a></li>
```

### 2. 童軍運動簡介 → 童軍運動介紹
```html
<!-- 當前 -->
<li><a href="#">徽章介紹</a></li>
<li><a href="#">制服介紹</a></li>
<li><a href="#">獎勵制度</a></li>

<!-- 建議修復為 -->
<li><a href="page-scoutinfo/badges.html">徽章介紹</a></li>
<li><a href="page-scoutinfo/uniform.html">制服介紹</a></li>
<li><a href="page-scoutinfo/award.html">獎勵制度</a></li>
```

### 3. 童軍運動簡介 → 參考資料
```html
<!-- 當前 -->
<li><a href="#">標準步操及禮儀</a></li>
<li><a href="#">貝登堡略傳</a></li>
<li><a href="#">三指記號</a></li>
<li><a href="#">生活禮節</a></li>

<!-- 建議修復為 -->
<li><a href="page-about/references/marching.html">標準步操及禮儀</a></li>
<li><a href="page-about/references/baden-powell.html">貝登堡略傳</a></li>
<li><a href="page-about/references/signal.html">三指記號</a></li>
<li><a href="page-about/references/courtesy.html">生活禮節</a></li>
```

### 4. 加入童軍行列
```html
<!-- 當前 -->
<li><a href="apply">童軍招募方式</a></li>
<li><a href="#">成年領袖招募</a></li>

<!-- 建議修復為 -->
<li><a href="page-scoutinfo/apply-scout.html">童軍招募方式</a></li>
<li><a href="page-scoutinfo/apply-adult.html">成年領袖招募</a></li>
```

### 5. 活動及訓練
```html
<!-- 當前 -->
<li><a href="#">活動行事曆</a></li>

<!-- 建議修復為 -->
<li><a href="page-activities/calendar.html">活動行事曆</a></li>
```

### 6. 部門及通告 → 通告
```html
<!-- 當前 -->
<li><a href="#">總會通告</a></li>
<li><a href="#">活動消息</a></li>
<li><a href="#">訓練班消息</a></li>
<li><a href="#">會內及社會服務</a></li>
<li><a href="#">童軍月刊</a></li>
<li><a href="#">旅團快訊</a></li>
<li><a href="#">國際活動</a></li>

<!-- 建議修復為 -->
<li><a href="page-news/hqnotices.html">總會通告</a></li>
<li><a href="page-news/activities.html">活動消息</a></li>
<li><a href="page-news/training.html">訓練班消息</a></li>
<li><a href="page-news/services.html">會內及社會服務</a></li>
<li><a href="page-news/newsletter.html">童軍月刊</a></li>
<li><a href="page-news/groupnews.html">旅團快訊</a></li>
<li><a href="page-news/intactivities.html">國際活動</a></li>
```

### 7. 關於我們
```html
<!-- 當前 -->
<li><a href="#">總會簡史</a></li>
<li><a href="#">會內人員</a></li>
<li><a href="#">組織架構</a></li>
<li><a href="#">部門簡介</a></li>
<li><a href="#">旅部簡介</a></li>
<li><a href="#">會章會徽</a></li>

<!-- 建議修復為 -->
<li><a href="page-about/hq-history.html">總會簡史</a></li>
<li><a href="page-about/namelist.html">會內人員</a></li>
<li><a href="page-about/structure.html">組織架構</a></li>
<li><a href="page-about/department.html">部門簡介</a></li>
<li><a href="page-about/group.html">旅部簡介</a></li>
<li><a href="page-about/identity.html">會章會徽</a></li>
```

### 8. 關於我們 → 表格下載
```html
<!-- 當前 -->
<li><a href="#">入會辦法</a></li>
<li><a href="#">更新會員證</a></li>
<li><a href="#">內部表格</a></li>

<!-- 建議修復為 -->
<li><a href="page-about/forms/application.html">入會辦法</a></li>
<li><a href="page-about/forms/renewal.html">更新會員證</a></li>
<li><a href="page-about/forms/internal-forms.html">內部表格</a></li>
```

## 📋 需要創建的頁面 (13個項目)

### 高優先級 (建議優先創建)
1. **聯絡我們** - 重要的聯繫信息頁面
2. **MOP 和平使者計劃** - 特色項目頁面
3. **軍職徽章** - 童軍制度重要組成部分

### 中優先級 (部門頁面)
4. **訓練部**
5. **支部計劃部**
6. **國際事務部**
7. **資訊科技部**

### 低優先級 (可與現有頁面合併)
8. **訓練班消息** (可重定向到 page-news/training.html)
9. **活動消息** (可重定向到 page-news/activities.html)
10. **國際活動** (可重定向到 page-news/intactivities.html)
11. **領袖招募計劃** (可與成年領袖招募合併)
12. **出版刊物** (可與童軍月刊合併)
13. **統計數字** (可創建簡單的統計頁面)

## 🎯 實施建議

### 階段1：修復現有連結 (立即執行)
- 完成度從71%提升到93%
- 工作量：約1-2小時
- 影響：大幅改善用戶體驗

### 階段2：創建高優先級頁面 (短期)
- 創建聯絡我們、MOP計劃、軍職徽章頁面
- 完成度提升到98%

### 階段3：完善剩餘頁面 (中期)
- 創建部門頁面和其他缺失頁面
- 達到100%完成度

