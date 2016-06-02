# -*- coding: utf-8 -*-
"""
Created on Tue May 03 16:36:36 2016

@author: Administrator
"""

import cv2
import os
import copy
import random
import sys
'''
函数：Resize（）
函数功能：批量调整图片大小
输入参数：dir_path----文件库路径
         new_h，new_w----新图片的高度和宽度
'''
def Resize(dir_path,new_h,new_w):
    if not os.path.exists(dir_path):
        print u'批量调整图片大小的图片库路径不存在'
        sys.exit(0)
    dirs = os.listdir(dir_path)
    if os.path.isdir(dir_path+'/'+dirs[0]):
        for subdir in dirs:
            #print dirs
            sub_dir = dir_path + '/' + subdir
            if os.path.isdir(sub_dir):
                for files in os.listdir(sub_dir):
                    print files
                    file_path = sub_dir + '/' + files
                    img = cv2.imread(file_path)
                    shape = img.shape
                    if (int(shape[0])==new_h) and (int(shape[1])==new_w):
                        continue
                    res = cv2.resize(img,(new_h,new_w),interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(file_path,res)
    else:
        sub_dir = dir_path
        for files in os.listdir(sub_dir):
            print files
            file_path = sub_dir + '/' + files
            img = cv2.imread(file_path)
            shape = img.shape
            if (int(shape[0])==new_h) and (int(shape[1])==new_w):
                continue
            res = cv2.resize(img,(new_h,new_w),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(file_path,res)

'''
函数：DataAugmentFlip（）
函数功能：扩大数据量,主要是通过翻转
输入参数：dir_path----图片库路径
         num----一个阈值，处理文件少于num文件内的图片
         targetnum----目标数量，即打算扩充后的图片数量
'''
def DataAugmentFlip(dir_path,iLR=True,iUD=False,iDia=False,targetnum=-1,num=-1):
    if not os.path.exists(dir_path):
        print u'路径不存在'
        sys.exit(0)
    #Num = 0 #计数
    dirs = os.listdir(dir_path)
    if os.path.isdir(dir_path + '/' + dirs[0]):
        for subdir in dirs:
            sub_dir = dir_path + '/' + subdir
            files = os.listdir(sub_dir)
            fileNum = len(files)
            Num = fileNum
            if fileNum > num:
                continue
            for fr in files:
                suff = fr.split('.')[1]
                filename = sub_dir + '/' + fr
                img = cv2.imread(filename)
                size = img.shape
                res = copy.deepcopy(img)
                h = size[0]
                w = size[1]
                
                if iLR == True:
                    for i in range(h):
                        for j in range(w):
                            res[i,w-1-j]=img[i,j]
                    new_name ="%s/%s.%s"%(sub_dir,fr+'_iLR',suff)
                    cv2.imwrite(new_name,iLR)
                    Num += 1
                    if Num == targetnum:
                        return 0
                #cv2.imshow('image',iLR)
                #cv2.waitKey(0)
                if iUD == True:
                    for i in range(h):
                        for j in range(w):
                            res[h-1-i,j]=img[i,j]
                    new_name ="%s/%s.%s"%(sub_dir,fr+'_iUD',suff)
                    cv2.imwrite(new_name,res)
                    Num += 1
                    if Num == targetnum:
                        return 0
                    
                if iDia == True:
                    for i in range(h):
                        for j in range(w):
                            res[h-1-i,w-1-j]=img[i,j]
                    new_name ="%s/%s.%s"%(sub_dir,fr+'_iDia',suff)
                    cv2.imwrite(new_name,iDia)
                    Num += 1
                    if Num == targetnum:
                        return 0
                    
    else:#只针对一个文件夹
        sub_dir = dir_path
        files = os.listdir(sub_dir)
        fileNum = len(files)
        Num = fileNum
        '''
        #可选
        if fileNum > num:
            return 0
        '''
        for fr in files:
            suff = fr.split('.')
            filename = sub_dir + '/' + fr
            img = cv2.imread(filename)
            size = img.shape
            res = copy.deepcopy(img)
            h = size[0]
            w = size[1]
                
            if iLR == True:
                for i in range(h):
                    for j in range(w):
                        res[i,w-1-j]=img[i,j]
                new_name ="%s/%s.%s"%(sub_dir,suff[0]+'_iLR',suff[1])
                cv2.imwrite(new_name,res)
                Num += 1
                if Num == targetnum:
                    return 0
                    
                #cv2.imshow('image',iLR)
                #cv2.waitKey(0)
            if iUD == True:
                for i in range(h):
                    for j in range(w):
                        res[h-1-i,j]=img[i,j]
                new_name ="%s/%s.%s"%(sub_dir,suff[0]+'_iUD',suff[1])
                cv2.imwrite(new_name,res)
                Num += 1
                if Num == targetnum:
                    return 0
                    
            if iDia == True:
                for i in range(h):
                    for j in range(w):
                        res[h-1-i,w-1-j]=img[i,j]
                new_name ="%s/%s.%s"%(sub_dir,suff[0]+'_iDia',suff[1])
                cv2.imwrite(new_name,res)
                Num += 1
                if Num == targetnum:
                    return 0
                    
'''
函数：DataAugmentCrop()
函数功能：通过随机剪裁扩充数据
输入参数：picdir----图片库文件夹路径
         leftup----是否从左上角剪裁,默认
         leftdown----是否从左下角剪裁
         rightup----是否从右上角剪裁
         rightdown----是否从右下角剪裁
         new_w----剪裁后图片宽度
         new_h----剪裁后图片长度
         picnum----处理小于picnum的文件夹
         addnum----扩充数量addnum*model
         targetnum----目标数量，即打算扩充后的图片数量
'''
def DataAugmentCrop(picdir,new_w,new_h,leftup=True,leftdown=False,\
                    rightup=False,rightdown=False,addnum=1,targetnum=-1,picnum=-1):
    if not os.path.exists(picdir):
        print u'图片库文件夹路径不存在！'
        sys.exit(0)
    #Num = 0 #计算
    dirs = os.listdir(picdir)
    if os.path.isdir(picdir+'/'+dirs[0]):
        for sub in dirs:
            subdir = picdir+'/'+sub
            files = os.listdir(subdir)
            Num = len(files)
            if len(files) >= picnum:
                continue
            for fr in files:
                filename = subdir+'/'+fr
                #第一步，先将图片缩放到new_h*new_w，保存下来
                img = cv2.imread(filename)
                size = img.shape 
                if size[0] != new_h or size[1] != new_w:
                    img0 = cv2.resize(img,(new_h,new_w),interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(filename,img0)
                #第二步，重新读取该图片,把该图片缩放到new_h+16,new_w+16
                img = cv2.imread(filename)
                size = img.shape
                '''
                if size[0]<=(new_h+5) or size[1]<=(new_w+5):
                    img1 = cv2.resize(img,(new_w+16,new_h+16),\
                                        interpolation=cv2.INTER_CUBIC)
                    size=img1.shape
                else:
                    img1 = img
                '''
                img1 = cv2.resize(img,(new_w+16,new_h+16),interpolation=cv2.INTER_CUBIC)
                size = img1.shape
                
                if leftup == True:
                    for i in range(addnum):
                        xpoint = random.randint(0,size[1]-new_w)
                        ypoint = random.randint(0,size[0]-new_h)
                        res = img1[ypoint:ypoint+new_h,xpoint:xpoint+new_w,:]
                        suff = fr.split('.')
                        outname="%s%d.%s"%(subdir+'/'+suff[0]+'_leftup_',i,suff[1])
                        cv2.imwrite(outname,res)
                        Num += 1
                        if Num == targetnum:
                            return 0
                        
                if leftdown == True:
                    for i in range(addnum):
                        xpoint = random.randint(0,size[1]-new_w)
                        ypoint = random.randint(new_h,size[0])
                        res = img1[ypoint-new_h:ypoint,xpoint:xpoint+new_w,:]
                        suff = fr.split('.')
                        outname="%s%d.%s"%(subdir+'/'+suff[0]+'_leftdown_',i,suff[1])
                        cv2.imwrite(outname,res)
                        Num += 1
                        if Num == targetnum:
                            return 0
                        
                if rightup == True:
                    for i in range(addnum):
                        xpoint = random.randint(new_w,size[1])
                        ypoint = random.randint(0,size[0]-new_h)
                        res = img1[ypoint:ypoint+new_h,xpoint-new_w:xpoint,:]
                        suff = fr.split('.')
                        outname="%s%d.%s"%(subdir+'/'+suff[0]+'_rightup_',i,suff[1])
                        cv2.imwrite(outname,res)
                        Num += 1
                        if Num == targetnum:
                            return 0
                        
                if rightdown == True:
                    for i in range(addnum):
                        xpoint = random.randint(new_w,size[1])
                        ypoint = random.randint(new_h,size[0])
                        res = img1[ypoint-new_h:ypoint,xpoint-new_w:xpoint,:]
                        suff = fr.split('.')
                        outname="%s%d.%s"%(subdir+'/'+suff[0]+'_rightdown_',i,suff[1])
                        cv2.imwrite(outname,res)
                        Num += 1
                        if Num == targetnum:
                            return 0
                        
    else:#只针对一个文件夹
        subdir = picdir
        files = os.listdir(subdir)
        Num = len(files)
        '''
        #可选
        if len(files) > picnum:
            return 0
        '''
        for fr in files:
            filename = subdir+'/'+fr
            #第一步，先将图片缩放到new_h*new_w，保存下来
            img = cv2.imread(filename)
            size = img.shape 
            if size[0] != new_h or size[1] != new_w:
                img0 = cv2.resize(img,(new_h,new_w),interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(filename,img0)
                #第二步，重新读取该图片,把该图片缩放到new_h+16,new_w+16
            img = cv2.imread(filename)
            size = img.shape
            '''
            if size[0]<=(new_h+5) or size[1]<=(new_w+5):
                img1 = cv2.resize(img,(new_w+16,new_h+16),\
                                        interpolation=cv2.INTER_CUBIC)
                size=img1.shape
            else:
                img1 = img
            '''
            img1 = cv2.resize(img,(new_w+16,new_h+16),interpolation=cv2.INTER_CUBIC)
            size = img1.shape
            if leftup == True:
                for i in range(addnum):
                    xpoint = random.randint(0,size[1]-new_w)
                    ypoint = random.randint(0,size[0]-new_h)
                    res = img1[ypoint:ypoint+new_h,xpoint:xpoint+new_w,:]
                    suff = fr.split('.')
                    outname="%s%d.%s"%(subdir+'/'+suff[0]+'_leftup_',i,suff[1])
                    cv2.imwrite(outname,res)
                    Num += 1
                    if Num == targetnum:
                        return 0
                        
            if leftdown == True:
                for i in range(addnum):
                    xpoint = random.randint(0,size[1]-new_w)
                    ypoint = random.randint(new_h,size[0])
                    res = img1[ypoint-new_h:ypoint,xpoint:xpoint+new_w,:]
                    suff = fr.split('.')
                    outname="%s%d.%s"%(subdir+'/'+suff[0]+'_leftdown_',i,suff[1])
                    cv2.imwrite(outname,res)
                    Num += 1
                    if Num == targetnum:
                        return 0
                        
            if rightup == True:
                for i in range(addnum):
                    xpoint = random.randint(new_w,size[1])
                    ypoint = random.randint(0,size[0]-new_h)
                    res = img1[ypoint:ypoint+new_h,xpoint-new_w:xpoint,:]
                    suff = fr.split('.')
                    outname="%s%d.%s"%(subdir+'/'+suff[0]+'_rightup_',i,suff[1])
                    cv2.imwrite(outname,res)
                    Num += 1
                    if Num == targetnum:
                        return 0
                        
            if rightdown == True:
                for i in range(addnum):
                    xpoint = random.randint(new_w,size[1])
                    ypoint = random.randint(new_h,size[0])
                    res = img1[ypoint-new_h:ypoint,xpoint-new_w:xpoint,:]
                    suff = fr.split('.')
                    outname="%s%d.%s"%(subdir+'/'+suff[0]+'_rightdown_',i,suff[1])
                    cv2.imwrite(outname,res)
                    Num += 1
                    if Num == targetnum:
                        return 0
                        

'''
函数:ReduceData()
函数：如果文件中的图片数量多于num，则随机选择num
输入参数：dirpath----图片库路径
         num----数量阈值
'''
def ReduceData(dirpath,num):
    if not os.path.exists(dirpath):
        print u'ReduceData  输入数据库路径不存在'
        sys.exit(0)
    dirs = os.listdir(dirpath)
    if os.path.isdir(dirpath+'/'+dirs[0]):
        for sub in dirs:
            subdir = dirpath+'/'+sub
            files = os.listdir(subdir)
            filenum = len(files)
            if filenum>num:
                subfiles = random.sample(files,filenum-num)
                for fr in subfiles:
                    filename = subdir+'/'+fr
                    os.remove(filename)
    else:#针对一个文件夹
        subdir = dirpath
        files = os.listdir(subdir)
        filenum = len(files)
        if filenum>num:
            subfiles = random.sample(files,filenum-num)
            for fr in subfiles:
                filename = subdir+'/'+fr
                os.remove(filename)

'''
函数：DataBalance（）
函数功能：平衡数据集，但只是粗略的并不能十分精确
输入参数：dirpath----数据集路径
         baisnum----基准数，就是想要的平均数，这里要说明一下，我做的只是少量数据的扩充
         因此大于baisnum的文件夹并没有处理,最好的2的倍数
		 new_h----处理后图片高度
		 new_w----处理后图片宽度
'''
def DataBalance(dirpath,basinum,new_w,new_h):
    if not os.path.exists(dirpath):
        print u'数据集路径不存在'
        sys.exit(0)
    dirs = os.listdir(dirpath)
    for sub in dirs:
        subdir = dirpath+'/'+sub
        files = os.listdir(subdir)
        Lfile = len(files)
        if Lfile == basinum:
            continue
        elif Lfile > basinum:
            #continue
            ReduceData(subdir,basinum)
            Resize(subdir,new_h,new_w)
        
        #如果basinum/Lfile=<2,则图片数量在basinum/2~basinum之间
        #因此只水平翻转就能达到目的
        elif basinum/Lfile <= 2:
            DataAugmentFlip(subdir,targetnum=basinum)
        
        #如果basinum/Lfile =<8,则翻转一次，在从四角随机剪裁
        elif 2< basinum/Lfile <= 8:
            DataAugmentFlip(subdir)
            Resize(subdir,new_h,new_w)
            DataAugmentCrop(subdir,new_w,new_h,True,True,True,True,targetnum=basinum)
        
        #如果basinum/Lfile > 8
        elif basinum/Lfile > 8:
            addnum = (basinum/Lfile)/2/4 + 1
            DataAugmentFlip(subdir)
            Resize(subdir,new_h,new_w)
            DataAugmentCrop(subdir,new_w,new_h,True,True,True,True,addnum,targetnum=basinum)
        
    print u'处理完毕'

'''
函数：GaussDataBalance()
函数功能：使数据呈现高斯分布
输入的参数：dirpath----数据集路径
           model-----选择数据呈现的分布类型，默认是高斯分布gauss
           其他类型暂时未加
           new_h----处理后图片高度
           new_w----处理后图片宽度
           mu----高斯分布的均值，这里不能是0，
           std----高斯分布方差，建议5，如果为1，其实相差不大 
'''
def GaussDataBalance(dirpath,new_w,new_h,mu,std=5,model='gauss'):
    if not os.path.exists(dirpath):
        print u'数据库路径不存在！'
        sys.exit(0)
    dirs = os.listdir(dirpath)
    numlist = []
    #产生一个高斯分布序列
    if model == 'gauss':
        for i in range(len(dirs)):
            N = random.gauss(mu,std)
            n = round(N,0)
            #print n
            numlist.append(int(n))
    
    Num = 0 #处理第Num个文件夹
    for sub in dirs:
        basinum = numlist[Num]
        if basinum <= 0:
            basinum = 1
        subdir = dirpath+'/'+sub
        files = os.listdir(subdir)
        Lfile = len(files)
        if Lfile == basinum:
            continue
        elif Lfile > basinum:
            #continue
            ReduceData(subdir,basinum)
            Resize(subdir,new_h,new_w)
        
        #如果basinum/Lfile=<2,则图片数量在basinum/2~basinum之间
        #因此只水平翻转就能达到目的
        elif basinum/Lfile <= 2:
            DataAugmentFlip(subdir,targetnum=basinum)
        
        #如果basinum/Lfile =<8,则翻转一次，在从四角随机剪裁
        elif 2< basinum/Lfile <= 8:
            DataAugmentFlip(subdir)
            Resize(subdir,new_h,new_w)
            DataAugmentCrop(subdir,new_w,new_h,True,True,True,True,targetnum=basinum)
        
        #如果basinum/Lfile > 8
        elif basinum/Lfile > 8:
            addnum = (basinum/Lfile)/2/4 + 1
            DataAugmentFlip(subdir)
            Resize(subdir,new_h,new_w)
            DataAugmentCrop(subdir,new_w,new_h,True,True,True,True,addnum,targetnum=basinum)
        
    print u'处理完毕'

if __name__=='__main__':
    dir_path = 'E:/Face_data/FaceImages'
    new_h = 144
    new_w = 144
    #Resize(dir_path,new_h,new_w)
    #DataAugment(dir_path,61)
    #DataAugmentCrop(dir_path,20,144,144,True,True,True,True,60)
    #DataBalance(dir_path,40)
    #ReduceData(dir_path,4)
    GaussDataBalance(dir_path,144,144,50)
    