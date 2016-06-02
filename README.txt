2016年6月2日17:18:30
增加了statistics.py
'''
函数：Describe()
函数功能：统计训练结果信息
输入参数：result----输出结果.txt文件
         outdir----保存结果文件夹
'''
'''
函数：DataSetInfo（）
函数功能：由于数据集分布不平均，通过统计直方图查看分布情况
输入参数：dirpath----数据集路径
         isplot----是否绘图
'''

2016年5月26日17:54:15
增加了一个制作imagelistGUI小工具，很好玩儿的，大家可以试试。

2016年5月26日17:06:15
这次更新新增加了几个函数
text_process.py
'''
函数：TxtToCsv（）
函数功能：将.txt文件转换成csv，这个函数只是在特定情况，针对特定类型.txt使用，
        并不通用，缺点是不具有普适性
输入参数：txt----.txt文件
         csv----.csv文件
'''
'''
函数：Find（）
函数功能：寻找包含特定文件数的文件夹
输入参数：dirpath----数据集路径
         num----文件夹的数量
'''
Picture.py
'''
函数：DataAugmentFlip（）
函数功能：扩大数据量,主要是通过翻转
输入参数：dir_path----图片库路径
         num----一个阈值，处理文件少于num文件内的图片
         targetnum----目标数量，即打算扩充后的图片数量
'''
'''
函数：DataAugmentCrop()
函数功能：通过随机剪裁扩充数据
输入参数：picdir----图片库文件夹路径
         leftup----是否从左上角剪裁,默认
         leftdown----是否从左下角剪裁
         rightup----是否从右上角剪裁
         rightdown----是否从右下角剪裁
         new_w----剪裁后图片宽度
         new_h----剪裁后图片长度
         picnum----处理小于picnum的文件夹
         addnum----扩充数量addnum*model
         targetnum----目标数量，即打算扩充后的图片数量
'''
'''
函数：DataBalance（）
函数功能：平衡数据集，但只是粗略的并不能十分精确
输入参数：dirpath----数据集路径
         baisnum----基准数，就是想要的平均数，这里要说明一下，我做的只是少量数据的扩充
         因此大于baisnum的文件夹并没有处理,最好的2的倍数
		 new_h----处理后图片高度
		 new_w----处理后图片宽度
'''

<<<<<<< HEAD
2016年5月13日09:37:58
No1.CreatImagelist.py  
这个不是出自我的手，但是却非常有用，可以产生带标签的图片路径列表

No2.dir_to_picture.py  
这个主要功能是将分好类的图片（在多个文件夹中）重新整理到一个文件夹中，便于删除

No3.extract_feacture.py
这个的主要功能是批量提取图片的特征，并将特征保存成文件

No4.feature_class.py
这个也是特征分类，但是这个每张图片都一一对比，如果数据量小可以，如果数据量大这个脚本太浪费时间

No5.Math.py 里就两个函数计算1、计算cos距离；2、比较两个数的大小

No6.text_process.py

'''
函数：name_convert（）
功能：采集到的图片名字命名时是字符型，将其转换成000000001形式
     另外进行比例缩放到128*128，同时转成灰度图
输入的参数：dir_name  只存放图片的文件夹名字
           dir_name_save  保存结果文件夹
'''

'''
函数：creat_imagelist_NoLabel()
功能：是把一个文件夹下所有图片写进一个imagelist.txt文件中
输入参数：dir_path 存放图片的文件夹
         imagelist_path,保存路径
'''

'''
函数：clean_image()
功能：人脸检测后把没有检测到的人脸剔除
输入参数：imagelist---人脸检测后的路劲列表
         dir_path_save---保存路径
'''

'''
函数：CreatImageListWithLabel()
功能：创建caffe imagelist.txt 文件，此文件带标签
输入参数：dir_path 图片路径，一般为保存很多子文件夹的跟文件夹路径
         imgelist 输出文件路径默认是当前文件夹下
'''

'''
函数：load()
函数功能：将一个文本文件中的特征读取到一个list中
输入参数：file_path----文本文件路径
'''

