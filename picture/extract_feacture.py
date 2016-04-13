# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:00:45 2016

@author: Administrator
"""

import cv2
import pickle

caffe_root = ''
protobuf = ''
import sys
sys.path.append(caffe_root + 'python')
sys.path.append(protobuf)
import caffe

def extract_feacture(imagelist.txt,save_path):
    caffe.set_device(0)
    caffe.set_mode_gpu()
    
    network_proto_path=''
    network_model_path=''
    layer_name = r'eltwise_fc1'
    
    net = caffe.Net(network_proto_path,network_model_path,caffe.TEST)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_raw_scale('data', 1)  # the reference model operates on images in [0,255] range instead of [0,1]

    net.blobs['data'].reshape(1,1,128,128)
    fr1 = open(file_path)
    lines1 = fr1.readlines()
    count = 0
    for i in range(len(lines1)):
        ImagePath = lines1[i].strip().split('\t')[0]
        Img = cv2.imread(ImagePath,0)
        Res = Img/256.0
        net.blobs['data'].data[0] = transformer.preprocess('data',Res)
        out = net.forward()
        feature = net.blobs[layer_name].data
        out_file = "%s%09d%s"%(save_path,i,'.pkl')
        count = i
        if count%1000 == 0:
            print u'extract_feature  %d  张图片......'%(count)
        with open(out_file,'wb') as fr2:
            pickle.dump(feature,fr2)
    fr1.close()
    print u'extract_feature 已经完成, 共%d张图片'%(count)

