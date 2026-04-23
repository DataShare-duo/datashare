#!/usr/bin/env python3
"""
自动从 SUMMARY.md 提取文章信息并生成 blog-index.md
支持从文件名中提取日期（格式：YYYYMMDD-）
"""

import re
import os
from pathlib import Path
from datetime import datetime
import random

def extract_date_from_filename(filename):
    """从文件名中提取日期，支持格式：YYYYMMDD-"""
    match = re.match(r'(\d{8})-', filename)
    if match:
        date_str = match.group(1)
        try:
            # 验证日期是否有效
            date_obj = datetime.strptime(date_str, '%Y%m%d')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            return None
    return None

def parse_summary_md(summary_path):
    """解析 SUMMARY.md 文件，提取所有文章信息"""
    posts = []
    current_category = None
    
    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    category_stack = []
    
    for line in lines:
        stripped = line.strip()
        
        # 跳过空行和注释
        if not stripped or stripped.startswith('#'):
            continue
        
        # 计算缩进级别（每级缩进为 1 个 tab 或 4 个空格）
        indent = len(line) - len(line.lstrip())
        if line.startswith('\t'):
            indent_level = indent
        else:
            indent_level = indent // 2
        
        # 检测分类标题（以 - [分类名]() 或 - [分类名](#) 形式）
        category_match = re.match(r'^\s*-\s*\[([^\]]+)\]\(\s*(\#)?\s*\)', line)
        if category_match:
            category_name = category_match.group(1).strip()
            if category_name:
                # 根据缩进级别管理分类层级
                while category_stack and category_stack[-1][1] >= indent_level:
                    category_stack.pop()
                category_stack.append((category_name, indent_level))
                current_category = '/'.join([cat[0] for cat in category_stack])
            continue
        
        # 匹配文章链接
        # 格式：- [标题](路径/文件名.md)
        article_match = re.search(r'- \[([^\]]+)\]\(([^\)]+\.md)\)', line)
        if article_match:
            title = article_match.group(1).strip()
            path = article_match.group(2).strip()
            
            # 跳过特殊页面
            if title in ['关于小编', '博客文章列表'] or path == 'about-me.md':
                continue
            
            # 从路径中提取文件名
            filename = os.path.basename(path)
            
            # 尝试从文件名提取日期
            date = extract_date_from_filename(filename)
            
            # 确定分类（使用最近的非空分类）
            category = current_category if current_category else '其他'
            
            # 将 .md 转换为 .html
            html_path = path.replace('.md', '.html')
            
            posts.append({
                'title': title,
                'path': html_path,
                'date': date,
                'category': category
            })
    
    return posts

