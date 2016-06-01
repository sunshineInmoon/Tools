# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 15:09:24 2016

@author: Administrator
"""

import os
import text_process
import SplitDataTo_Train_Test

'''
函数：DataToTrain()
功能：从预处理后的数据集到训练前数据的处理，包括数据的分离，转换caffe数据格式
    计算平均值
输入参数：dir_path----预处理后的数据，一般是保存文件的问价夹
         out_path----处理后保存文件夹和文件的路径
         Format----转换后的数据格式默认leveldb
         command----命令行
'''
def DataToTrain(dir_path,out_path,command,Format='leveldb',parencent=0.1):
    #第一步，分离数据
   print u'第一步，分离数据----开始'
   train_data = out_path + '/' + 'train_data'
   if not os.path.exists(train_data):
       os.mkdir(train_data)
   test_data = out_path + '/' + 'test_data'
   if not os.path.exists(test_data):
       os.mkdir(test_data)
   SplitDataTo_Train_Test.SplitData(dir_path,train_data,test_data,parencent)
   print u'第一步，分离数据----结束。'
   #第二步，转换数据格式
   print u'第二步，转换数据格式----开始'
   train_imagelist = out_path + '/' + 'train_imagelist.txt'
   text_process.CreatImageListWithLabel(train_data,train_imagelist)
   train = out_path + '/' + 'train_' + Format
   command_train = "%s %s %s %s %s"%('convert_imageset.exe',command,train_data,\
   train_imagelist,train)
   print command_train
   os.system(command_train)
   
   test_imagelist = out_path + '/' + 'test_imagelist.txt'
   text_process.CreatImageListWithLabel(test_data,test_imagelist)
   test = out_path + '/' + 'test_' + Format
   command_test = "%s %s %s %s %s"%('convert_imageset.exe',command,test_data,\
   test_imagelist,test)
   print command_test
   os.system(command_test)
   print u'第二步，转换数据格式----结束'
   #第三步，计算平均值
   print u'第三步，计算平均值----开始'
   train_mean = out_path + '/' + 'train_mean.binaryproto'
   command_train_mean = "%s %s%s %s %s"%('compute_image_mean.exe','--backend=',Format,train,train_mean)
   print command_train_mean
   os.system(command_train_mean)
   
   test_mean = out_path + '/' + 'test_mean.binaryproto'
   command_test_mean = "%s %s%s %s %s"%('compute_image_mean.exe','--backend=',Format,test,test_mean)
   os.system(command_test_mean)
   print u'第三步，计算平均值----结束'
if __name__ == '__main__':
    dir_path = 'E:/practical_face/LogPhoto'
    out_path = 'E:/practical_face'
    command = '--backend=leveldb --gray=true --shuffle=ture'
    command = '--backend=leveldb --gray=true --shuffle=ture --resize_height=144 --resize_width=144'
    DataToTrain(dir_path,out_path,command)