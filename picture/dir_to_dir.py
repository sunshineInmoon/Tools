# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:38:36 2016

@author: Administrator
"""

#import cv2
import os
import numpy as np
import pickle
import shutil

def dis_cos(a,b):
    sum0 = np.dot(a,b)
    sum1 = np.sqrt(np.sum(np.power(a,2)))
    sum2 = np.sqrt(np.sum(np.power(b,2)))
    return sum0/(sum1*sum2)
    
caffe_root='C:/Users/Administrator/Desktop/'
import sys
sys.path.append(caffe_root+'python')
sys.path.append('D:/Anaconda/Lib/site-packages/')
sys.path.append('D:/Documents/Downloads/protobuf-2.5.0/protobuf-2.5.0/python/')
import caffe

'''
input_txt = 'E:/practical_face/LogPhoto/imageList.txt'
output_dir = 'E:/practical_face/result/Positive'

fr = open(input_txt,'r')
lines = fr.readlines()
num = 0
for line in lines:
    path = line.strip().split(' ')[0]
    lable = line.strip().split(' ')[1]
    dir_name = output_dir + '/' + lable
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        num = 0
    img = cv2.imread(path)
    res = cv2.resize(img,(128,128))
    gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    output_path = "%s%s%d%s"%(dir_name,'/',num,'.bmp')
    num += 1
    cv2.imwrite(output_path,gray)
'''

'''
重新分类
'''

