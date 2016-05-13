2016年4月13日10:16:37
vedio 文件夹主要目的是从视频文件中获得人脸数据库的一些小工具。

1、video_to_pic.exe  将视频中检测到的人脸保存到save_path中，不分类。
2、feature.exe 特征提取，可以使用feature.exe --help  查看帮助信息。对于输入图片的要求128*128，灰度，归一化到0-1
3、ext_feature.exe  暂时不用
4、text_process.py  里面主要包括了创建imagelist.txt文件的函数，可以创建带标签的，也可以创建不带标签的，具体使用可以查看里面的函数说明。
5、vedio.py 现在主要包括三个函数，人脸检测，图片清晰度清晰，提取特征，

2016年5月13日09:23:42
对各个文件中函数做个列表，方便大家查找
No1.text_process.py

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
'''

No2.Math.py 里就两个函数计算1、计算cos距离；2、比较两个数的大小

No3.classficition.py
'''
函数：classficiton（）
函数功能：此函数并不是直接将图片进行分类，因为我的目的是整理数据，如果每张图片都提取特征
         再归类，时间太浪费。所以，我先前提取特征，把每个特征保存到一个.txt文件中，再
         利用这些文件提取特征
输入参数：features_path----保存特征文件的路径
         save_path----保存分类结果路径
         picture_path----保存着图片的路径，也就是分类前的图片
         suff----图片的后缀名，默认.bmp
'''

No4.ext-classficition.py 这是一个加强版的分类脚本，将小于10张图片的类别直接删除掉
'''
函数：classficiton（）
函数功能：此函数并不是直接将图片进行分类，因为我的目的是整理数据，如果每张图片都提取特征
         再归类，时间太浪费。所以，我先前提取特征，把每个特征保存到一个.txt文件中，再
         利用这些文件提取特征
输入参数：features_path----保存特征文件的路径
         save_path----保存分类结果路径
         picture_path----保存着图片的路径，也就是分类前的图片
         suff----图片的后缀名，默认.bmp
'''

No5.face_detection.py
'''
函数：face_detection（）
函数功能：检测人脸，保存人脸框
输入参数：imagelist----图片路径列表
	  bboxlist----保存人脸框文件
'''

No6.vedio.py
'''
函数：vedio_to_pic（）
功能：从视频文件中提取人脸保存到文件中
输入参数：vedio_path----视频文件路径
         save_path----保存文件路径
         suff----保存文件的后缀名
'''

'''
函数：sharpness_clean()
功能：进行清晰度检测，删除清晰度低的图片
输入参数：imagelist----储存图片路径的文件
         save_path----保存图片的路径
         dis----阈值
'''

'''
函数：ext_feature()
功能：提取图片特征，把每张图片特征保存成一个.txt文件
输入参数：proto----网络配置文件
         model----模型文件
         imagelist----保存图片路径的文件
         out----保存特征文件的文件夹路径
'''

