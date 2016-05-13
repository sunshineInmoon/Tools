# -*- coding: utf-8 -*-
"""
Created on Fri May 06 15:04:52 2016

@author: Sun
"""
import os
import shutil
import random

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
def TestPair(dir_path,class_num,leftlist,rightlist,label,pos_num=3000,neg_num=3000):
    left = open(leftlist,'w')
    right = open(rightlist,'w')
    label = open(label,'w')
    
    dirs = os.listdir(dir_path)
    
    print u'产生正样本'
    for i in range(pos_num):
        sample = random.randint(0,class_num-1)
        sub_dir = dir_path + '/' + dirs[sample]
        files = os.listdir(sub_dir)
        l = len(files)
        file1 = random.randint(0,l-1)
        file2 = random.randint(0,l-1)
        while(file1 == file2):
            file2 = random.randint(0,l-1)
        file1_path = sub_dir + '/' + files[file1]
        file2_path = sub_dir + '/' + files[file2]
        left.write(file1_path+'\n')
        right.write(file2_path+'\n')
        label.write('1'+'\n')
        print i
        
    left.close()
    right.close()
    label.close()
if __name__=='__main__':
    TestPair('E:/Face_data/FaceImages_1',500,'E:/Face_data/left_1.txt','E:/Face_data/right_1.txt',\
        'E:/Face_data/label_1.txt')