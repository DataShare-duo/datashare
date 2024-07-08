#背景
在进行数据建模时（有时也叫训练模型），我们需要先经过数据清洗、特征选择与特征构造等预处理步骤，然后构造一个模型进行训练，其中One-Hot编码属于数据清洗步骤里面。
#One-Hot意义
在进行特征处理时，分类数据和顺序数据这种字符型变量，无法直接用于计算，那么就需要进行数值化处理。其中分类数据，比如一个特征包含红（R），绿（G），蓝（B）3个分类，那么怎么给这3个分类进行数值化处理呢，可以直接用1,2,3来表示吗，**肯定不行，如果用1,2,3表示，那么3种颜色之间就会产生等级差异，本来他们之间应该是平等的**，这时就需要进行one-hot编码（哑变量），如下图所示的转换
![one-hot](https://upload-images.jianshu.io/upload_images/6641583-f59372eab9db16ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)
#实操数据
利用西瓜数据集（部分特征）为例进行实操，这个数据在网上都可下载到
![西瓜数据集](https://upload-images.jianshu.io/upload_images/6641583-802d00130db8653b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)
读取西瓜数据到数据框里面
```python
import pandas as pd

data = pd.read_excel('西瓜数据集.xlsx', sheet_name='西瓜')

data.head()
```
![读取西瓜数据](https://upload-images.jianshu.io/upload_images/6641583-40756cb1636646c9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)


#常用方法
- **pandas里面的get_dummies方法**
这个方法是最简单，最直接的方法
```python
#也可以用concat,join
data_onehot=data.merge(pd.get_dummies(data,columns=['色泽','触感']),on='编号')    

data_onehot.head()
```
![pd.get_dummies](https://upload-images.jianshu.io/upload_images/6641583-76ae828a0a2a0669.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)
- **sklearn里面的One-HotEncoder方法**
利用One-HotEncoder进行转换
```python
from sklearn.preprocessing import OneHotEncoder

one_hot=OneHotEncoder()

data_temp=pd.DataFrame(one_hot.fit_transform(data[['色泽','触感']]).toarray(),
             columns=one_hot.get_feature_names(['色泽','触感']),dtype='int32')
data_onehot=pd.concat((data,data_temp),axis=1)    #也可以用merge,join

data_onehot.head()
```
![OneHotEncoder](https://upload-images.jianshu.io/upload_images/6641583-21f709c3a6da15b1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)
- **自定义函数方法**
```python
def OneHot(df,columns):
    df_new=df.copy()
    for column in columns:
        value_sets=df_new[column].unique()
        for value_unique in value_sets:
            col_name_new=column+'_'+value_unique
            df_new[col_name_new]=(df_new[column]==value_unique)
            df_new[col_name_new]=df_new[col_name_new].astype('int32')
    return df_new

data_onehot_def=OneHot(data,columns=['色泽','触感'])

data_onehot_def.head()
```
![OneHot_def](https://upload-images.jianshu.io/upload_images/6641583-834bbbd8c224a05c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1040)
#历史相关文章
- **[Python pandas 里面的数据类型坑，astype要慎用](https://www.jianshu.com/p/19c537f24b34)**
- **[Pandas数据处理误区要知其然知其所以然](https://www.jianshu.com/p/6d554114ab33)**
- **[Python pandas 数据筛选与赋值升级版详解](https://www.jianshu.com/p/0e27025e9010)**
- **[历史双色球数据分析---python](https://www.jianshu.com/p/79979e7982fa)**
