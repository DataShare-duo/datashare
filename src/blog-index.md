# 博客文章列表

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
    {title: "告别焦虑，借助AI深化技术学习", path: "随笔/20260421-告别焦虑，借助AI深化技术学习.html", date: "2026-04-21", category: "随笔"},
    {title: "Python 与 Rust 类型参数对比：从 TypeVar 到泛型 \<T\>", path: "Python基础库/20260410-Python与Rust类型参数对比：从TypeVar到泛型T.html", date: "2026-04-10", category: "Python/Python基础库"},
    {title: "Vibe Coding初体验：用AI辅助开发一款心情打卡小程序", path: "大模型相关/20260326-Vibe_Coding初体验：用AI辅助开发一款心情打卡小程序.html", date: "2026-03-26", category: "大模型相关"},
    {title: "VibeCoding完全指南：2026年，我们用“感觉”写代码", path: "大模型相关/20260320-VibeCoding完全指南：2026年，我们用“感觉”写代码.html", date: "2026-03-20", category: "大模型相关"},
    {title: "OpenClaw使用体验", path: "大模型相关/20260313-OpenClaw使用体验.html", date: "2026-03-13", category: "大模型相关"},
    {title: "现代Python全栈分布式数据计算：Ray、Daft与Lance的探索", path: "Python数据处理/20260228-现代Python全栈分布式数据计算：Ray、Daft与Lance的探索.html", date: "2026-02-28", category: "Python/Python数据处理"},
    {title: "Python-装饰器的灵活实现：带参数与不带参数", path: "Python基础库/20260204-Python-装饰器的灵活实现：带参数与不带参数.html", date: "2026-02-04", category: "Python/Python基础库"},
    {title: "利用熵值法确定指标权重---原理及Python实现", path: "数据分析与挖掘/利用熵值法确定指标权重---原理及Python实现.html", date: null, category: "Python/数据分析与挖掘"},
    {title: "利用Python画出《人民日报》各国疫情图——南丁格尔玫瑰图", path: "数据可视化/利用Python画出《人民日报》各国疫情图——南丁格尔玫瑰图.html", date: null, category: "Python/数据可视化"},
    {title: "Python-3-14-无GIL解释器性能测试：释放多核CPU的并行潜力", path: "Python基础库/Python-3-14-无GIL解释器性能测试：释放多核CPU的并行潜力.html", date: null, category: "Python/Python基础库"},
    {title: "Python用xlwings库处理Excel", path: "Python数据处理/Python用xlwings库处理Excel.html", date: null, category: "Python/Python数据处理"},
    {title: "数据分析师常用的-Linux-命令总结", path: "Linux/数据分析师常用的-Linux-命令总结.html", date: null, category: "Linux"},
    {title: "Python-两个字典如何实现相加？（相同的键，值相加）", path: "Python数据处理/Python-两个字典如何实现相加？（相同的键，值相加）.html", date: null, category: "Python/Python数据处理"},
    {title: "Python数据预处理中One-Hot编码的方法", path: "Python数据处理/Python数据预处理中One-Hot编码的方法.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-利用协程整合IPTV直播源", path: "数据采集/Python-利用协程整合IPTV直播源.html", date: null, category: "Python/数据采集"},
    {title: "Python中的Lambda匿名函数", path: "Python数据处理/Python中的Lambda匿名函数.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-jupyter-常用语句汇总", path: "Python数据处理/Python-jupyter-常用语句汇总.html", date: null, category: "Python/Python数据处理"},
    {title: "Hive-中把一行记录拆分为多行记录", path: "Hive/Hive-中把一行记录拆分为多行记录.html", date: null, category: "Hive"},
    {title: "Python-利用聚类算法对图片进行颜色压缩", path: "Python图像处理/Python-利用聚类算法对图片进行颜色压缩.html", date: null, category: "Python/Python图像处理"},
    {title: "Python-基于协程的端口扫描工具", path: "Python基础库/Python-基于协程的端口扫描工具.html", date: null, category: "Python/Python基础库"},
    {title: "管理的精髓", path: "随笔/管理的精髓.html", date: null, category: "随笔"},
    {title: "Pythonner还在为了练习Numpy而没有真实数据而烦恼吗？", path: "Python数据处理/Pythonner还在为了练习Numpy而没有真实数据而烦恼吗？.html", date: null, category: "Python/Python数据处理"},
    {title: "pandas-错误提醒：FutureWarning--elementwise-comparison-failed;", path: "Python数据处理/pandas-错误提醒：FutureWarning--elementwise-comparison-failed;.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-一个在本地给图片添加水印的小工具", path: "Python图像处理/Python-一个在本地给图片添加水印的小工具.html", date: null, category: "Python/Python图像处理"},
    {title: "Python pandas-数据无法正常分列", path: "Python数据处理/Python-pandas-数据无法正常分列.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-标准库heapq，堆数据结构操作详解", path: "Python基础库/Python-标准库heapq，堆数据结构操作详解.html", date: null, category: "Python/Python基础库"},
    {title: "Python-扑克牌发牌游戏", path: "Python基础库/Python-扑克牌发牌游戏.html", date: null, category: "Python/Python基础库"},
    {title: "NumPy论文都已经登上了Nature，Pythoneer会用了吗？", path: "Python基础库/NumPy论文都已经登上了Nature，Pythoneer会用了吗？.html", date: null, category: "Python/Python基础库"},
    {title: "Python基于opencv-“三维”旋转图片，解决日常小问题", path: "Python图像处理/Python基于opencv-“三维”旋转图片，解决日常小问题.html", date: null, category: "Python/Python图像处理"},
    {title: "Hive中各种日期格式转换方法总结", path: "Hive/Hive中各种日期格式转换方法总结.html", date: null, category: "Hive"},
    {title: "Python-polars学习-11-用户自定义函数", path: "polars-学习/Python-polars学习-11-用户自定义函数.html", date: null, category: "Python/polars-学习"},
    {title: "Python-pandas在读取csv文件时（linux与windows之间传输），数据行数不一致的问题", path: "Python数据处理/Python-pandas在读取csv文件时（linux与windows之间传输），数据行数不一致的问题.html", date: null, category: "Python/Python数据处理"},
    {title: "Python常用语句汇总", path: "Python数据处理/Python常用语句汇总.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-基于ssh连接远程Mysql数据库", path: "Python基础库/Python-基于ssh连接远程Mysql数据库.html", date: null, category: "Python/Python基础库"},
    {title: "Python内置的-os-模块常用函数、方法", path: "Python基础库/Python内置的-os-模块常用函数、方法.html", date: null, category: "Python/Python基础库"},
    {title: "Python polars学习 10-时间序列类型", path: "polars-学习/Python-polars学习-10-时间序列类型.html", date: null, category: "Python/polars-学习"},
    {title: "Hive---HQL支持的2种查询语句风格，你喜欢哪一种？", path: "Hive/Hive---HQL支持的2种查询语句风格，你喜欢哪一种？.html", date: null, category: "Hive"},
    {title: "在Linux服务器上部署Jupyter-notebook", path: "Linux/在Linux服务器上部署Jupyter-notebook.html", date: null, category: "Linux"},
    {title: "不同岗位的数据分析人员，可能使用不同的分析方法", path: "数据分析与挖掘/不同岗位的数据分析人员，可能使用不同的分析方法.html", date: null, category: "Python/数据分析与挖掘"},
    {title: "Excel中的标准差stdev-S和stdev-P区别", path: "EXCEL数据处理-VBA/Excel中的标准差stdev-S和stdev-P区别.html", date: null, category: "EXCEL数据处理-VBA"},
    {title: "Python-利用aiohttp异步流式下载文件", path: "Python数据处理/Python-利用aiohttp异步流式下载文件.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-基于hdfs路径统计hive表存储信息", path: "Python数据处理/Python-基于hdfs路径统计hive表存储信息.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-利用Matplotlib制作初中时圆规画的图", path: "数据可视化/Python-利用Matplotlib制作初中时圆规画的图.html", date: null, category: "Python/数据可视化"},
    {title: "Python-内建模块-bisect，数组二分查找算法", path: "Python基础库/Python-内建模块-bisect，数组二分查找算法.html", date: null, category: "Python/Python基础库"},
    {title: "机器学习之sklearn-feature_selection-chi2基于卡方，特征筛选详解", path: "数据分析与挖掘/机器学习之sklearn-feature_selection-chi2基于卡方，特征筛选详解.html", date: null, category: "Python/数据分析与挖掘"},
    {title: "Python-基于OpenList接口下载夸克网盘资源", path: "Python数据处理/Python-基于OpenList接口下载夸克网盘资源.html", date: null, category: "Python/Python数据处理"},
    {title: "Python polars学习 06_Lazy-Eager-API", path: "polars-学习/Python_polars学习-06_Lazy-Eager-API.html", date: null, category: "Python/polars-学习"},
    {title: "利用Python计算两个地理位置之间的中点", path: "Python数据处理/利用Python计算两个地理位置之间的中点.html", date: null, category: "Python/Python数据处理"},
    {title: "Python文件打包成exe可执行程序", path: "Python基础库/Python文件打包成exe可执行程序.html", date: null, category: "Python/Python基础库"},
    {title: "Python-pandas遍历行数据的2种方法", path: "Python数据处理/Python-pandas遍历行数据的2种方法.html", date: null, category: "Python/Python数据处理"},
    {title: "Linux之NTFS、FAT32、exFAT-各种格式硬盘挂载整理", path: "Linux/Linux之NTFS、FAT32、exFAT-各种格式硬盘挂载整理.html", date: null, category: "Linux"},
    {title: "Python利用partial偏函数，生成不同的聚合函数", path: "Python基础库/Python利用partial偏函数，生成不同的聚合函数.html", date: null, category: "Python/Python基础库"},
    {title: "Hive-数据聚合成键值对时，根据值大小进行排序", path: "Hive/Hive-数据聚合成键值对时，根据值大小进行排序.html", date: null, category: "Hive"},
    {title: "Python-迈向强类型化的优雅转变", path: "Python基础库/Python-迈向强类型化的优雅转变.html", date: null, category: "Python/Python基础库"},
    {title: "Python-多线程，真实使用代码", path: "Python数据处理/Python-多线程，真实使用代码.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-单实例模式详解", path: "Python基础库/Python-单实例模式详解.html", date: null, category: "Python/Python基础库"},
    {title: "Python polars学习 05_包含的数据结构", path: "polars-学习/Python_polars学习-05_包含的数据结构.html", date: null, category: "Python/polars-学习"},
    {title: "hadoop-常用命令总结", path: "Hive/hadoop-常用命令总结.html", date: null, category: "Hive"},
    {title: "Python-使用sklearn计算余弦相似度", path: "数学知识/Python-使用sklearn计算余弦相似度.html", date: null, category: "Python/数学知识"},
    {title: "Python-除了结巴分词，还有什么好用的中文分词工具？", path: "NLP/Python-除了结巴分词，还有什么好用的中文分词工具？.html", date: null, category: "Python/NLP"},
    {title: "Python-collections详解：解锁高效数据结构", path: "Python基础库/Python-collections详解：解锁高效数据结构.html", date: null, category: "Python/Python基础库"},
    {title: "罗兰贝格图--Python等高线图（平滑处理）", path: "数据可视化/罗兰贝格图--Python等高线图（平滑处理）.html", date: null, category: "Python/数据可视化"},
    {title: "Clickhouse中创建生成日期序列自定义函数", path: "Clickhouse/Clickhouse中创建生成日期序列自定义函数.html", date: null, category: "Clickhouse"},
    {title: "Python-字典已经是有序的，你知道吗？", path: "Python基础库/Python-字典已经是有序的，你知道吗？.html", date: null, category: "Python/Python基础库"},
    {title: "传统统计分析在Python中的使用", path: "数据分析与挖掘/传统统计分析在Python中的使用.html", date: null, category: "Python/数据分析与挖掘"},
    {title: "Python-字符串格式化方法总结", path: "Python数据处理/Python-字符串格式化方法总结.html", date: null, category: "Python/Python数据处理"},
    {title: "Python polars学习 09_数据框关联与拼接", path: "polars-学习/Python_polars学习-09_数据框关联与拼接.html", date: null, category: "Python/polars-学习"},
    {title: "数据去重-----VBA字典法", path: "EXCEL数据处理-VBA/数据去重-----VBA字典法.html", date: null, category: "EXCEL数据处理-VBA"},
    {title: "Python-math模块详解", path: "Python基础库/Python-math模块详解.html", date: null, category: "Python/Python基础库"},
    {title: "Python pandas-里面的数据类型坑，astype要慎用", path: "Python数据处理/Python-pandas-里面的数据类型坑，astype要慎用.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-pandas数据分列，分割符号&固定宽度", path: "Python数据处理/Python-pandas数据分列，分割符号&固定宽度.html", date: null, category: "Python/Python数据处理"},
    {title: "Python数据处理中-pd-concat-与-pd-merge-区别", path: "Python数据处理/Python数据处理中-pd-concat-与-pd-merge-区别.html", date: null, category: "Python/Python数据处理"},
    {title: "Python pandas.2.0-初探", path: "Python数据处理/Python-pandas-2-0-初探.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-利用-uv-“一键”-快速部署服务", path: "Python基础库/Python-利用-uv-“一键”-快速部署服务.html", date: null, category: "Python/Python基础库"},
    {title: "像excel透视表一样使用pandas透视函数", path: "Python数据处理/像excel透视表一样使用pandas透视函数.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-利用Pandas把数据直接导入Mysql", path: "Python数据处理/Python-利用Pandas把数据直接导入Mysql.html", date: null, category: "Python/Python数据处理"},
    {title: "Python中一个构建-web-页面的神奇库-streamlit", path: "Web/Python中一个构建-web-页面的神奇库-streamlit.html", date: null, category: "Python/数学知识/Web"},
    {title: "Hive-中的各种常用set设置", path: "Hive/Hive-中的各种常用set设置.html", date: null, category: "Hive"},
    {title: "Clickhouse-基础使用教程", path: "Clickhouse/Clickhouse-基础使用教程.html", date: null, category: "Clickhouse"},
    {title: "Python polars学习 02_上下文与表达式", path: "polars-学习/Python_polars学习-02_上下文与表达式.html", date: null, category: "Python/polars-学习"},
    {title: "Python-小知识系列（一）", path: "Python数据处理/Python-小知识系列（一）.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-如何确定K-Means聚类的簇数", path: "数据分析与挖掘/Python-如何确定K-Means聚类的簇数.html", date: null, category: "Python/数据分析与挖掘"},
    {title: "Python-中一个好用的股票开源库akshare", path: "数据采集/Python-中一个好用的股票开源库akshare.html", date: null, category: "Python/数据采集"},
    {title: "吴军老师的《计算之魂》部分重点摘要", path: "随笔/吴军老师的《计算之魂》部分重点摘要.html", date: null, category: "随笔"},
    {title: "基于DeepSeek，构建个人本地RAG知识库", path: "大模型相关/基于DeepSeek，构建个人本地RAG知识库.html", date: null, category: "大模型相关"},
    {title: "Python-处理Excel文件为了通用原则，建议用openpyxl库", path: "Python数据处理/Python-处理Excel文件为了通用原则，建议用openpyxl库.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-基于Matplotlib制作动态图", path: "数据可视化/Python-基于Matplotlib制作动态图.html", date: null, category: "Python/数据可视化"},
    {title: "Python函数参数：列表作为默认值，一个隐藏的陷阱！", path: "Python基础库/Python函数参数：列表作为默认值，一个隐藏的陷阱！.html", date: null, category: "Python/Python基础库"},
    {title: "Python通过修改系统注册表，强制设置Excel宏信任级别", path: "Python数据处理/Python通过修改系统注册表，强制设置Excel宏信任级别.html", date: null, category: "Python/Python数据处理"},
    {title: "Python polars学习 01_读取与写入文件", path: "polars-学习/Python_polars学习-01_读取与写入文件.html", date: null, category: "Python/polars-学习"},
    {title: "Python-利用数据分布直方图来确定合适的阈值", path: "数据分析与挖掘/Python-利用数据分布直方图来确定合适的阈值.html", date: null, category: "Python/数据分析与挖掘"},
    {title: "Python-pandas数据计数函数value_counts", path: "Python数据处理/Python-pandas数据计数函数value_counts.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-在指定文件夹安装三方库，并进行加载使用", path: "Python基础库/Python-在指定文件夹安装三方库，并进行加载使用.html", date: null, category: "Python/Python基础库"},
    {title: "Python-常用的加解密算法实例应用", path: "Python数据处理/Python-常用的加解密算法实例应用.html", date: null, category: "Python/Python数据处理"},
    {title: "利用Python+PyEcharts画出《人民日报》各国疫情图", path: "数据可视化/利用Python+PyEcharts画出《人民日报》各国疫情图.html", date: null, category: "Python/数据可视化"},
    {title: "Clickhouse-读取存储在hdfs的hive表数据", path: "Clickhouse/Clickhouse-读取存储在hdfs的hive表数据.html", date: null, category: "Clickhouse"},
    {title: "Python利用枚举法，解决一道面试算法题", path: "数学知识/Python利用枚举法，解决一道面试算法题.html", date: null, category: "Python/数学知识"},
    {title: "工欲善其事必先利其器", path: "随笔/工欲善其事必先利其器.html", date: null, category: "随笔"},
    {title: "《Python-编程从新手到高手》知识点", path: "Python基础库/《Python-编程从新手到高手》知识点.html", date: null, category: "Python/Python基础库"},
    {title: "从互联网+，到DeepSeek+，新一轮的技术变革", path: "随笔/从互联网+，到DeepSeek+，新一轮的技术变革.html", date: null, category: "随笔"},
    {title: "Hive中对相邻访问时间进行归并分组", path: "Hive/Hive中对相邻访问时间进行归并分组.html", date: null, category: "Hive"},
    {title: "Python-基于pyhive库操作hive", path: "Python数据处理/Python-基于pyhive库操作hive.html", date: null, category: "Python/Python数据处理"},
    {title: "对比Excel，利用pandas进行数据分析各种用法", path: "Python数据处理/对比Excel，利用pandas进行数据分析各种用法.html", date: null, category: "Python/Python数据处理"},
    {title: "历史双色球数据分析---python", path: "Python数据处理/历史双色球数据分析---python.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-人脸检测方法总结", path: "Python图像处理/Python-人脸检测方法总结.html", date: null, category: "Python/Python图像处理"},
    {title: "Python---opencv一次读取视频里面多张视频帧", path: "Python图像处理/Python---opencv一次读取视频里面多张视频帧.html", date: null, category: "Python/Python图像处理"},
    {title: "Numpy中的shuffle和permutation区别", path: "Python数据处理/Numpy中的shuffle和permutation区别.html", date: null, category: "Python/Python数据处理"},
    {title: "自然语言处理（NLP）-Bert与Lstm结合", path: "NLP/自然语言处理（NLP）-Bert与Lstm结合.html", date: null, category: "Python/NLP"},
    {title: "利用Python对图片进行马赛克处理", path: "Python图像处理/利用Python对图片进行马赛克处理.html", date: null, category: "Python/Python图像处理"},
    {title: "Python-基于pyecharts自定义经纬度热力图可视化", path: "数据可视化/Python-基于pyecharts自定义经纬度热力图可视化.html", date: null, category: "Python/数据可视化"},
    {title: "Python-基于plotly库快速画旭日图", path: "数据可视化/Python-基于plotly库快速画旭日图.html", date: null, category: "Python/数据可视化"},
    {title: "利用Python实现二维码自由", path: "Python图像处理/利用Python实现二维码自由.html", date: null, category: "Python/Python图像处理"},
    {title: "Python-基于plotly库快速绘制时间线图", path: "数据可视化/Python-基于plotly库快速绘制时间线图.html", date: null, category: "Python/数据可视化"},
    {title: "Python polars学习 08_分类数据处理", path: "polars-学习/Python_polars学习-08_分类数据处理.html", date: null, category: "Python/polars-学习"},
    {title: "Python-标准库之pathlib，路径操作", path: "Python基础库/Python-标准库之pathlib，路径操作.html", date: null, category: "Python/Python基础库"},
    {title: "利用Python模拟Excel数据透视表具有“值显示方式”功能", path: "Python数据处理/利用Python模拟Excel数据透视表具有“值显示方式”功能.html", date: null, category: "Python/Python数据处理"},
    {title: "Python调用apiKey试玩ChatGPT", path: "NLP/Python调用apiKey试玩ChatGPT.html", date: null, category: "Python/NLP"},
    {title: "Hive中的常用函数", path: "Hive/Hive中的常用函数.html", date: null, category: "Hive"},
    {title: "Python pandas中重排列与列重名", path: "Python数据处理/Python-pandas中重排列与列重名.html", date: null, category: "Python/Python数据处理"},
    {title: "Python polars学习 03_数据类型转换", path: "polars-学习/Python_polars学习-03_数据类型转换.html", date: null, category: "Python/polars-学习"},
    {title: "分类问题中Sigmoid-与-Softmax-区别", path: "数学知识/分类问题中Sigmoid-与-Softmax-区别.html", date: null, category: "Python/数学知识"},
    {title: "机器学习-决策树原理-Python", path: "数据分析与挖掘/机器学习-决策树原理-Python.html", date: null, category: "Python/数据分析与挖掘"},
    {title: "Python-利用4行代码实现图片灰度化", path: "Python图像处理/Python-利用4行代码实现图片灰度化.html", date: null, category: "Python/Python图像处理"},
    {title: "机器学习算法总结", path: "数据分析与挖掘/机器学习算法总结.html", date: null, category: "Python/数据分析与挖掘"},
    {title: "Python-新晋包项目工具uv的简单尝试", path: "Python基础库/Python-新晋包项目工具uv的简单尝试.html", date: null, category: "Python/Python基础库"},
    {title: "Python-函数参数类型与使用规则详解", path: "Python基础库/Python-函数参数类型与使用规则详解.html", date: null, category: "Python/Python基础库"},
    {title: "Python-项目管理新思路：用-uv-Workspace-共享虚拟环境，省时省空间！", path: "Python基础库/Python-项目管理新思路：用-uv-Workspace-共享虚拟环境，省时省空间！.html", date: null, category: "Python/Python基础库"},
    {title: "Python-记录re正则模块，方便后期查找使用", path: "Python基础库/Python-记录re正则模块，方便后期查找使用.html", date: null, category: "Python/Python基础库"},
    {title: "让ChatGPT回答闰年的计算逻辑", path: "数学知识/让ChatGPT回答闰年的计算逻辑.html", date: null, category: "Python/数学知识"},
    {title: "利用Python对图片进行模糊化处理", path: "Python图像处理/利用Python对图片进行模糊化处理.html", date: null, category: "Python/Python图像处理"},
    {title: "Python-中一个好用的地址解析工具cpca（chinese_province_city_area_mapper）", path: "Python基础库/Python-中一个好用的地址解析工具cpca（chinese_province_city_area_mapper）.html", date: null, category: "Python/Python基础库"},
    {title: "Python-基于datetime库的日期时间数据处理", path: "Python数据处理/Python-基于datetime库的日期时间数据处理.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-微信头像添加国旗", path: "Python图像处理/Python-微信头像添加国旗.html", date: null, category: "Python/Python图像处理"},
    {title: "利用Python枚举所有的排列情况", path: "数学知识/利用Python枚举所有的排列情况.html", date: null, category: "Python/数学知识"},
    {title: "对csv文件，又get了新的认知", path: "Python数据处理/对csv文件，又get了新的认知.html", date: null, category: "Python/Python数据处理"},
    {title: "Python pandas.str.replace-不起作用", path: "Python数据处理/Python-pandas-str-replace-不起作用.html", date: null, category: "Python/Python数据处理"},
    {title: "Python 利用矢量化，计算2个经纬度之间的距离", path: "Python数据处理/Python-利用矢量化，计算2个经纬度之间的距离.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-利用协程采集想看的《人世间》下载地址", path: "数据采集/Python-利用协程采集想看的《人世间》下载地址.html", date: null, category: "Python/数据采集"},
    {title: "Python polars学习 07_缺失值", path: "polars-学习/Python_polars学习-07_缺失值.html", date: null, category: "Python/polars-学习"},
    {title: "利用Python生成手绘效果的图片", path: "Python图像处理/利用Python生成手绘效果的图片.html", date: null, category: "Python/Python图像处理"},
    {title: "Linux-（Centos-7）中-Anaconda环境管理，安装不同的版本Python包", path: "Linux/Linux-（Centos-7）中-Anaconda环境管理，安装不同的版本Python包.html", date: null, category: "Linux"},
    {title: "Matplotlib-自定义函数实现左边柱形图，右边饼图", path: "数据可视化/Matplotlib-自定义函数实现左边柱形图，右边饼图.html", date: null, category: "Python/数据可视化"},
    {title: "尝试-gemini-cli，在本地开发俄罗斯方块", path: "大模型相关/尝试-gemini-cli，在本地开发俄罗斯方块.html", date: null, category: "大模型相关"},
    {title: "Python-把csv文件转换为excel文件", path: "Python数据处理/Python-把csv文件转换为excel文件.html", date: null, category: "Python/Python数据处理"},
    {title: "SecureCRT利用Python脚本自动登陆服务器，自动验证Google-Authenticator动态验证码", path: "Linux/SecureCRT利用Python脚本自动登陆服务器，自动验证Google-Authenticator动态验证码.html", date: null, category: "Linux"},
    {title: "Python-利用pandas对数据进行特定排序", path: "Python数据处理/Python-利用pandas对数据进行特定排序.html", date: null, category: "Python/Python数据处理"},
    {title: "Rust-是否会重写-Python-解释器与有关的库，替代-C-语言地位？", path: "Python基础库/Rust-是否会重写-Python-解释器与有关的库，替代-C-语言地位？.html", date: null, category: "Python/Python基础库"},
    {title: "Python加载txt数据乱码问题升级版解决方法", path: "Python数据处理/Python加载txt数据乱码问题升级版解决方法.html", date: null, category: "Python/Python数据处理"},
    {title: "对csv文件，又get了新的认知（二）", path: "Python数据处理/对csv文件，又get了新的认知（二）.html", date: null, category: "Python/Python数据处理"},
    {title: "Python--Numpy中的范数", path: "Python数据处理/Python--Numpy中的范数.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-2个好用的装饰器函数", path: "Python基础库/Python-2个好用的装饰器函数.html", date: null, category: "Python/Python基础库"},
    {title: "Python pandas-数据筛选与赋值升级版详解", path: "Python数据处理/Python-pandas-数据筛选与赋值升级版详解.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-Pandas导出Excel时保留URL为纯文本的完美方案", path: "Python数据处理/Python-Pandas导出Excel时保留URL为纯文本的完美方案.html", date: null, category: "Python/Python数据处理"},
    {title: "利用Python-自己动手制作动漫效果图片", path: "Python图像处理/利用Python-自己动手制作动漫效果图片.html", date: null, category: "Python/Python图像处理"},
    {title: "Pandas数据处理误区要知其然知其所以然", path: "Python数据处理/Pandas数据处理误区要知其然知其所以然.html", date: null, category: "Python/Python数据处理"},
    {title: "Python-标准库之pathlib（二），路径操作", path: "Python基础库/Python-标准库之pathlib（二），路径操作.html", date: null, category: "Python/Python基础库"},
    {title: "《精益数据分析》读书分享-----增长引擎说", path: "数据分析与挖掘/《精益数据分析》读书分享-----增长引擎说.html", date: null, category: "Python/数据分析与挖掘"},
    {title: "Python polars学习 04_字符串数据处理", path: "polars-学习/Python_polars学习-04_字符串数据处理.html", date: null, category: "Python/polars-学习"}
];

