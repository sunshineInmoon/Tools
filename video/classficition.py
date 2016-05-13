# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:55:51 2016

@author: Administrator
"""

import os
import Math
import text_process
import shutil
import sys
import numpy as np

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
def classficition(features_path,save_path,picture_path,suff='.bmp'):
    #标志序列，0表示没有比对过的，1表示已经比对过的
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    all_num = text_process.Pic_Num(features_path,count=[0])
    mark = [0]*all_num
    file_num = 0
    dis = 0.65# 此阈值可根据你自己需要更改
    
    for i in range(all_num):
        if mark[i] != 0:
            continue
        else:
            mark[i] = 1
            save_dir_name = "%s%d"%(save_path+'/',file_num)
            if not os.path.exists(save_dir_name):
                os.mkdir(save_dir_name)
            oldf_num = '%09d'%i
            oldfile_name = '%s%s%s'%(picture_path+'/',oldf_num,suff)
            
            newfile_name = '%s%s%09d%s'%(save_dir_name,'/',0,suff)
            shutil.copyfile(oldfile_name,newfile_name)
            
            bais_feature_num = i
            bais_feature_file = '%s%09d%s'%(features_path+'/',bais_feature_num,'.txt')
            bais_features_data = text_process.load(bais_feature_file)
            
            j = i + 2000 #在1000张范围内搜索
            end = Math.Min(j,all_num)
            num = 1
            for k in range(i+1,end):
                if mark[k] != 0:
                    continue
                else:
                    feature_num = k
                    feature_file = '%s%09d%s'%(features_path+'/',feature_num,'.txt')
                    feature_data = text_process.load(feature_file)
                    #计算相似度
                    sim = Math.dis_cos(np.array(bais_features_data),np.array(feature_data),256,'false')
                    if sim<dis:
                        continue
                    else:
                        mark[k] = 1
                        oldf_num = '%09d'%k
                        oldfile_name = '%s%s%s'%(picture_path+'/',oldf_num,suff)
                        newfile_name = '%s%s%09d%s'%(save_dir_name,'/',num,suff)
                        num += 1
                        shutil.copyfile(oldfile_name,newfile_name)
            file_num += 1
    print u'分类结束，共得到%d类'%(file_num)


if __name__ == '__main__':
    #features_path = 'E:/practical_face/result/code/video/Output/txt'
    #save_path = 'E:/practical_face/result/code/video/Output/result'
    #picture_path = 'E:/practical_face/result/code/video/Output/sharpness_clean'

    #features_path = sys.argv[1]
    #save_path = sys.argv[2]
    #picture_path = sys.argv[3]
    #suff = sys.argv[4]
    features_path = 'E:/test/color/feature'
    save_path = 'E:/test/color/result'
    picture_path = 'E:/test/color/picture'
    classficition(features_path,save_path,picture_path,'.jpg')

