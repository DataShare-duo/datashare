# 背景
由于昨天利用基础库Matplotlib画的不是很完美，今天借助高级可视化库pyecharts来重新再实现一下人民日报的各国疫情图。

#pyecharts简介
>[Echarts](https://github.com/ecomfe/echarts) 是一个由百度开源的数据可视化，凭借着良好的交互性，精巧的图表设计，得到了众多开发者的认可。而 Python 是一门富有表达力的语言，很适合用于数据处理。当数据分析遇上数据可视化时，[pyecharts](https://github.com/pyecharts/pyecharts) 诞生了。

# 《人民日报》  VS   pyecharts制作
数据均是截至到2020年3月14日0时，各国疫情累计确诊人数，可以明显看出人民日报的图可能是PS出来的~~~
![人民日报](https://upload-images.jianshu.io/upload_images/6641583-5e104e3137c26987.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/440)

![pyecharts制作](https://upload-images.jianshu.io/upload_images/6641583-c30228831c00604f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/440)


#安装pyecharts
官网：[https://pyecharts.org/#/](https://pyecharts.org/#/)

```
#在终端中安装，或者Anaconda Prompt 中
pip install pyecharts
#conda install pyecharts

#查看是否安装成功
import pyecharts

print(pyecharts.__version__)
# 1.7.1
```
# 整个画图代码
```
#导入pandas
import pandas as pd

#读取数据
data=pd.read_excel('海外疫情.xlsx')

#自定义了一个人民日报的颜色主题
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"

from pyecharts.datasets import register_files
register_files({"people_COVID": ["themes/people_COVID", "js"]})

#导入pyecharts用到的内容
from pyecharts import options as opts
from pyecharts.charts import Pie

#画图
p=Pie(init_opts=opts.InitOpts(width="1000px", height="1200px",theme='people_COVID'))
p.add('',
      [list(z) for z in zip(data['国家'][:30],data['累计'][:30])],
      radius=["7%", '100%'],   #内半径，外半径
      center=["50%", "60%"],   #中心点的坐标位置
      rosetype="area",        
      is_clockwise=False,   #逆时针
      label_opts=opts.LabelOpts(is_show=False))  #标签显示设置
p.set_global_opts(title_opts=opts.TitleOpts(title="新冠肺炎全球疫情形势",
                                            pos_left="30%",
                                            pos_top="12%",
                                            title_textstyle_opts=opts.TextStyleOpts(font_size=30)
                                           ),
                 legend_opts=opts.LegendOpts(is_show=False)
                 )

p.render_notebook()
# p.render("pie.html")
```

#参考资料
1.http://gallery.pyecharts.org/#/Pie/pie_rosetype
2.https://echarts.baidu.com/theme-builder/
3.https://github.com/pyecharts/pyecharts-assets
4.https://www.sioe.cn/yingyong/yanse-rgb-16/