// 随机打乱无日期文章的顺序
function shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
}

// 格式化日期显示
function formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// 获取相对时间描述
function getRelativeTime(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    const now = new Date();
    const diffTime = now - date;
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) return '今天';
    if (diffDays === 1) return '昨天';
    if (diffDays < 7) return `${diffDays}天前`;
    if (diffDays < 30) return `${Math.floor(diffDays / 7)}周前`;
    if (diffDays < 365) return `${Math.floor(diffDays / 30)}月前`;
    return `${Math.floor(diffDays / 365)}年前`;
}

// 渲染文章卡片
function renderPostCard(post) {
    const dateDisplay = post.date ? 
        `<span class="post-date" style="color: #e45e28; font-size: 0.85em; font-weight: 600;">📅 ${formatDate(post.date)}</span>` :
        `<span class="post-date" style="color: #999; font-size: 0.85em;">📅 待补充日期</span>`;
    
    const relativeTime = post.date ? 
        `<span style="color: #999; font-size: 0.8em; margin-left: 10px;">(${getRelativeTime(post.date)})</span>` : '';
    
    return `
        <a href="${post.path}" class="post-card" style="
            display: block;
            padding: 20px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            text-decoration: none;
            color: inherit;
            transition: all 0.3s ease;
            border-left: 4px solid ${post.date ? '#e45e28' : '#ccc'};
        " onmouseover="this.style.transform='translateX(5px)'; this.style.boxShadow='0 4px 16px rgba(0,0,0,0.12)'" 
           onmouseout="this.style.transform='translateX(0)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.08)'">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                <div style="flex: 1; min-width: 0;">
                    <h3 style="margin: 0 0 8px 0; font-size: 1.1em; color: #333; line-height: 1.4;">${post.title}</h3>
                    <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                        ${dateDisplay}${relativeTime}
                        <span class="post-category" style="
                            background: ${post.date ? '#fff3e0' : '#f5f5f5'}; 
                            color: ${post.date ? '#e45e28' : '#999'}; 
                            padding: 3px 10px; 
                            border-radius: 12px; 
                            font-size: 0.8em;
                            font-weight: 500;
                        ">📁 ${post.category}</span>
                    </div>
                </div>
                <div style="flex-shrink: 0;">
                    <span style="color: #e45e28; font-size: 1.2em;">→</span>
                </div>
            </div>
        </a>
    `;
}

