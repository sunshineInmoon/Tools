# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 10:02:48 2016

@author: Administrator
"""

import Math
import pickle
import os
import shutil
import text_process
'''
函数：feature_clas（）
功能：根据提取到的每张图片的特征，进行大循环分类
输入参数：imagelist---存放图片路径的.txt文件，主要利用这个文件获得图片数量和图片路径
         save_path---保存分类路径
         features_path---保存特征文件的路径，注意这与imagelist的不同
         dis 阈值，默认值为0.65
'''
def feature_class(imagelist,save_path,features_path,dis=0.65,suff='.bmp'):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    fr0 = open(imagelist,'r')
    line_num = fr0.readlines()
    all_num = len(line_num)
    end = all_num
    #mark 标记数组   标志序列 0表示没有比对过的，1表示已经比对过的
    mark = [0]*all_num
    file_num = 0
    
    #通过imagelist获得picture_path
    fr = open(imagelist,'r')
    line = fr.readline().strip('\n').split('.')[0]
    word = line.split('/')
    picture_path = word[0]+'/'
    for i in range(1,(len(word)-1)):
        picture_path += word[i] + '/'
    fr.close()
    
    #大循环分类
    count = 0
    for i in range(all_num):
        if mark[i] != 0:
            continue
        else:
            mark[i] = 1
            save_dir_name = '%s%s%d'%(save_path,'/',file_num)
            if not os.path.exists(save_dir_name):
                os.mkdir(save_dir_name)
            oldf_num = '%09d'%i
            oldfile_name = '%s%s%s'%(picture_path,oldf_num,suff)
        
            newfile_name = '%s%s%09d%s'%(save_dir_name,'/',0,suff)
            shutil.copyfile(oldfile_name,newfile_name)# 复制基准图像到文件夹
        
            bais_feature_num = i
            bais_feature_file = '%s%s%09d%s'%(features_path,'/',bais_feature_num,'.pkl')
            fr1 = open(bais_feature_file,'rb') 
            bais_features_data = pickle.load(fr1) #获得了基准特征数据
        
            num = 1# 每类中图片编号
            for k in range(i+1,end):
                if mark[k] != 0:
                    continue
                else:
                    feature_num = k
                    feature_file = '%s%s%09d%s'%(features_path,'/',feature_num,'.pkl')
                    fr2 = open(feature_file,'rb')
                    feature_data = pickle.load(fr2).reshape(256,1)
                    #计算相似度
                    sim = Math.dis_cos(bais_features_data,feature_data)
                    if sim < dis:
                        continue
                    else:
                        mark[k] = 1
                        oldf_num = '%09d'%k
                        oldfile_name = '%s%s%s'%(picture_path,oldf_num,suff)
                        newfile_name = '%s%s%09d%s'%(save_dir_name,'/',num,suff)
                        num += 1
                        shutil.copyfile(oldfile_name,newfile_name)
                        count += 1
                        if count%1000 == 0:
                            print u'feature_class  %d  张图片'%(count)
            file_num += 1
            fr1.close()
            fr2.close()
    print u'feature_class 已经完成，共处理%d张图片'%(count)
        
if __name__ == '__main__':
    dir_path = 'E:/practical_face/result/clean_image'
    imagelist = 'E:/practical_face/result/imagelist.txt'
    text_process.creat_imagelist_NoLabel(dir_path,imagelist)
    features_path = 'E:/practical_face/result/feature'
    save_path = 'E:/practical_face/result/feature_save'
    feature_class(imagelist,save_path,features_path)