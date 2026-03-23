const SITE_SHELL_LABELS = {
  "/aboutus.html": [{ label: "\u95dc\u65bc\u6211\u5011" }],
  "/contact.html": [{ label: "\u806f\u7d61\u6211\u5011" }],
  "/news.html": [{ label: "\u901a\u544a" }],
  "/newsletters.html": [{ label: "\u7ae5\u8ecd\u6708\u520a" }],
  "/promise.html": [{ label: "\u7ae5\u8ecd\u8a93\u8a5e\u3001\u9298\u8a00\u53ca\u898f\u5f8b" }],
  "/scout.html": [{ label: "\u7ae5\u8ecd\u904b\u52d5\u7c21\u4ecb" }],
  "/scout-resources.html": [{ label: "\u53c3\u8003\u8cc7\u6599" }],
  "/scout-sections.html": [{ label: "\u652f\u90e8\u7c21\u4ecb" }],
  "/page-about/introduction.html": [{ label: "\u95dc\u65bc\u6211\u5011", href: "/aboutus.html" }, { label: "\u7e3d\u6703\u7c21\u4ecb" }],
  "/page-about/patrons.html": [{ label: "\u95dc\u65bc\u6211\u5011", href: "/aboutus.html" }, { label: "\u6703\u5167\u4eba\u54e1" }],
  "/page-about/structure.html": [{ label: "\u95dc\u65bc\u6211\u5011", href: "/aboutus.html" }, { label: "\u7d44\u7e54\u67b6\u69cb" }],
  "/page-about/departments.html": [{ label: "\u95dc\u65bc\u6211\u5011", href: "/aboutus.html" }, { label: "\u90e8\u9580\u7c21\u4ecb" }],
  "/page-about/groups.html": [{ label: "\u95dc\u65bc\u6211\u5011", href: "/aboutus.html" }, { label: "\u65c5\u90e8\u7c21\u4ecb" }],
  "/page-about/forms.html": [{ label: "\u95dc\u65bc\u6211\u5011", href: "/aboutus.html" }, { label: "\u8868\u683c" }],
  "/page-about/history.html": [{ label: "\u7ae5\u8ecd\u904b\u52d5\u7c21\u4ecb", href: "/scout.html" }, { label: "\u6fb3\u9580\u7ae5\u8ecd\u767c\u5c55\u53f2" }],
  "/page-about/emblem.html": [{ label: "\u7ae5\u8ecd\u904b\u52d5\u7c21\u4ecb", href: "/scout.html" }, { label: "\u6703\u5fbd" }],
  "/page-about/references/baden-powell.html": [{ label: "\u53c3\u8003\u8cc7\u6599", href: "/scout-resources.html" }, { label: "\u8c9d\u767b\u5821\u7565\u50b3" }],
  "/page-about/references/courtesy.html": [{ label: "\u53c3\u8003\u8cc7\u6599", href: "/scout-resources.html" }, { label: "\u751f\u6d3b\u79ae\u7bc0" }],
  "/page-about/references/marching.html": [{ label: "\u53c3\u8003\u8cc7\u6599", href: "/scout-resources.html" }, { label: "\u6a19\u6e96\u6b65\u64cd\u53ca\u79ae\u5100" }],
  "/page-about/references/signal.html": [{ label: "\u53c3\u8003\u8cc7\u6599", href: "/scout-resources.html" }, { label: "\u4e09\u6307\u8a18\u865f" }],
  "/page-about/references/training.html": [{ label: "\u53c3\u8003\u8cc7\u6599", href: "/scout-resources.html" }, { label: "\u51fa\u7248\u520a\u7269" }],
  "/page-scoutinfo/apply.html": [{ label: "\u95dc\u65bc\u6211\u5011", href: "/aboutus.html" }, { label: "\u52a0\u5165\u7ae5\u8ecd" }],
  "/page-scoutinfo/award.html": [{ label: "\u7ae5\u8ecd\u904b\u52d5\u7c21\u4ecb", href: "/scout.html" }, { label: "\u734e\u52f5\u5236\u5ea6" }],
  "/page-scoutinfo/badge.html": [{ label: "\u7ae5\u8ecd\u904b\u52d5\u7c21\u4ecb", href: "/scout.html" }, { label: "\u5fbd\u7ae0\u4ecb\u7d39" }],
  "/page-scoutinfo/cub.html": [{ label: "\u652f\u90e8\u7c21\u4ecb", href: "/scout-sections.html" }, { label: "\u5e7c\u7ae5\u8ecd" }],
  "/page-scoutinfo/mop.html": [{ label: "\u901a\u544a", href: "/news.html" }, { label: "MOP \u548c\u5e73\u4f7f\u8005\u8a08\u5283" }],
  "/page-scoutinfo/ranking.html": [{ label: "\u7ae5\u8ecd\u904b\u52d5\u7c21\u4ecb", href: "/scout.html" }, { label: "\u8ecd\u8077\u5fbd\u7ae0" }],
  "/page-scoutinfo/scout.html": [{ label: "\u652f\u90e8\u7c21\u4ecb", href: "/scout-sections.html" }, { label: "\u7ae5\u8ecd" }],
  "/page-scoutinfo/uniform.html": [{ label: "\u7ae5\u8ecd\u904b\u52d5\u7c21\u4ecb", href: "/scout.html" }, { label: "\u5236\u670d\u4ecb\u7d39" }],
  "/page-scoutinfo/venture.html": [{ label: "\u652f\u90e8\u7c21\u4ecb", href: "/scout-sections.html" }, { label: "\u6df1\u8cc7\u7ae5\u8ecd" }],
  "/page-scoutinfo/wood-badge.html": [{ label: "\u652f\u90e8\u7c21\u4ecb", href: "/scout-sections.html" }, { label: "\u6210\u5e74\u9818\u8896" }]
};