// 渲染文章列表
function renderPosts(posts) {
    const container = document.getElementById('posts-container');
    container.innerHTML = posts.map(renderPostCard).join('');
    
    // 更新统计信息
    const datedCount = posts.filter(p => p.date).length;
    const undatedCount = posts.filter(p => !p.date).length;
    document.getElementById('stats-info').innerHTML = `
        共 <strong>${posts.length}</strong> 篇文章 | 
        已标注日期：<strong style="color: #e45e28;">${datedCount}</strong> | 
        待标注日期：<strong style="color: #999;">${undatedCount}</strong>
    `;
}

// 过滤和排序文章
function filterAndSortPosts(category = 'all', searchTerm = '') {
    let filtered = [...blogPosts];
    
    // 分类过滤
    if (category !== 'all') {
        filtered = filtered.filter(post => post.category === category);
    }
    
    // 搜索过滤
    if (searchTerm) {
        const term = searchTerm.toLowerCase();
        filtered = filtered.filter(post => 
            post.title.toLowerCase().includes(term) || 
            post.category.toLowerCase().includes(term)
        );
    }
    
    // 分离有日期和无日期的文章
    const datedPosts = filtered.filter(post => post.date);
    const undatedPosts = filtered.filter(post => !post.date);
    
    // 有日期的按时间倒序排序
    datedPosts.sort((a, b) => new Date(b.date) - new Date(a.date));
    
    // 无日期的随机排序
    const shuffledUndated = shuffleArray(undatedPosts);
    
    // 合并：有日期的在前，无日期的在后
    return [...datedPosts, ...shuffledUndated];
}