def generate_blog_index(posts, output_path):
    """生成 blog-index.md 文件"""
    
    # 分离有日期和无日期的文章
    dated_posts = [p for p in posts if p['date']]
    undated_posts = [p for p in posts if not p['date']]
    
    # 有日期的按时间倒序排序
    dated_posts.sort(key=lambda x: x['date'], reverse=True)
    
    # 无日期的随机排序
    random.shuffle(undated_posts)
    
    # 合并文章列表
    all_posts = dated_posts + undated_posts
    
    # 生成 JavaScript 数组
    posts_js = []
    for i, post in enumerate(all_posts):
        date_str = f'"{post["date"]}"' if post['date'] else 'null'
        comma = ',' if i < len(all_posts) - 1 else ''
        # 转义标题中的引号
        safe_title = post['title'].replace('"', '\\"')
        posts_js.append(f'    {{title: "{safe_title}", path: "{post["path"]}", date: {date_str}, category: "{post["category"]}"}}{comma}')
    
    # 获取所有分类
    categories = sorted(set(p['category'] for p in posts))
    
    js_content = '\n'.join(posts_js)
    
    template = f'''# 博客文章列表

<div id="blog-posts" style="max-width: 900px; margin: 0 auto; padding: 20px;">
    <div style="text-align: center; margin-bottom: 30px;">
        <p style="font-size: 1.2em; color: #666;">欢迎来到 DataShare 博客！以下是所有文章，按发布时间倒序排列。</p>
        <p style="font-size: 0.9em; color: #999;">💡 提示：部分文章尚未标注日期，这些文章将随机显示在列表底部</p>
    </div>
    
    <!-- 搜索框 -->
    <div style="margin-bottom: 20px;">
        <input type="text" id="search-input" placeholder="🔍 搜索文章标题..." 
               style="width: 100%; padding: 12px 15px; font-size: 16px; border: 2px solid #ddd; border-radius: 8px; outline: none; transition: border-color 0.3s;">
    </div>
    
    <!-- 分类筛选 -->
    <div style="margin-bottom: 20px; display: flex; flex-wrap: wrap; gap: 10px;" id="category-filters">
        <button class="filter-btn active" data-category="all" style="padding: 8px 16px; border: none; border-radius: 20px; background: #e45e28; color: white; cursor: pointer; font-size: 14px;">全部</button>
    </div>
    
    <!-- 文章列表 -->
    <div id="posts-container" style="display: grid; gap: 15px;"></div>
    
    <!-- 统计信息 -->
    <div style="margin-top: 30px; padding: 15px; background: #f8f9fa; border-radius: 8px; text-align: center;">
        <p id="stats-info" style="color: #666; font-size: 14px;"></p>
    </div>
</div>

<script>
// 博客文章数据 - 自动生成，请勿手动修改
// 如需添加新文章，请在 SUMMARY.md 中添加对应的链接
const blogPosts = [
{js_content}
];

// 随机打乱无日期文章的顺序
function shuffleArray(array) {{
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }}
    return shuffled;
}}

// 格式化日期显示
function formatDate(dateStr) {{
    if (!dateStr) return '';
    const date = new Date(dateStr);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${{year}}-${{month}}-${{day}}`;
}}

// 获取相对时间描述
function getRelativeTime(dateStr) {{
    if (!dateStr) return '';
    const date = new Date(dateStr);
    const now = new Date();
    const diffTime = now - date;
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return '今天';
    if (diffDays === 1) return '昨天';
    if (diffDays < 7) return `${{diffDays}}天前`;
    if (diffDays < 30) return `${{Math.floor(diffDays / 7)}}周前`;
    if (diffDays < 365) return `${{Math.floor(diffDays / 30)}}月前`;
    return `${{Math.floor(diffDays / 365)}}年前`;
}}

// 渲染文章卡片
function renderPostCard(post) {{
    const dateDisplay = post.date ? 
        `<span class="post-date" style="color: #e45e28; font-size: 0.85em; font-weight: 600;">📅 ${{formatDate(post.date)}}</span>` :
        `<span class="post-date" style="color: #999; font-size: 0.85em;">📅 待补充日期</span>`;
    
    const relativeTime = post.date ? 
        `<span style="color: #999; font-size: 0.8em; margin-left: 10px;">(${{getRelativeTime(post.date)}})</span>` : '';
    
    return `
        <a href="${{post.path}}" class="post-card" style="
            display: block;
            padding: 20px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            text-decoration: none;
            color: inherit;
            transition: all 0.3s ease;
            border-left: 4px solid ${{post.date ? '#e45e28' : '#ccc'}};
        " onmouseover="this.style.transform='translateX(5px)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.12)'" 
           onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.08)'">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1; min-width: 0;">
                    <h3 style="margin: 0 0 8px 0; font-size: 1.1em; color: #333; line-height: 1.4;">${{post.title}}</h3>
                    <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                        ${{dateDisplay}}${{relativeTime}}
                        <span class="post-category" style="
                            background: ${{post.date ? '#fff3e0' : '#f5f5f5'}}; 
                            color: ${{post.date ? '#e45e28' : '#999'}}; 
                            padding: 3px 10px; 
                            border-radius: 12px; 
                            font-size: 0.8em;
                            font-weight: 500;
                        ">📁 ${{post.category}}</span>
                    </div>
                </div>
                <div style="flex-shrink: 0;">
                    <span style="color: #e45e28; font-size: 1.2em;">→</span>
                </div>
            </div>
        </a>
    `;
}}

// 渲染文章列表
function renderPosts(posts) {{
    const container = document.getElementById('posts-container');
    container.innerHTML = posts.map(renderPostCard).join('');
    
    // 更新统计信息
    const datedCount = posts.filter(p => p.date).length;
    const undatedCount = posts.filter(p => !p.date).length;
    document.getElementById('stats-info').innerHTML = `
        共 <strong>${{posts.length}}</strong> 篇文章 | 
        已标注日期：<strong style="color: #e45e28;">${{datedCount}}</strong> | 
        待标注日期：<strong style="color: #999;">${{undatedCount}}</strong>
    `;
}}

// 过滤和排序文章
function filterAndSortPosts(category = 'all', searchTerm = '') {{
    let filtered = [...blogPosts];
    
    // 分类过滤
    if (category !== 'all') {{
        filtered = filtered.filter(post => post.category === category);
    }}
    
    // 搜索过滤
    if (searchTerm) {{
        const term = searchTerm.toLowerCase();
        filtered = filtered.filter(post => 
            post.title.toLowerCase().includes(term) || 
            post.category.toLowerCase().includes(term)
        );
    }}
    
    // 分离有日期和无日期的文章
    const datedPosts = filtered.filter(post => post.date);
    const undatedPosts = filtered.filter(post => !post.date);
    
    // 有日期的按时间倒序排序
    datedPosts.sort((a, b) => new Date(b.date) - new Date(a.date));
    
    // 无日期的随机排序
    const shuffledUndated = shuffleArray(undatedPosts);
    
    // 合并：有日期的在前，无日期的在后
    return [...datedPosts, ...shuffledUndated];
}}

// 初始化分类过滤器
function initCategoryFilters() {{
    const categories = [...new Set(blogPosts.map(post => post.category))].sort();
    const filterContainer = document.getElementById('category-filters');
    
    categories.forEach(category => {{
        const btn = document.createElement('button');
        btn.className = 'filter-btn';
        btn.dataset.category = category;
        btn.textContent = category;
        btn.style.cssText = 'padding: 8px 16px; border: none; border-radius: 20px; background: #f0f0f0; color: #666; cursor: pointer; font-size: 14px; transition: all 0.2s;';
        btn.onmouseover = function() {{
            if (!this.classList.contains('active')) {{
                this.style.background = '#e0e0e0';
            }}
        }};
        btn.onmouseout = function() {{
            if (!this.classList.contains('active')) {{
                this.style.background = '#f0f0f0';
            }}
        }};
        btn.onclick = function() {{
            document.querySelectorAll('.filter-btn').forEach(b => {{
                b.classList.remove('active');
                b.style.background = '#f0f0f0';
                b.style.color = '#666';
            }});
            this.classList.add('active');
            this.style.background = '#e45e28';
            this.style.color = 'white';
            
            const searchTerm = document.getElementById('search-input').value;
            const posts = filterAndSortPosts(this.dataset.category, searchTerm);
            renderPosts(posts);
        }};
        filterContainer.appendChild(btn);
    }});
}}

// 初始化搜索功能
function initSearch() {{
    const searchInput = document.getElementById('search-input');
    searchInput.addEventListener('input', (e) => {{
        const activeCategory = document.querySelector('.filter-btn.active').dataset.category;
        const posts = filterAndSortPosts(activeCategory, e.target.value);
        renderPosts(posts);
    }});
}}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {{
    initCategoryFilters();
    initSearch();
    
    // 初始渲染所有文章
    const posts = filterAndSortPosts('all', '');
    renderPosts(posts);
}});
</script>

<style>
/* 响应式设计 */
@media (max-width: 768px) {{
    #blog-posts {{
        padding: 10px !important;
    }}
    
    .post-card {{
        padding: 15px !important;
    }}
    
    #category-filters {{
        justify-content: center !important;
    }}
    
    .filter-btn {{
        font-size: 12px !important;
        padding: 6px 12px !important;
    }}
}}

/* 平滑滚动 */
html {{
    scroll-behavior: smooth;
}}

/* 卡片悬停效果增强 */
.post-card:hover h3 {{
    color: #e45e28 !important;
}}

/* 搜索框焦点效果 */
#search-input:focus {{
    border-color: #e45e28 !important;
    box-shadow: 0 0 0 3px rgba(228, 94, 40, 0.1) !important;
}}

/* 分类按钮动画 */
.filter-btn {{
    transition: all 0.2s ease !important;
}}

.filter-btn:active {{
    transform: scale(0.95) !important;
}}
</style>
'''
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(template)
    
    return len(posts), len(dated_posts), len(undated_posts)

def main():
    """主函数"""
    src_dir = Path('/workspace/src')
    summary_path = src_dir / 'SUMMARY.md'
    output_path = src_dir / 'blog-index.md'
    
    print("📖 正在解析 SUMMARY.md...")
    posts = parse_summary_md(summary_path)
    
    print(f"📝 找到 {len(posts)} 篇文章")
    
    print("✨ 正在生成 blog-index.md...")
    total, dated, undated = generate_blog_index(posts, output_path)
    
    print(f"✅ 生成成功！")
    print(f"   - 总文章数：{total}")
    print(f"   - 已标注日期：{dated}")
    print(f"   - 待标注日期：{undated}")
    print(f"\n💡 提示：")
    print(f"   - 在文件名前添加 YYYYMMDD- 前缀可自动识别日期（如：20260421-文章标题.md）")
    print(f"   - 每次修改 SUMMARY.md 后运行此脚本更新博客列表")

if __name__ == '__main__':
    main()
