# 背景
在对文本进行处理分析时，大家第一印象就是对句子进行分词，统计词频，看哪些词语出现的词频较高，重点关注这些高频词即可，文章可能就是围绕着这些词展开的。中文的分词工具，大家耳熟能详的可能就是结巴分词，但是结巴分词最近也没有怎么更新，随着技术的不断迭代有一些更优秀的分词工具诞生，比如：LAC（百度）、THULAC（清华大学）、LTP（哈工大）、FoolNLTK等

这里主要介绍一下百度的LAC，现在已更新到v2.1，GitHub地址：https://github.com/baidu/lac，使用起来速度与效果还可以，足以应对简单的分词任务

# LAC介绍
>LAC全称 Lexical Analysis of Chinese，是百度自然语言处理部研发的一款联合的词法分析工具，实现中文分词、词性标注、专名识别等功能。该工具具有以下特点与优势：
>- **效果好**：通过深度学习模型联合学习分词、词性标注、专名识别任务，词语重要性，整体效果F1值超过0.91，词性标注F1值超过0.94，专名识别F1值超过0.85，效果业内领先。
>- **效率高**：精简模型参数，结合Paddle预测库的性能优化，CPU单线程性能达800QPS，效率业内领先。
>- **可定制**：实现简单可控的干预机制，精准匹配用户词典对模型进行干预。词典支持长片段形式，使得干预更为精准。
>- **调用便捷**：支持一键安装，同时提供了Python、Java和C++调用接口与调用示例，实现快速调用和集成。
>- **支持移动端**: 定制超轻量级模型，体积仅为2M，主流千元手机单线程性能达200QPS，满足大多数移动端应用的需求，同等体积量级效果业内领先。

功能看着很强大，但是这里只用到中文分词功能，下面介绍一下使用的demo，
通过 `pip install lac` 进行安装即可

# 使用教程
**直接使用lac分词**
加载`LAC `后，通过其自带的模型进行分词，结果为一个列表
```python
from LAC import LAC

# 装载分词模型
lac = LAC(mode='seg')

text='我是一名北漂的打工人、干饭人'
lac.run(text)

text_list=['我是一名北漂的打工人、干饭人','5月15日，航天科研人员在北京航天飞行控制中心指挥大厅庆祝我国首次火星探测任务着陆火星成功']
lac.run(text_list)
```
![直接使用lac分词](https://upload-images.jianshu.io/upload_images/6641583-70eb2250ac02085d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)
**加载自定义字典**
从上面可以看出“打工人”可以正确分词，但是“干饭人”不能正确的切分，可以通过加载自定义字典来进行处理这种情况
![自定义字典](https://upload-images.jianshu.io/upload_images/6641583-8fd0e1d46a6409ae.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/640)
```python
from LAC import LAC

#装载分词模型
lac = LAC(mode='seg')

#加载自定义字典
lac.load_customization('自定义字典.txt', sep=None)

text='我是一名北漂的打工人、干饭人'
lac.run(text)

text_list=['我是一名北漂的打工人、干饭人',
           '5月15日，航天科研人员在北京航天飞行控制中心指挥大厅庆祝我国首次火星探测任务着陆火星成功']
lac.run(text_list)
```
![加载自定义字典](https://upload-images.jianshu.io/upload_images/6641583-079ffa957b927545.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)

从上面的输出结果可以看出，已经正确分词

# 历史相关文章
- [自然语言处理（NLP） Bert与Lstm结合](https://www.jianshu.com/p/767931a5b994)
- [Python加载txt数据乱码问题升级版解决方法](https://www.jianshu.com/p/e2572f67c983)
**************************************************************************
**以上是自己实践中遇到的一些问题，分享出来供大家参考学习，欢迎关注微信公众号：DataShare ，不定期分享干货**
