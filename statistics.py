# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:59:02 2016

@author: Sun
"""

import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import text_process
import os
import sys

'''
函数：replace（）
函数功能：辅助函数，将连续值转换成离散值
'''
def replace(input):
    if input<0.1:
        return 0
    elif input<0.15:
        return 1
    elif input <0.2:
        return 1.5
    elif input <0.25:
        return 1.75
    elif input < 0.3:
        return 2
    elif input < 0.4:
        return 3
    elif input < 0.5:
        return 4
    elif input < 0.6:
        return 5
    elif input < 0.7:
        return 6
    elif input < 0.8:
        return 7
    elif input < 0.9:
        return 8
    elif input <= 1.1:
        return 9

'''
函数：Describe()
函数功能：统计训练结果信息
输入参数：result----输出结果.txt文件
         outdir----保存结果文件夹
'''
def Describe(result,outdir):
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    csvfile = outdir+'/'+'result.csv'
    text_process.TxtToCsv(result,csvfile)
    data = pd.read_csv(csvfile)
    #data.info()
    #print data.Similar.describe()
    l = []
    for i in data.Similar:
        num = replace(i)
        l.append(num)
    odj = Series(l)
    data['sim']=odj
    #print data.info()

    res0 = data.sim[data.Sample==0].value_counts()
    res1 = data.sim[data.Sample==1].value_counts()
    plt.rcParams['font.family']='SimHei'
    df=pd.DataFrame({u'负样本':res0,'正样本':res1})
    df.plot(kind='bar')
    plt.xlabel(u'相似度')
    plt.ylabel(u'数量')
    resultpic = outdir+'/'+'result.png'
    plt.savefig(resultpic)
    #plt.show()
    
'''
函数：DataSetInfo（）
函数功能：由于数据集分布不平均，通过统计直方图查看分布情况
输入参数：dirpath----数据集路径
         isplot----是否绘图
'''
def DataSetInfo(dirpath,isplot=False):
    if not os.path.exists(dirpath):
        print u'数据集路径不存在'
        sys.exit(0)
    else:
        files=[]
        dirs = os.listdir(dirpath)
        for sub in dirs:
            subdir=dirpath+'/'+sub
            fls = os.listdir(subdir)
            files.append(len(fls))
        #print files
        data = {'files':files}
        frame = pd.DataFrame(data)
        #print frame
        #data1 = frame['files'].value_counts()
        data1 = frame['files']
        print u'统计信息如下：'
        print data1.describe()
        if isplot == True:
            data1.plot(kind='bar')

if __name__=='__main__':
    
    result=r'E:/Face_data/result_my_2.txt'
    outdir=r'C:/Users/Sun/Desktop/model/add1_1'
    #Describe(result,outdir)
    
    
    dirpath=r'E:/Face_data/FaceImages3'
    DataSetInfo(dirpath)
    
