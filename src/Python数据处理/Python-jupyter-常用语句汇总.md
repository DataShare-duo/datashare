#1.全局设置
```
#显示所有列
pd.set_option('display.max_columns', None)

#显示所有行
pd.set_option('display.max_rows', None)

#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)

#禁止自动换行(设置为Flase不自动换行，True反之)
pd.set_option('expand_frame_repr', False)

#打开修改时复制机制
pd.set_option("mode.copy_on_write", True)

#打印时显示全部数组信息
np.set_printoptions(threshold=np.inf)
```
#2.画图
```
#内嵌画图
%matplotlib inline

#单独画图
%matplotlib qt
```
#3.显示
```
#让一个cell同时有多个输出print
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all" 
```
