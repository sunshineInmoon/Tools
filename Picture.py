# -*- coding: utf-8 -*-
"""
Created on Tue May 03 16:36:36 2016

@author: Administrator
"""

import cv2
import os
import copy
'''
函数：Resize（）
函数功能：批量调整图片大小
输入参数：dir_path----文件库路径
         new_h，new_w----新图片的高度和宽度
'''
def Resize(dir_path,new_h,new_w):
    for dirs in os.listdir(dir_path):
        print dirs
        sub_dir = dir_path + '/' + dirs
        if os.path.isdir(sub_dir):
            for files in os.listdir(sub_dir):
                print files
                file_path = sub_dir + '/' + files
                img = cv2.imread(file_path)
                shape = img.shape
                if (int(shape[0])==128) and (int(shape[1])==128):
                    continue
                res = cv2.resize(img,(new_h,new_w),interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(file_path,res)

'''
函数：DataAugment（）
函数功能：扩大数据量
输入参数：dir_path----图片库路径
'''
def DataAugment(dir_path):
    if not os.path.exists(dir_path):
        print u'路径不存在'
    else:
        dirs = os.listdir(dir_path)
        for subdir in dirs:
            sub_dir = dir_path + '/' + subdir
            files = os.listdir(sub_dir)
            fileNum = len(files)
            if fileNum > 25:
                continue
            num=0
            for fr in files:
                suff = fr.split('.')[1]
                filename = sub_dir + '/' + fr
                img = cv2.imread(filename)
                size = img.shape
                iLR = copy.deepcopy(img)
                h = size[0]
                w = size[1]
                for i in range(h):
                    for j in range(w):
                        iLR[i,w-1-j]=img[i,j]
                new_name ="%s/%09d.%s"%(sub_dir,num,suff)
                num+=1
                cv2.imwrite(new_name,iLR)
                #cv2.imshow('image',iLR)
                #cv2.waitKey(0)
if __name__=='__main__':
    dir_path = 'E:/Face_data/FaceImages5'
    new_h = 128
    new_w = 128
    #Resize(dir_path,new_h,new_w)
    DataAugment(dir_path)