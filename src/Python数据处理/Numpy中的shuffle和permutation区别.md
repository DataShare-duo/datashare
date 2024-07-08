# 主要区别
- `shuffle`没有返回值，直接在原来的数据上进行打乱排序，没有返回；而`permutation`是在数据副本上面进行打乱，返回打乱之后的副本。
- 由于permutation会复制数据，所以当数据量特别大的时候，使用shuffle的效率更高。
- 无论是`shuffle`还是`permutation`对二维及以上数据，都是只对**第一维进行打乱顺序**，第二维中的顺序并不会打乱。
# 示例
![示例](https://upload-images.jianshu.io/upload_images/6641583-114773a39b850879.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