// 初始化分类过滤器
function initCategoryFilters() {
    const categories = [...new Set(blogPosts.map(post => post.category))].sort();
    const filterContainer = document.getElementById('category-filters');
    
    categories.forEach(category => {
        const btn = document.createElement('button');
        btn.className = 'filter-btn';
        btn.dataset.category = category;
        btn.textContent = category;
        btn.style.cssText = 'padding: 8px 16px; border: none; border-radius: 20px; background: #f0f0f0; color: #666; cursor: pointer; font-size: 14px; transition: all 0.2s;';
        btn.onmouseover = function() {
            if (!this.classList.contains('active')) {
                this.style.background = '#e0e0e0';
            }
        };
        btn.onmouseout = function() {
            if (!this.classList.contains('active')) {
                this.style.background = '#f0f0f0';
            }
        };
        btn.onclick = function() {
            document.querySelectorAll('.filter-btn').forEach(b => {
                b.classList.remove('active');
                b.style.background = '#f0f0f0';
                b.style.color = '#666';
            });
            this.classList.add('active');
            this.style.background = '#e45e28';
            this.style.color = 'white';
            
            const searchTerm = document.getElementById('search-input').value;
            const posts = filterAndSortPosts(this.dataset.category, searchTerm);
            renderPosts(posts);
        };
        filterContainer.appendChild(btn);
    });
}

