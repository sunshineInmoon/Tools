# -*- coding: utf-8 -*-
"""
Created on Fri May 06 14:14:09 2016

@author: Sun
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
'''
函数：Draw（）
函数功能：绘制WU_lfw_test.py 产生的result.txt文件的图
输入参数：file_path
'''
def Draw(file_path):
    neg=[]
    pos=[]
    fr = open(file_path)
    lines = fr.readlines()
    for line in lines:
        curline = line.strip('\n').split('，')
        if curline[1] == '负样本':
            neg.append(float(curline[2].split(':')[-1]))
        else:
            pos.append(float(curline[2].split(':')[-1]))
    x_n = np.arange(0,len(neg))
    x_p = np.arange(0,len(pos))
    plt.figure()
    #ax = fig.add_subplot(111)
    
    plt.plot(x_n,neg,'g',label=u"负")
    avg_n = float(sum(neg))/len(neg)
    avg = [avg_n]*len(neg)
    plt.plot(x_n,avg,'b')
    
    plt.plot(x_p,pos,'r')
    avg_p = float(sum(pos))/len(pos)
    avg = [avg_p]*len(pos)
    plt.plot(x_p,avg,'y')
    
    plt.xlabel('Sample')
    plt.ylabel('Dis')
    plt.title('Model Test')
    plt.legend()
    plt.show()
    
    
'''
函数：Draw_His（）
函数功能：计算图片库的一些统计信息，并画出直方图
输入参数：dir_path
'''
def Draw_His(dir_path):
    if not os.path.exists(dir_path):
        print u'路径不存在。。。。'
    else:
        lines=[]
        for dirs in os.listdir(dir_path):
            sub_dir = dir_path + '/' + dirs
            files = os.listdir(sub_dir)
            print len(files)
            lines.append(len(files))
        s = pd.Series(lines)
        print s.describe()
        #print s.value_counts()
        #plt.hist(lines,bins=50)
        print np.argmax(lines)
        x = np.linspace(0,1,len(os.listdir(dir_path)))
        plt.figure()
        plt.xlabel('file_No')
        plt.ylabel('Pic_Num')
        plt.title('tongjixinxi')
        plt.plot(x,lines,'r',label='Num')
        plt.legend()
        plt.show()
if __name__=='__main__':
    #Draw('E:/Face_data/result_my_2.txt')
    Draw_His('E:/Face_data/FaceImages5')