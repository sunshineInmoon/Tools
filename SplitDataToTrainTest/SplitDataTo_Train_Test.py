# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 15:06:19 2016

@author: Administrator
"""

import shutil
import os
'''
函数：SplitData（）
功能：将一个数据集按照特定比例分离成训练和测试两个数据集
输入参数：dir_path---存放数据集的文件夹路径
         percent---这里的百分比是训练集占总数据集的百分比
         train_path---训练集路径
         test_path---测试集路径
'''
def SplitData(dir_path,train_path,test_path,percent=0.1):
    if not os.path.exists(dir_path):
        print u'输入文件夹没有找到'
    else:
        if not os.path.exists(train_path):
            os.mkdir(train_path)
        if not os.path.exists(test_path):
            os.mkdir(test_path)
        train_count = 0
        test_count = 0
        for root,dirnames,filenames in os.walk(dir_path):
            #第一个root是dir_path 跳过
            if root == dir_path:
                continue
            #获得子文件夹文件名
            dirname = root.strip().split('\\')[-1]
            root_path = root + '/'
            #如果一个文件夹里图片数量小于10张 计算时加1处理
            #取每个子文件的前10%为test集
            Num = int(len(filenames)*percent) + 1
            sub_test_dir = test_path + '/' + dirname
            if not os.path.exists(sub_test_dir):
                os.mkdir(sub_test_dir)
            for i in range(Num):
                oldfile = root_path + filenames[i]
                newfile = sub_test_dir + '/' + filenames[i]
                shutil.copyfile(oldfile,newfile)
                test_count += 1
                #剩下的是train集
                sub_train_dir = train_path + '/' + dirname
            if not os.path.exists(sub_train_dir):
                os.mkdir(sub_train_dir)
            for k in range(Num,len(filenames)):
                oldfile = root_path + filenames[k]
                newfile = sub_train_dir + '/' + filenames[k]
                shutil.copyfile(oldfile,newfile)
                train_count += 1
                print u'处理完文件夹%s'%(dirname)
    print u'已经处理完分离操作，test集共%d张图片，train集共%d张图片'%(test_count,train_count)


if __name__ == '__main__':
    dir_path = 'E:/test/results'
    train_path = 'E:/test/train_data'
    test_path = 'E:/test/test_data'
    SplitData(dir_path,train_path,test_path)