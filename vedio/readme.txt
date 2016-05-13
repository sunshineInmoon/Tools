2016年4月13日10:16:37
vedio 文件夹主要目的是从视频文件中获得人脸数据库的一些小工具。

1、video_to_pic.exe  将视频中检测到的人脸保存到save_path中，不分类。
2、feature.exe 特征提取，可以使用feature.exe --help  查看帮助信息。对于输入图片的要求128*128，灰度，归一化到0-1
3、ext_feature.exe  暂时不用
4、text_process.py  里面主要包括了创建imagelist.txt文件的函数，可以创建带标签的，也可以创建不带标签的，具体使用可以查看里面的函数说明。
5、vedio.py 现在主要包括三个函数，人脸检测，图片清晰度清晰，提取特征，
