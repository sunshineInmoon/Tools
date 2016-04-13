# -*- coding: utf-8 -*-
"""
Created on Fri Apr 01 10:00:47 2016

@author: Administrator
"""

import numpy as np

#距离计算
def dis_cos(a,b):
    sum0 = np.dot(a,b)
    #print 'sum0:',sum0
    sum1 = np.sqrt(np.sum(np.power(a,2)))
    #print 'sum1:',sum1
    sum2 = np.sqrt(np.sum(np.power(b,2)))
    #print 'sum2',sum2
    return sum0/(sum1*sum2)
    
#取两个数的最大值
def Min(a,b):
    if a<=b:
        return a
    else:
        return b