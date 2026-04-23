# 📝 博客使用指南

## 概述

本项目基于 mdBook 构建，提供了一个用户友好的博客页面，支持以下功能：

- ✅ **时间倒序排序**：有日期的文章按发布时间倒序显示
- ✅ **随机排序**：没有日期的文章随机显示在列表底部
- ✅ **分类筛选**：支持按文章分类进行筛选
- ✅ **实时搜索**：支持按标题或分类搜索文章
- ✅ **响应式设计**：适配手机、平板和桌面设备
- ✅ **自动统计**：显示已标注和待标注日期的文章数量

## 快速开始

### 1. 添加新文章

#### 步骤 1：在 `src/` 目录下创建文章文件

```bash
# 推荐：在文件名前添加日期前缀（格式：YYYYMMDD-）
touch "src/Python基础库/20260425-我的新文章.md"

# 或者不添加日期（将随机显示在列表底部）
touch "src/Python基础库/我的新文章.md"
```

#### 步骤 2：在 `SUMMARY.md` 中添加文章链接

打开 `src/SUMMARY.md`，在对应的分类下添加：

```markdown
- [Python]()
    - [Python基础库]()
        - [我的新文章](Python基础库/我的新文章.md)
```

#### 步骤 3：更新博客索引页

运行生成脚本：

```bash
python3 generate_blog_index.py
```

### 2. 为文章添加日期

有两种方式为文章添加日期：

#### 方法一：修改文件名（推荐）

在文件名前添加 `YYYYMMDD-` 前缀：

```bash
# 原始文件名
mv "src/Python基础库/我的文章.md" "src/Python基础库/20260425-我的文章.md"
```

然后在 `SUMMARY.md` 中更新路径：

```markdown
- [我的文章](Python基础库/20260425-我的文章.md)
```

#### 方法二：后续手动维护

暂时不添加日期，文章会随机显示在列表底部，并标记为"待补充日期"。
后续可以随时通过修改文件名来添加日期。

### 3. 构建和预览

```bash
# 安装 mdBook（如果尚未安装）
# macOS
brew install mdbook

# Linux
cargo install mdbook

# 构建博客
mdbook build

# 本地预览
mdbook serve
```

访问 http://localhost:3000 查看博客。

## 目录结构

```
/workspace
├── book.toml                    # mdBook 配置文件
├── blog.css                     # 自定义样式
├── generate_blog_index.py       # 博客索引生成脚本
├── src/
│   ├── SUMMARY.md              # 书籍目录（也是博客文章索引）
│   ├── blog-index.md           # 博客文章列表页（自动生成）
│   ├── about-me.md             # 关于页面
│   └── [分类文件夹]/
│       └── [文章].md           # 博客文章
└── theme/
    └── index.hbs               # 自定义主题模板
```

## 文件命名规范

### 推荐格式

```
YYYYMMDD-文章标题.md
```

示例：
- `20260425-Python装饰器详解.md`
- `20260320-VibeCoding完全指南.md`

### 优点

1. **自动识别**：脚本会自动从文件名提取日期
2. **时间排序**：文章按时间倒序显示
3. **易于管理**：文件名即包含发布时间信息

## 分类管理

在 `SUMMARY.md` 中，分类通过层级结构表示：

```markdown
- [Python]()                          # 一级分类
    - [Python基础库]()                # 二级分类
        - [文章 1](路径/文章 1.md)
        - [文章 2](路径/文章 2.md)
    - [Python数据处理]()
        - [文章 3](路径/文章 3.md)
```

博客页面会自动提取这些分类，并生成筛选按钮。

## 博客页面功能

### 搜索功能

- 在搜索框输入关键词，实时过滤文章
- 支持搜索标题和分类
- 不区分大小写

### 分类筛选

- 点击分类按钮，只显示该分类的文章
- 点击"全部"按钮，显示所有文章
- 分类筛选和搜索可以同时使用

### 文章卡片

每篇文章显示：
- 📅 发布日期（如果有）
- ⏰ 相对时间描述（如"3 天前"）
- 📁 所属分类
- 🔗 点击卡片跳转到文章详情页

### 统计信息

页面底部显示：
- 总文章数
- 已标注日期的文章数
- 待标注日期的文章数

## 常见问题

### Q: 如何修改已有文章的日期？

A: 直接修改文件名即可：

```bash
mv "src/分类/旧文件名.md" "src/分类/20260425-新文件名.md"
```

然后更新 `SUMMARY.md` 中的路径，最后运行 `python3 generate_blog_index.py`。

### Q: 可以批量为文章添加日期吗？

A: 可以编写脚本批量重命名文件。例如：

```python
import os
from datetime import datetime

# 示例：为指定文件夹下的所有文章添加今天的日期
today = datetime.now().strftime('%Y%m%d')
folder = 'src/Python基础库'

for filename in os.listdir(folder):
    if filename.endswith('.md') and not filename[0].isdigit():
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, f'{today}-{filename}')
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {today}-{filename}')
```

### Q: 为什么有些文章分类显示为"Python/Python 基础库"？

A: 这是因为 `SUMMARY.md` 中的层级结构。如果希望简化分类名称，可以调整 `SUMMARY.md` 的结构，或者在生成脚本中修改分类处理逻辑。

### Q: 如何自定义博客页面的样式？

A: 可以修改以下文件：
- `blog.css`：全局样式
- `src/blog-index.md`：博客列表页的内联样式
- `theme/index.hbs`：页面模板

## 技术细节

### 生成脚本说明

`generate_blog_index.py` 脚本执行以下操作：

1. 解析 `SUMMARY.md` 文件
2. 提取所有文章链接和分类信息
3. 从文件名中提取日期（如果存在）
4. 分离有日期和无日期的文章
5. 有日期的按时间倒序排序
6. 无日期的随机打乱顺序
7. 生成包含所有数据的 `blog-index.md` 文件

### 数据持久化

文章数据存储在 `SUMMARY.md` 中，这是 mdBook 的标准格式。
`blog-index.md` 是自动生成的，不需要手动编辑。

### 浏览器兼容性

博客页面使用现代 JavaScript 特性，支持：
- Chrome 60+
- Firefox 55+
- Safari 11+
- Edge 79+

## 贡献与反馈

欢迎提交 Issue 和 Pull Request 来改进这个博客系统！

---

**祝写作愉快！** 🎉
