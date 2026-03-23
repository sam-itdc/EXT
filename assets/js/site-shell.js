const SITE_SHELL_LABELS = {
  "/aboutus.html": [{ label: "關於我們" }],
  "/contact.html": [{ label: "聯絡我們" }],
  "/news.html": [{ label: "通告" }],
  "/newsletters.html": [{ label: "童軍月刊" }],
  "/promise.html": [{ label: "童軍誓詞、銘言及規律" }],
  "/scout.html": [{ label: "童軍運動簡介" }],
  "/scout-resources.html": [{ label: "參考資料" }],
  "/scout-sections.html": [{ label: "支部簡介" }],
  "/page-about/introduction.html": [{ label: "關於我們", href: "/aboutus.html" }, { label: "總會簡介" }],
  "/page-about/patrons.html": [{ label: "關於我們", href: "/aboutus.html" }, { label: "會內人員" }],
  "/page-about/structure.html": [{ label: "關於我們", href: "/aboutus.html" }, { label: "組織架構" }],
  "/page-about/departments.html": [{ label: "關於我們", href: "/aboutus.html" }, { label: "部門簡介" }],
  "/page-about/groups.html": [{ label: "關於我們", href: "/aboutus.html" }, { label: "旅部簡介" }],
  "/page-about/forms.html": [{ label: "關於我們", href: "/aboutus.html" }, { label: "表格" }],
  "/page-about/history.html": [{ label: "童軍運動簡介", href: "/scout.html" }, { label: "澳門童軍發展史" }],
  "/page-about/emblem.html": [{ label: "童軍運動簡介", href: "/scout.html" }, { label: "會徽" }],
  "/page-about/references/baden-powell.html": [{ label: "參考資料", href: "/scout-resources.html" }, { label: "貝登堡略傳" }],
  "/page-about/references/courtesy.html": [{ label: "參考資料", href: "/scout-resources.html" }, { label: "生活禮節" }],
  "/page-about/references/marching.html": [{ label: "參考資料", href: "/scout-resources.html" }, { label: "標準步操及禮儀" }],
  "/page-about/references/signal.html": [{ label: "參考資料", href: "/scout-resources.html" }, { label: "三指記號" }],
  "/page-about/references/training.html": [{ label: "參考資料", href: "/scout-resources.html" }, { label: "出版刊物" }],
  "/page-scoutinfo/apply.html": [{ label: "關於我們", href: "/aboutus.html" }, { label: "加入童軍" }],
  "/page-scoutinfo/award.html": [{ label: "童軍運動簡介", href: "/scout.html" }, { label: "獎勵制度" }],
  "/page-scoutinfo/badge.html": [{ label: "童軍運動簡介", href: "/scout.html" }, { label: "徽章介紹" }],
  "/page-scoutinfo/cub.html": [{ label: "支部簡介", href: "/scout-sections.html" }, { label: "幼童軍" }],
  "/page-scoutinfo/mop.html": [{ label: "通告", href: "/news.html" }, { label: "MOP 和平使者計劃" }],
  "/page-scoutinfo/ranking.html": [{ label: "童軍運動簡介", href: "/scout.html" }, { label: "軍職徽章" }],
  "/page-scoutinfo/scout.html": [{ label: "支部簡介", href: "/scout-sections.html" }, { label: "童軍" }],
  "/page-scoutinfo/uniform.html": [{ label: "童軍運動簡介", href: "/scout.html" }, { label: "制服介紹" }],
  "/page-scoutinfo/venture.html": [{ label: "支部簡介", href: "/scout-sections.html" }, { label: "深資童軍" }],
  "/page-scoutinfo/wood-badge.html": [{ label: "支部簡介", href: "/scout-sections.html" }, { label: "成年領袖" }]
};

function loadHTML(id, url, callback) {
  fetch(url)
    .then((res) => res.text())
    .then((data) => {
      const target = document.getElementById(id);
      if (!target) return;
      target.innerHTML = data;
      if (typeof callback === "function") callback(target);
    });
}

function toggleMenu() {
  const menu = document.getElementById("menu");
  if (menu) {
    menu.classList.toggle("show");
  }
}

function insertBreadcrumb() {
  if (
    document.body.classList.contains("homepage") ||
    document.body.classList.contains("no-breadcrumb")
  ) return;

  const pathname = window.location.pathname.replace(/\/+$/, "") || "/";
  const labels = SITE_SHELL_LABELS[pathname];
  if (!labels || !labels.length) return;

  const target =
    document.querySelector(".hero-content") ||
    document.querySelector("#content article") ||
    document.querySelector("#content") ||
    document.querySelector(".content") ||
    document.querySelector("main") ||
    document.querySelector(".container");

  if (!target || target.querySelector(".site-breadcrumb")) return;

  const nav = document.createElement("nav");
  nav.className = "site-breadcrumb";
  nav.setAttribute("aria-label", "現在位置");

  const parts = labels
    .map((item) => {
      const content = item.href
        ? '<a href="' + item.href + '">' + item.label + '</a>'
        : '<span>' + item.label + '</span>';
      return '<span class="breadcrumb-sep">/</span>' + content;
    })
    .join("");

  nav.innerHTML =
    '<span class="breadcrumb-label">現在位置</span>' +
    '<div class="breadcrumb-trail">' +
    '<a href="/index.html">首頁</a>' +
    parts +
    '</div>';

  target.insertBefore(nav, target.firstChild);
}

function initSiteShell(prefix) {
  const headerTarget = document.getElementById("header-slot") ? "header-slot" : "header";
  const footerTarget = document.getElementById("footer-slot") ? "footer-slot" : "footer";

  loadHTML(headerTarget, prefix + "includes/header.html", (target) => {
    const header = target.querySelector(".header-wrap");
    if (header) {
      header.id = "site-header";
    }
  });

  loadHTML(footerTarget, prefix + "includes/footer.html");
  insertBreadcrumb();
}
