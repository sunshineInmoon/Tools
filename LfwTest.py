# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:33:58 2015

@author: Administrator
"""

import time
import math
import numpy as np
import scipy.io as sio
import os
import cv2
import copy
import sklearn.metrics.pairwise as pw
import matplotlib.pyplot as plt

import sys
caffe_root = 'F:/caffe-Microsoft/Build/x64/Release/pycaffe' 
sys.path.insert(0, caffe_root)
#sys.path.append('D:/Documents/Downloads/protobuf-2.5.0/protobuf-2.5.0/python/')
import caffe

def cos_dist(a, b):
    if len(a) != len(b):
        return None
    part_up = 0.0
    a_sq = 0.0
    b_sq = 0.0
    for a1, b1 in zip(a,b):
        part_up += a1*b1
        a_sq += a1**2
        b_sq += b1**2
    part_down = math.sqrt(a_sq*b_sq)
    if part_down == 0.0:
        return None
    else:
        return part_up / part_down

def dis_cos(a,b):
    sum0 = np.dot(a,b)
    sum1 = np.sqrt(np.sum(np.power(a,2)))
    sum2 = np.sqrt(np.sum(np.power(b,2)))
    return sum0/(sum1*sum2)

#初始化网络
def Init_net(network_proto_path,network_model_path):
    caffe.set_mode_cpu()
    net = caffe.Net(network_proto_path, network_model_path, caffe.TEST)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_raw_scale('data', 1)  # the reference model operates on images in [0,255] range instead of [0,1]
#    transformer.set_mean('data', None)
    return net,transformer


def extract_feature(net,transformer,ImagePath1, ImagePath2,layer_name, image_as_grey = False):
    """
    Extracts features for given model and image list.

    Input
    network_proto_path: network definition file, in prototxt format.
    network_model_path: trainded network model file
    image_list: A list contains paths of all images, which will be fed into the
                network and their features would be saved.
    layer_name: The name of layer whose output would be extracted.
    save_path: The file path of extracted features to be saved.
    """
    net.blobs['data'].reshape(2,3,128,128)
    img = cv2.imread(ImagePath1)
    img1 = cv2.imread(ImagePath2)
    shape0 = img.shape
    shape1 = img1.shape
    if shape0[0]!=128 and shape0[1]!=128:
        cv2.resize(img,(128,128))
    if shape1[0]!=128 and shape1[1]!=128:
        cv2.resize(img1,(128,128))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    
    gray = gray / 256.0
    gray1 = gray1 / 256.0
    ImageBatch= []
    ImageBatch.append(gray)
    ImageBatch.append(gray)
    net.blobs['data'].data[0] = transformer.preprocess('data', gray)
    net.blobs['data'].data[1] = transformer.preprocess('data', gray1)

    out = net.forward()
    a = net.blobs[layer_name].data[0].copy()
    b = net.blobs[layer_name].data[1].copy()

    #b = b.reshape(256,1)
    #dst = dis_cos(a,b)
    dst = pw.paired_distances(a,b,'cosine')
    #b = b.reshape(256,1)
    #dst = dis_cos(a,b)
    #print 'dst0:',dst0,'     dst:',dst
    return 1-dst

if __name__ == "__main__":
    network_proto_path = r'F:/Net_train.prototxt'
    network_model_path = r'F:/Net_iter_800000.caffemodel'
    layer_name = r'fc1'
    theat = [0.25,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.20]
    #初试化网络
    net,transformer = Init_net(network_proto_path,network_model_path)
    Res=[]
    for k in range(1):
        fr1 = open('E:/Face_data/left_1.txt')
        fr2 = open('E:/Face_data/right_1.txt')
        fr3 = open('E:/Face_data/label_1.txt')
        fr4 = open('E:/Face_data/result_my_2.txt','w')
        fr5 = open('E:/Face_data/error.txt','w')
        lines1 = fr1.readlines()
        lines2 = fr2.readlines()
        lines3 = fr3.readlines()
        result=0
        num = 0.0
        re=0
        dist = []
        pos = []
        neg = []
        err = []
        for i in range(len(lines1)):
            ImagePath1 = lines1[i].strip().split()
            ImagePath2 = lines2[i].strip().split()
            label = lines3[i].strip().split()
            if not os.path.exists(ImagePath1[0]):
                continue
            if not os.path.exists(ImagePath2[0]):
                continue
            dst = extract_feature(net,transformer,ImagePath1[0],ImagePath2[0],layer_name)
            d = copy.deepcopy(dst)
            dist.append(dst)
        #print "第%d个样本，相似度: %f" %(num,dst)
        
            if int(label[0]) == 1:
                pos.append(dst)
                str1 = "第%d个样本，正样本，相似度: %f" %(num,dst)
                fr4.write(str1+'\n')
                print str1
            else:
                neg.append(dst)
                str2 = "第%d个样本，负样本，相似度: %f" %(num,dst)
                fr4.write(str2 + '\n')
                print str2
            
            if dst >= theat[k]:
                re = 1
            else:
                re = 0
            
            if re == int(label[0]):
                result += 1
            else:
                err.append(dst)
                str3="第%d个样本，相似度：%f \n路径1：%s\n路径:2：%s"%(num,dst,ImagePath1[0],ImagePath2[0])
                fr5.write(str3+'\n\n')
            num += 1
        print theat[k],u'     准确度：',(result/num)
        Res.append(result/num)
    
    fr1.close()
    fr2.close()
    fr3.close()
    fr4.close()
    fr5.close()
    
