# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:09:06 2016

@author: Administrator
"""

import os
import sharpness
import shutil
import text_process

'''
函数：vedio_to_pic（）
功能：从视频文件中提取人脸保存到文件中
输入参数：vedio_path----视频文件路径
         save_path----保存文件路径
         suff----保存文件的后缀名
'''
def vedio_to_pic(vedio_path,save_path,suff):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    commnd_line = "vedio_to_pic.exe " + vedio_path +' ' + save_path +' ' + suff
    os.system(commnd_line)


'''
函数：sharpness_clean()
功能：进行清晰度检测，删除清晰度低的图片
输入参数：imagelist----储存图片路径的文件
         save_path----保存图片的路径
         dis----阈值
'''
def sharpness_clean(imagelist,save_path,dis=40):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    fr = open(imagelist,'r')
    lines = fr.readlines()
    num = 0;
    for line in lines:
        words = line.strip('\n').split('.')
        suff = words[1]
        new_filename = "%s%09d%s"%(save_path+'/',num,'.'+suff)
        d = sharpness.detection(line.strip('\n'))
        if d>dis:
            shutil.copyfile(line.strip('\n'),new_filename)
            num+=1
    print u'清晰度清除已经完成，共保留%d张图片'%(num)

'''
函数：ext_feature()
功能：提取图片特征，把每张图片特征保存成一个.txt文件
输入参数：proto----网络配置文件
         model----模型文件
         imagelist----保存图片路径的文件
         out----保存特征文件的文件夹路径
'''
def ext_feature(proto,model,imagelist,out):
    if not os.path.exists(out):
        os.mkdir(out)
    command_line = "%s %s %s %s %s"%("feature.exe","--proto="+proto,\
                    "--model="+model,"--imagelist="+imagelist,"--out="+out)
    os.system(command_line)
    print u'特征提取完毕'

if __name__ == "__main__":
    vedio_path = 'E:/1-18/12mm/2.avi'
    save_path = 'E:/practical_face/result/code/video/Output/Pictures'
    suff = '.bmp'
    a = sharpness.detection('E:/wu_test/pictures1/000000000.jpg')
    print a
    
    '''
    pic_dath = 'E:/practical_face/result/code/video/Output/Pictures'
    imagelist = 'E:/practical_face/result/code/video/Output/imagelist.txt'
    save_path = 'E:/practical_face/result/code/video/Output/sharpness_clean'
    text_process.creat_imagelist_NoLabel(pic_dath,imagelist)
    sharpness_clean(imagelist,save_path,40)
    '''
    proto = 'C:/Users/Administrator/Desktop/model/net_deploy.prototxt'
    model = 'C:/Users/Administrator/Desktop/model/net.caffemodel'
    imagelist = 'E:/practical_face/result/code/video/Output/imagelist1.txt'
    dir_path = 'E:/practical_face/result/code/video/Output/sharpness_clean'
    out = 'E:/practical_face/result/code/video/Output/txt'
    text_process.creat_imagelist_NoLabel(dir_path,imagelist)
    ext_feature(proto,model,imagelist,out)