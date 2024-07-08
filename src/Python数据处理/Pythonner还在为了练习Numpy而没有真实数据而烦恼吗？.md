#前言
Python里面在数据处理、数据分析、数据可视化、数据挖掘等领域，用到的库有Numpy、Pandas、Matplotlib、Sklearn、Scipy等，这些库都是建立在Numpy基础之上，因此学习Numpy是每个Pythoner进入数据科学领取的必经之路。
在练习Numpy时肯定离不开数据，可以随机生成，也可以自己去搜集，这些都可以，**但是在手机发达的今天，还有一种数据更容易直接获得、而且还很真实，这就是照片，RGB值，下面就来详细介绍怎么把照片读取为Numpy数组。**
#通过读取照片获得Numpy数组
读取照片的库有很多，这里推荐大家直接用PIL（PIL即Python Imaging Library，也即为我们所称的Pillow，是一个很流行的图像库，它比opencv更为轻巧，正因如此，它深受大众的喜爱。）以下面这张《家乡的风力发电基地.jpg》为案例，来介绍怎么把照片变为Numpy数组。
![家乡的风力发电基地](https://upload-images.jianshu.io/upload_images/6641583-85001824fd43f9c1.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 导入相关的库
```
import numpy as np
from PIL import Image
```
- 读取照片
```
img = Image.open('家乡的风力发电基地.jpg')
img   #显示照片
```
- 查看照片的属性
```
print(img.format)
print(img.size)  #(w，h)  宽，高
print(img.mode)
```
![](https://upload-images.jianshu.io/upload_images/6641583-7b2e472d926a2ecd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)
- 转换为Numpy数组
```
img_array=np.array(img)
img_array
```
![](https://upload-images.jianshu.io/upload_images/6641583-5d2d8795574665e8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)
- 查看Numpy数组属性
```
print(img_array.shape)   #(height,width,channel)  高，宽，通道数（RGB值）
print(img_array.dtype)   #数据类型
print(img_array.size)    #数组中所有元素的个数  400*600*3
```
![](https://upload-images.jianshu.io/upload_images/6641583-cf4db8793122198e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)

- 开始你的各种练习
这里简单展示一下，转为RGB三列数据
![](https://upload-images.jianshu.io/upload_images/6641583-caa2c071fef28c2a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)
#历史相关文章
- [Numpy中的shuffle和permutation区别](https://www.jianshu.com/p/cf7d040a05f8)
- [Python基于opencv “三维”旋转图片，解决日常小问题](https://www.jianshu.com/p/88a8154c8bc2)

**************************************************************************
**以上是自己实践中遇到的一些问题，分享出来供大家参考学习，欢迎关注微信公众号，不定期分享干货**
![](https://upload-images.jianshu.io/upload_images/6641583-bce6d13cc37824d7.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/240)