'''
函数：Pic_Num()
功能：统计文件夹中图片的数量
输入参数：dir_path----保存图片的文件夹路径
'''

'''
函数：ReName（）
功能：重新按顺序命名文件，用在对个别文件删除后，对文件重新排序命名
输入参数：dir_path----包含文件（无文件夹的）的文件夹路径

No7.Visualize.py   网络权重可视化，未完
'''
函数：vis_square()
函数功能：一个显示辅助函数
输入参数：data
        out----保存图片的路径
'''
'''
函数：VisualWeights()
函数功能：根据层名字显示相应的权重
输入参数：layer_name----层名字
         net----初始化后的网络
         out----保存图片的路径
'''
'''
函数：VisualWeight()
函数功能：根据层名字显示相应的权重
输入参数：layer_name----层名字
         net----初始化后的网络
'''
'''
函数：VisualBlob()
函数功能：可视化Blob
输入参数：net----初始化后的网络
         layer_name----层的名字
'''
'''
函数：VisualBlobs()
函数功能：保存所有Blobs
输入参数：net----初始化后的网络
         out----保存路径
'''
'''
函数：VisualLayerShape()
函数：显示层的名字和形状
输入参数：net----初始化后的网络
'''
'''
函数：VisualLayerWeightShape()
函数功能：显示各层权重的形状
输入参数：net----初始化后的网络
'''
No8.Picture.py
'''
函数：Resize（）
函数功能：批量调整图片大小
输入参数：dir_path----文件库路径
         new_h，new_w----新图片的高度和宽度
'''
'''
函数：DataAugment（）
函数功能：扩大数据量
输入参数：dir_path----图片库路径
'''

No9.draw.py
'''
函数：Draw（）
函数功能：绘制WU_lfw_test.py 产生的result.txt文件的图
输入参数：file_path
'''
'''
函数：Draw_His（）
函数功能：计算图片库的一些统计信息，并画出直方图
输入参数：dir_path
'''

No10.CreatValSet.py
'''
函数：TestPair（）
函数功能：随机产生验证集对，来测试网络性能
输入参数：dir_path----验证集库
         class_num----验证集的类别
         leftlist----left.txt 路径
         rightlist----right.txt 路径
         label----标签路径
         pos_num----正样本数量
         neg_num----负样本数量
'''

No11.LfwTest.py  在lfw库上测试模型

No12.process.py
'''
函数：renamedir（）
函数功能：重命名文件夹，按一定顺序
输入参数：dir_path----包含子文件夹的路径
         start   ----开始序号
'''
'''
函数：Rmovedir（）
函数功能：删除文件夹中文件少于一定数量的文件夹
输入参数：dir_path----包含子文件夹的路径
         num----阈值，将文件数量小于等于num的文件夹删掉
'''
'''
函数： Romvepath（）
函数功能：删除一个imagelist中不存在的路径
输入参数：inputlist,outputlist
'''
'''
函数：Rmovepath_pair()
函数功能：成对删除文件中不存在的路径
输入参数：input1,input2,inlabel,output1,output2,outlabel
'''
'''
函数：TestPair（）
函数功能：从数据库中挑选正负样本
输入参数：dir_path----存放图片库路径
         class_num----类别数量
         neg_num----负样本数
         pos_num----正样本数
         leftlist
         rightlist
         label
'''
'''
函数：Select_K_MaxMin()
函数功能：输出文件夹中图片数量最多或最小的前K个文件夹路径
输入参数：dir_path----图片库路径
         model----选择最大还是最小默认
         K----前K个
'''
=======
   这里主要是我在使用caffe是编写的一些小脚本，你可以自由免费的使用，也希望把你的小工具与大家分享。我已经把每个函数的功能和输入参数做了说明，如果你有使用上的问题可以给我发送电子邮件451413025@qq.com。
   在这里对vedio做一点说明，vedio里的特征提取部分可能在你的计算机上无法运行，那个针对我自己的项目编写的部分，尤其是featue.exe文件。但是你可以自己编写特征提取部分，然后修改main.py文件即可。
   仍在更新之中........
>>>>>>> origin/master
