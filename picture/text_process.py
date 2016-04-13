# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 11:51:03 2016

@author: Administrator
"""

import cv2
import os
import shutil

'''
函数：name_convert（）
功能：采集到的图片名字命名时是字符型，将其转换成000000001形式
     另外进行比例缩放到128*128，同时转成灰度图
输入的参数：dir_name  只存放图片的文件夹名字
           dir_name_save  保存结果文件夹
'''
def name_convert(dir_name,dir_name_save):
    num = 0
    for dirpath,dirnames,filenames in os.walk(dir_name):
        for files in filenames:
            image_path = dir_name + '/' + files
            img = cv2.imread(image_path)
            res = cv2.resize(img,(128,128))
            gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
            save_file_path = "%s%s%09d%s"%(dir_name_save,'/',num,'.bmp')
            num += 1
            if num%1000 == 0:
                print u'已经完成 %d 张........'%(num)
            cv2.imwrite(save_file_path,gray)
    print u'name_covert 完成 共处理 %d 张图片'%(num)
            
            
'''
函数：creat_imagelist_NoLabel()
功能：是把一个文件夹下所有图片写进一个imagelist.txt文件中
输入参数：dir_path 存放图片的文件夹
         imagelist_path,保存路径
'''
def creat_imagelist_NoLabel(dir_path,imagelist_path):
    fr = open(imagelist_path,'w')
    count = 0
    for dirpath,dirnames,filenames in os.walk(dir_path):
        for files in filenames:
            image_path = dir_path + '/' + files + '\n'
            fr.write(image_path)
            count += 1
    fr.close()
    print u'creat_imageslist_NoLabel 完成，共%d张图片'%(count)
    
    
'''
函数：clean_image()
功能：人脸检测后把没有检测到的人脸剔除
输入参数：imagelist---人脸检测后的路劲列表
         dir_path_save---保存路径
'''
def clean_image(imagelist,dir_path_save):
    if not os.path.exists(dir_path_save):
        os.mkdir(dir_path_save)
        
    fr = open(imagelist,'r')
    lines = fr.readlines()
    num = 0
    
    for line in lines:
        sourcefile_path = line.strip('\n')
        targefile_path = "%s%s%09d%s"%(dir_path_save,'/',num,'.bmp')
        shutil.copyfile(sourcefile_path,targefile_path)
        num += 1
        if num%1000 == 0:
            print u"clean_image  %d  张图片"%(num)
    print u"已经完成 clean_image  共%d张图片"%(num)


if __name__ == '__main__':
    dir_name = 'E:/practical_face/passerbPhoto'
    dir_name_save = 'E:/practical_face/result/passerbPhoto'
    if not os.path.exists(dir_name_save):
        os.mkdir(dir_name_save)
        '''
    name_convert(dir_name,dir_name_save)
    '''
    '''
    imagelist_path = 'E:/practical_face/result/imagelist.txt'
    creat_imagelist_NoLabel(dir_name_save,imagelist_path)
    '''
    clean_image('E:/practical_face/result/clean_imagelist.txt','E:/practical_face/result/clean_image')