(function () {
  function parseDate(text) {
    const compact = text.match(/(20\d{2})(\d{2})(\d{2})/);
    if (compact) {
      const [, y, m, d] = compact;
      return new Date(`${y}-${m}-${d}T00:00:00Z`);
    }

    const dashed = text.match(/(20\d{2})[-_](\d{2})[-_](\d{2})/);
    if (dashed) {
      const [, y, m, d] = dashed;
      return new Date(`${y}-${m}-${d}T00:00:00Z`);
    }

    return null;
  }

  function formatDate(date) {
    if (!date) return "未标注日期";
    const y = date.getUTCFullYear();
    const m = String(date.getUTCMonth() + 1).padStart(2, "0");
    const d = String(date.getUTCDate()).padStart(2, "0");
    return `${y}-${m}-${d}`;
  }

  function getCategoryFromHref(href) {
    const cleanHref = href.split("#")[0].split("?")[0];
    const segments = cleanHref.split("/").filter(Boolean);
    if (segments.length <= 1) return "其他";
    return decodeURIComponent(segments[segments.length - 2]);
  }

  function collectPosts() {
    const links = Array.from(document.querySelectorAll("#sidebar a"));
    const seen = new Set();

    return links
      .map((a) => {
        const href = a.getAttribute("href") || "";
        if (!href || !href.endsWith(".html") || href.includes("print.html")) return null;
        if (href.endsWith("about-me.html") || href.endsWith("文章导航.html")) return null;

        const absolute = new URL(href, window.location.href).href;
        if (seen.has(absolute)) return null;
        seen.add(absolute);

        const title = (a.textContent || "").trim();
        const date = parseDate(title) || parseDate(decodeURIComponent(href));
        const category = getCategoryFromHref(decodeURIComponent(href));

        return { title, href, date, category };
      })
      .filter(Boolean)
      .sort((a, b) => {
        if (a.date && b.date) return b.date - a.date;
        if (a.date) return -1;
        if (b.date) return 1;
        return a.title.localeCompare(b.title, "zh-Hans-CN");
      });
  }

  function render(container, posts) {
    const categories = ["全部", ...Array.from(new Set(posts.map((p) => p.category))).sort((a, b) => a.localeCompare(b, "zh-Hans-CN"))];

    container.innerHTML = `
      <section class="post-index-controls">
        <label class="post-index-label" for="post-index-search">关键词</label>
        <input id="post-index-search" class="post-index-search" type="search" placeholder="输入标题关键词..." />
        <div class="post-index-categories" id="post-index-categories"></div>
      </section>
      <p class="post-index-tip">说明：按日期倒序展示；若标题/文件名不包含日期（YYYYMMDD 或 YYYY-MM-DD），将归为“未标注日期”。</p>
      <ul class="post-index-list" id="post-index-list"></ul>
    `;

    const categoryBox = container.querySelector("#post-index-categories");
    const searchInput = container.querySelector("#post-index-search");
    const list = container.querySelector("#post-index-list");

    let activeCategory = "全部";

    function renderCategoryButtons() {
      categoryBox.innerHTML = categories
        .map(
          (cat) => `<button type="button" class="post-index-category ${cat === activeCategory ? "active" : ""}" data-cat="${cat}">${cat}</button>`
        )
        .join("");
    }

    function renderPosts() {
      const keyword = (searchInput.value || "").trim().toLowerCase();
      const filtered = posts.filter((p) => {
        const catMatched = activeCategory === "全部" || p.category === activeCategory;
        const keywordMatched = !keyword || p.title.toLowerCase().includes(keyword);
        return catMatched && keywordMatched;
      });

      list.innerHTML = filtered
        .map(
          (p) => `
            <li class="post-index-item">
              <a class="post-index-link" href="${p.href}">${p.title}</a>
              <div class="post-index-meta">
                <span class="post-index-date">${formatDate(p.date)}</span>
                <span class="post-index-dot">•</span>
                <span class="post-index-tag">${p.category}</span>
              </div>
            </li>
          `
        )
        .join("");

      if (!filtered.length) {
        list.innerHTML = '<li class="post-index-empty">没有匹配到文章，请调整关键词或分类。</li>';
      }
    }

    categoryBox.addEventListener("click", (event) => {
      const button = event.target.closest("button[data-cat]");
      if (!button) return;
      activeCategory = button.dataset.cat;
      renderCategoryButtons();
      renderPosts();
    });

    searchInput.addEventListener("input", renderPosts);

    renderCategoryButtons();
    renderPosts();
  }

  document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("post-index-root");
    if (!container) return;

    const posts = collectPosts();
    render(container, posts);
  });
})();
