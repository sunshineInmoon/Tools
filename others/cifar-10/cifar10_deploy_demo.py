# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:38:15 2015

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt


# Make sure that caffe is on the python path:
caffe_root = 'E:/DeepLearning/caffe/caffe-windows-master/'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.append('F:/caffe-Microsoft/Build/x64/Release/pycaffe')
sys.path.append('D:/Anaconda/Lib/site-packages/')
#sys.path.append('D:/Documents/Downloads/protobuf-2.5.0/protobuf-2.5.0/python/')
import caffe
print ("Right1")

#plt.rcParams['figure.figsize'] = (10, 10)
#plt.rcParams['image.interpolation'] = 'nearest'
#plt.rcParams['image.cmap'] = 'gray'

#对平均值文件处理，转换成npy格式
blob =caffe.proto.caffe_pb2.BlobProto()
data=open("trainmean.binaryproto",'rb').read()
blob.ParseFromString(data)
arr=np.array(caffe.io.blobproto_to_array(blob))
out=arr[0]
np.save("cifar10_mean.npy",out)

caffe.set_mode_cpu()
net = caffe.Net('D:/DesktopDocuments/caffe_test/cifar-10/cifar10_deploy.prototxt',
                'D:/DesktopDocuments/caffe_test/cifar-10/cifar10_quick_iter_4000.caffemodel',
                caffe.TEST)

# input preprocessing: 'data' is the name of the input blob == net.inputs[0]
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_mean('data', np.load('cifar10_mean.npy').mean(1).mean(1)) # mean pixel
transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB

# set net to batch size of 50
net.blobs['data'].reshape(1,3,32,32)

net.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image('D:/DesktopDocuments/caffe_test/cifar-10/airplane.jpg'))
out = net.forward()
print("Predicted class is #{}.".format(out['prob'].argmax()))

print '0'
plt.imshow(transformer.deprocess('data', net.blobs['data'].data[0]))
print '1'

# load labels
#imagenet_labels_filename = caffe_root + 'data/ilsvrc12/synset_words.txt'
#labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

# sort top k predictions from softmax output
#top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
#print labels[top_k]