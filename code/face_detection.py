# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:19:25 2016

@author: Administrator
"""

import os

def face_detection(imagelist,bboxlist):
    os.system('face_detection.exe '+imagelist+' '+bboxlist)
    
if __name__ == '__main__':
    imagelist = 'E:/practical_face/result/imagelist.txt'
    bboxlist = 'E:/practical_face/result/clean_imagelist.txt'
    face_detection(imagelist,bboxlist)