// 初始化搜索功能
function initSearch() {
    const searchInput = document.getElementById('search-input');
    searchInput.addEventListener('input', (e) => {
        const activeCategory = document.querySelector('.filter-btn.active').dataset.category;
        const posts = filterAndSortPosts(activeCategory, e.target.value);
        renderPosts(posts);
    });
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    initCategoryFilters();
    initSearch();
    
    // 初始渲染所有文章
    const posts = filterAndSortPosts('all', '');
    renderPosts(posts);
});
</script>

<style>
/* 响应式设计 */
@media (max-width: 768px) {
    #blog-posts {
        padding: 10px !important;
    }
    
    .post-card {
        padding: 15px !important;
    }
    
    #category-filters {
        justify-content: center !important;
    }
    
    .filter-btn {
        font-size: 12px !important;
        padding: 6px 12px !important;
    }
}

/* 平滑滚动 */
html {
    scroll-behavior: smooth;
}

/* 卡片悬停效果增强 */
.post-card:hover h3 {
    color: #e45e28 !important;
}

/* 搜索框焦点效果 */
#search-input:focus {
    border-color: #e45e28 !important;
    box-shadow: 0 0 0 3px rgba(228, 94, 40, 0.1) !important;
}

/* 分类按钮动画 */
.filter-btn {
    transition: all 0.2s ease !important;
}

.filter-btn:active {
    transform: scale(0.95) !important;
}
</style>
