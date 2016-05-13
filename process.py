# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:03:58 2016

@author: Sun
"""
import os
import shutil
import random
import numpy as np
from operator import itemgetter,attrgetter
'''
函数：renamedir（）
函数功能：重命名文件夹，按一定顺序
输入参数：dir_path----包含子文件夹的路径
         start   ----开始序号
'''
def Renamedir(dir_path,start):
    #print os.listdir(dir_path)
    end = start
    dirs = os.listdir(dir_path)
    for dir_name in dirs:
        old_name = dir_path + '/' + dir_name
        new_name = "%s/%d"%(dir_path,end)
        if old_name == new_name:
            continue
        else:
            os.rename(old_name,new_name)
            end += 1
    print u'文件夹重命名结束，共处理%d个文件夹'%(end-start)
    
'''
函数：Rmovedir（）
函数功能：删除文件夹中文件少于一定数量的文件夹
输入参数：dir_path----包含子文件夹的路径
         num----阈值，将文件数量小于等于num的文件夹删掉
'''
def Rmovedir(dir_path,num):
    dirs = os.listdir(dir_path)
    start = len(dirs)
    end = 0
    for name in dirs:
        dir_name = dir_path + '/' + name
        count = len(os.listdir(dir_name))
        #print count
        if count<=num:
            shutil.rmtree(dir_name)
            end += 1
    print u'删减前文件数量%d,删减后文件夹数量%d，共删减%d个文件夹'%(start,start-end,end)
    
    
'''
函数： Romvepath（）
函数功能：删除一个imagelist中不存在的路径
输入参数：inputlist,outputlist
'''
def Rmovepath(inputlist,outlist):
    fr_in = open(inputlist,'r')
    fr_out = open(outlist,'w')
    lines = fr_in.readlines()
    start = len(lines)
    end = 0
    for line in lines:
        curline = line.strip('\n')
        if os.path.exists(curline):
            fr_out.write(curline+'\n')
        else:
            end += 1
    fr_in.close()
    fr_out.close()
    print u'Romvepath()已经完成，共删除%d路径，保留%d路径 '%(end,start-end)
    
    
'''
函数：Rmovepath_pair()
函数功能：成对删除文件中不存在的路径
输入参数：input1,input2,inlabel,output1,output2,outlabel
'''
def Rmovepath_pair(input1,input2,inlabel,output1,output2,outlabel):
    fr_in1 = open(input1,'r')
    fr_in2 = open(input2,'r')
    fr_l = open(inlabel,'r')
    fr_out1 = open(output1,'w')
    fr_out2 = open(output2,'w')
    fr_outl = open(outlabel,'w')
    lines1 = fr_in1.readlines()
    lines2 = fr_in2.readlines()
    lines3 = fr_l.readlines()
    start = len(lines1)
    end = 0
    for i in range(start):
        curline = lines1[i].strip('\n')
        if os.path.exists(curline):
            fr_out1.write(curline+'\n')
            fr_out2.write(lines2[i])
            fr_outl.write(lines3[i])
        else:
            end += 1
    fr_in1.close()
    fr_in2.close()
    fr_l.close()
    fr_out1.close()
    fr_out2.close()
    fr_outl.close()
    print u'Romvepath_path()已经完成，共删除%d路径，保留%d路径 '%(end,start-end)
    
    
    
'''
函数：TestPair（）
函数功能：从数据库中挑选正负样本
输入参数：dir_path----存放图片库路径
         class_num----类别数量
         neg_num----负样本数
         pos_num----正样本数
         leftlist
         rightlist
         label
'''
def TestPair(dir_path,class_num,leftlist,rightlist,label,pos_num=3000,neg_num=3000):
    left = open(leftlist,'w')
    right = open(rightlist,'w')
    label = open(label,'w')
    
    dirs = os.listdir(dir_path)
    #print dirs[23]
    #第一步，产生负样本
    
    print u'产生负样本'
    for i in range(neg_num):
        #随机选取两个不同的文件夹
        sample1 = random.randint(0,class_num-1)
        sample2 = random.randint(0,class_num-1)
        while(sample1 == sample2):
            sample2 = random.randint(0,class_num-1)
        sub_dir1 = dir_path + '/' + dirs[sample1]
        sub_dir2 = dir_path + '/' + dirs[sample2]
        files1 = os.listdir(sub_dir1)
        files2 = os.listdir(sub_dir2)
        l1 = len(files1)
        l2 = len(files2)
        #随机选取两个文件
        f1 = random.randint(0,l1-1)
        f2 = random.randint(0,l2-1)
        files1_path = sub_dir1 + '/' + files1[f1]
        files2_path = sub_dir2 + '/' + files2[f2]
        #print files1_path,files2_path
        left.write(files1_path+'\n')
        right.write(files2_path+'\n')
        label.write('0'+'\n')
        print i
        #print 'l1:',l1,'    l2:',l2
    
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
    
    
'''
函数：Select_K_MaxMin()
函数功能：输出文件夹中图片数量最多或最小的前K个文件夹路径
输入参数：dir_path----图片库路径
         model----选择最大还是最小默认
         K----前K个
'''
'''
def Select_K_MaxMin(dir_path,k=1,model='All'):
    if not os.path.exists(dir_path):
        print u'路径不存在！'
    else:
        label=[]
        fileNum=[]
        dirs = os.listdir(dir_path)
        for subdir in dirs:
            sub_dir = dir_path + '/' + subdir
            files = os.listdir(sub_dir)
            fileNum.append(len(files))
        if model=='Max':
            for i in range(k):
                Max_label = np.argmax(fileNum)
                #print Max_label
                label.append(Max_label)
                dir_name = dir_path + '/' + dirs[Max_label]
                print '图片数：%d, 文件夹路径：%s'%(fileNum[Max_label],dir_name)
                del fileNum[Max_label]
        if model=='Min':
            for i in range(k):
                Min_label = np.argmin(fileNum)
                label.append(Min_label)
                dir_name = dir_path + '/' + dirs[Min_label]
                print '图片数：%d, 文件夹路径：%s'%(fileNum[Min_label],dir_name)
                del fileNum[Min_label]
        if model=='All':
            print 'Max'
            for i in range(k):
                Max_label = np.argmax(fileNum)
                label.append(Max_label)
                dir_name = dir_path + '/' + dirs[Max_label]
                print '图片数：%d, 文件夹路径：%s'%(fileNum[Max_label],dir_name)
                del fileNum[Max_label]
            print 'Min'
            for i in range(k):
                Min_label = np.argmin(fileNum)
                label.append(Min_label)
                dir_name = dir_path + '/' + dirs[Min_label]
                print '图片数：%d, 文件夹路径：%s'%(fileNum[Min_label],dir_name)
                del fileNum[Min_label]
'''
'''
函数：Select_K_MaxMin()
函数功能：输出文件夹中图片数量最多或最小的前K个文件夹路径
输入参数：dir_path----图片库路径
         model----选择最大还是最小默认
         K----前K个
'''
def Select_K_MaxMin(dir_path,k=1,model='All'):
    if not os.path.exists(dir_path):
        print u'路径不存在！'
    else:
        label=[]
        fileNum=[]
        result=[]
        dirs = os.listdir(dir_path)
        for subdir in dirs:
            sub_dir = dir_path + '/' + subdir
            files = os.listdir(sub_dir)
            fileNum.append(len(files))
            result.append((len(files),sub_dir))
        if model=='Max':
            print 'Max'
            Maxlist = sorted(result,key=itemgetter(0),reverse=True)
            for i in range(k):
                print '图片数：%d，文件夹路径：%s'%(Maxlist[i][0],Maxlist[i][1])
                
        if model=='Min':
            print 'Min'
            Minlist = sorted(result,key=itemgetter(0))
            for i in range(k):
                print '图片数：%d，文件夹路径：%s'%(Minlist[i][0],Minlist[i][1])
        
        if model=='All':
            print 'Max'
            Maxlist = sorted(result,key=itemgetter(0),reverse=True)
            for i in range(k):
                print '图片数：%d，文件夹路径：%s'%(Maxlist[i][0],Maxlist[i][1])
            print 'Min'
            Minlist = sorted(result,key=itemgetter(0))
            for i in range(k):
                print '图片数：%d，文件夹路径：%s'%(Minlist[i][0],Minlist[i][1])
if __name__=='__main__':
    Rmovedir('E:/Face_data/FaceImages5',5)
    Renamedir('E:/Face_data/FaceImages5',2001)
    Renamedir('E:/Face_data/FaceImages5',0)
    '''
Rmovepath_pair('D:/Documents/Downloads/DeepFace-master/FaceRecongnition/deepid/filelist_lfw/filelist_left.list',\
'D:/Documents/Downloads/DeepFace-master/FaceRecongnition/deepid/filelist_lfw/filelist_right.list',\
'D:/Documents/Downloads/DeepFace-master/FaceRecongnition/deepid/filelist_lfw/filelist_label.list',\
'D:/Documents/Downloads/DeepFace-master/FaceRecongnition/deepid/filelist_lfw/lfw_left.list',\
'D:/Documents/Downloads/DeepFace-master/FaceRecongnition/deepid/filelist_lfw/lfw_right.list',\
'D:/Documents/Downloads/DeepFace-master/FaceRecongnition/deepid/filelist_lfw/label.list')
    '''
    
    '''
    TestPair('E:/Face_data/FaceImages4',541,'E:/Face_data/left_1.txt','E:/Face_data/right_1.txt',\
        'E:/Face_data/label_1.txt')
    '''
    Select_K_MaxMin('E:/Face_data/FaceImages5',5,'All')