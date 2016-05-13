# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:03:16 2016

@author: Sun
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

import sys
caffe_root = 'F:/caffe-Microsoft/Build/x64/Release/pycaffe'
#caffe_root = 'F:/caffe-windows/caffe/caffe-windows-master/python'
sys.path.insert(0,caffe_root)
import caffe

#初始化网络
def Init_net(network_proto_path,network_model_path,ImagePath):
    caffe.set_mode_cpu()
    net = caffe.Net(network_proto_path, network_model_path, caffe.TEST)
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_raw_scale('data', 1)  # the reference model operates on images in [0,255] range instead of [0,1]
#    transformer.set_mean('data', None)
    net.blobs['data'].reshape(1,3,128,128)
    img = cv2.imread(ImagePath)
    plt.imshow(img)
    shape0 = img.shape
    if shape0[0]!=128 and shape0[1]!=128:
        img = cv2.resize(img,(128,128))
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #plt.imshow(gray)
    #gray = gray / 256.0
    net.blobs['data'].data[...] = transformer.preprocess('data', gray)
    out = net.forward()
    return net,transformer

'''
函数：vis_square()
函数功能：一个显示辅助函数
输入参数：data
        out----保存图片的路径
'''
def vis_square(data,isLayer='False',out='None'):
    #normalize data for display
    data = (data - data.min()) / (data.max() - data.min())
    #force the number of filters to be square
    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = (((0, n ** 2 - data.shape[0]),
               (0, 1), (0, 1))                 # add some space between filters
               + ((0, 0),) * (data.ndim - 3))  # don't pad the last dimension (if there is one)
    data = np.pad(data, padding, mode='constant', constant_values=1)  # pad with ones (white)
    
    # tile the filters into an image
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
    
    #plt.savefig()
    if isLayer == 'True':
        cv2.imshow('image',data)
        cv2.waitKey(0)
        cv2.destroyWindow('image')
    else:
        cv2.imwrite(out,data*255)
    #plt.imshow(data)
    #plt.axis('off')

'''
函数：VisualWeights()
函数功能：根据层名字显示相应的权重
输入参数：layer_name----层名字
         net----初始化后的网络
         out----保存图片的路径
'''
def VisualWeights(net,out):
    #显示各个层的shape
    # the parameters are a list of [weights, biases]
    sub_dir = out + '/' + 'Weights'
    if not os.path.exists(sub_dir):
        os.mkdir(sub_dir)
    for layer_name,param in net.params.iteritems():
        out_name = sub_dir + '/' + layer_name + '.jpg'
        filters = net.params[layer_name][0].data
        vis_square(filters.transpose(0,2,3,1),out_name)

'''
函数：VisualWeight()
函数功能：根据层名字显示相应的权重
输入参数：layer_name----层名字
         net----初始化后的网络
'''
def VisualWeight(net,layer_name):
    filters = net.params[layer_name][0].data
    vis_square(filters.transpose(0,2,3,1),'True')

'''
函数：VisualBlob()
函数功能：可视化Blob
输入参数：net----初始化后的网络
         layer_name----层的名字
'''
def VisualBlob(net,layer_name):
    feat = net.blobs[layer_name].data[0,]
    vis_square(feat,'True')

'''
函数：VisualBlobs()
函数功能：保存所有Blobs
输入参数：net----初始化后的网络
         out----保存路径
'''
def VisualBlobs(net,out):
    sub_dir = out + '/' + 'Blobs'
    if not os.path.exists(sub_dir):
        os.mkdir(sub_dir)
    for layer_name,blob in net.blobs.iteritems():
        out_name = sub_dir + '/' + layer_name + '.jpg'
        feat = net.blobs['conv1'].data[0,]
        vis_square(feat,out_name)

'''
函数：VisualLayerShape()
函数：显示层的名字和形状
输入参数：net----初始化后的网络
'''
def VisualLayerShape():
    #显示各个层的shape
    for layer_name1,blob in net.blobs.iteritems():
        print layer_name1 + '\t' + str(blob.data.shape)

'''
函数：VisualLayerWeightShape()
函数功能：显示各层权重的形状
输入参数：net----初始化后的网络
'''
def VisualLayerWeightShape(net):
    #显示各个层权重的形状
    #权重的形状（(output_channels, input_channels, filter_height, filter_width)）
    #param[0]=weights  param[1]=biases
    for layer_name,param in net.params.iteritems():
        print layer_name + '\t' + str(param[0].data.shape),str(param[1].data.shape)

if __name__=='__main__':
    network_proto_path = r'F:/Net_train.prototxt'
    network_model_path = r'F:/Net_iter_800000.caffemodel'
    ImagePath = 'E:/Face_data/FaceImages/0/000000000.bmp'
    net,transformer = Init_net(network_proto_path,network_model_path,ImagePath)
    #net.params
    layer_name = r'fc1'
    VisualLayerShape()
    #VisualWeights(net,'F:/Weights')
    #VisualWeight(net,'conv2a')
    #VisualLayerWeightShape(net)
    VisualBlob(net,'conv1')
    VisualBlobs(net,out='F:/OUT')