function getSiteRoot(prefix) {
  const cleanPath = window.location.pathname.replace(/\/+$/, "");
  const parts = cleanPath.split("/");
  const currentDepth = parts.length - 2;
  const prefixDepth = (prefix.match(/\.\.\//g) || []).length;
  const rootIndex = Math.max(0, currentDepth - prefixDepth);
  const rootParts = parts.slice(0, rootIndex + 1);
  const root = rootParts.join("/") || "";
  return root ? root + "/" : "/";
}

function stripSiteRoot(pathname, siteRoot) {
  if (siteRoot !== "/" && pathname.indexOf(siteRoot) === 0) {
    return pathname.slice(siteRoot.length - 1) || "/";
  }
  return pathname || "/";
}

function resolveLabels(pathname) {
  if (SITE_SHELL_LABELS[pathname]) return SITE_SHELL_LABELS[pathname];
  if (!/\.html$/i.test(pathname) && SITE_SHELL_LABELS[pathname + ".html"]) {
    return SITE_SHELL_LABELS[pathname + ".html"];
  }
  return null;
}

function withSiteRoot(path, siteRoot) {
  if (!path || /^https?:\/\//i.test(path) || path.indexOf("//") === 0) return path;
  if (path.charAt(0) !== "/") return path;
  if (siteRoot === "/") return path;
  return siteRoot.replace(/\/$/, "") + path;
}

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

  const siteRoot = getSiteRoot(window.__siteShellPrefix || "");
  const pathname = stripSiteRoot(window.location.pathname.replace(/\/+$/, "") || "/", siteRoot);
  const labels = resolveLabels(pathname);
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
  nav.setAttribute("aria-label", "\u73fe\u5728\u4f4d\u7f6e");

  const parts = labels
    .map((item) => {
      const content = item.href
        ? '<a href="' + withSiteRoot(item.href, siteRoot) + '">' + item.label + "</a>"
        : "<span>" + item.label + "</span>";
      return '<span class="breadcrumb-sep">/</span>' + content;
    })
    .join("");

  nav.innerHTML =
    '<span class="breadcrumb-label">\u73fe\u5728\u4f4d\u7f6e</span>' +
    '<div class="breadcrumb-trail">' +
    '<a href="' + withSiteRoot("/index.html", siteRoot) + '">\u9996\u9801</a>' +
    parts +
    "</div>";

  target.insertBefore(nav, target.firstChild);
}

function initSiteShell(prefix) {
  window.__siteShellPrefix = prefix || "";
  const headerTarget = document.getElementById("header-slot") ? "header-slot" : "header";
  const footerTarget = document.getElementById("footer-slot") ? "footer-slot" : "footer";
  const siteRoot = getSiteRoot(window.__siteShellPrefix);

  loadHTML(headerTarget, prefix + "includes/header.html", (target) => {
    const header = target.querySelector(".header-wrap");
    if (header) {
      header.id = "site-header";
    }

    target.querySelectorAll('a[href^="/"]').forEach((link) => {
      link.setAttribute("href", withSiteRoot(link.getAttribute("href"), siteRoot));
    });

    target.querySelectorAll('img[src^="/"]').forEach((img) => {
      img.setAttribute("src", withSiteRoot(img.getAttribute("src"), siteRoot));
    });
  });

  loadHTML(footerTarget, prefix + "includes/footer.html");
  insertBreadcrumb();
}
