# 背景
在计算相似度时，常常用到余弦夹角来判断相似度，Cosine（余弦相似度）取值范围[-1,1]，当两个向量的方向重合时夹角余弦取最大值1，当两个向量的方向完全相反夹角余弦取最小值-1，两个方向正交时夹角余弦取值为0。
$$cos(x_1,x_2)=\frac{x_1·x_2}{|x_1||x_2|}$$
在实际业务中运用的地方还是挺多的，比如：可以根据历史异常行为的用户，找出现在有异常行为的其他用户；在文本分析领域，可以根据一些文章，找出一些相似文章（把文章转换为向量）。

计算相似度的方法除了余弦夹角，还可以利用距离来判断相似，距离越近越相似，这里不做详细展开。
# 自定义函数法

```python
import numpy as np
def cosine_similarity(x,y):
    num = x.dot(y.T)
    denom = np.linalg.norm(x) * np.linalg.norm(y)
    return num / denom
```
输入两个`np.array`向量，计算余弦函数的值
```python
cosine_similarity(np.array([0,1,2,3,4]),np.array([5,6,7,8,9]))
#0.9146591207600472

cosine_similarity(np.array([1,1]),np.array([2,2]))
#0.9999999999999998

cosine_similarity(np.array([0,1]),np.array([1,0]))
#0.0
```
# 基于sklearn
```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

a1=np.arange(15).reshape(3,5)
a2=np.arange(20).reshape(4,5)

cosine_similarity(a1,a2)   #第一行的值是a1中的第一个行向量与a2中所有的行向量之间的余弦相似度

cosine_similarity(a1)   #a1中的行向量之间的两两余弦相似度
```

>cosine_similarity(X, Y=None, dense_output=True)
X : ndarray or sparse array, shape: (n_samples_X, n_features)
    Input data.---------------X是二维的矩阵
Y : ndarray or sparse array, shape: (n_samples_Y, n_features)
    Input data. If ``None``, the output will be the pairwise
    similarities between all samples in ``X``.---------------Y也是二维的矩阵

![sklearn余弦相似度](https://upload-images.jianshu.io/upload_images/6641583-6f38d392eb993e79.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 历史相关文章
- [Python Numpy中的范数](https://www.jianshu.com/p/343618e8e455)
- [Python 如何确定K-Means聚类的簇数](https://www.jianshu.com/p/0e74342b9b0b)
**************************************************************************
**以上是自己实践中遇到的一些问题，分享出来供大家参考学习，欢迎关注微信公众号DataShare，不定期分享干货**
