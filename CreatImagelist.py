# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:44:22 2016

@author: Administrator
"""


import os
import sys

def creat_imagelist_NoLabel(dir_path,imagelist_path):
    fr = open(imagelist_path,'w')
    count = 0
    for dirpath,dirnames,filenames in os.walk(dir_path):
        for files in filenames:
            image_path = dir_path + '/' + files + '\n'
            fr.write(image_path)
            count += 1
    fr.close()
    print u'creat_imageslist_NoLabel 完成，共%d张图片'%(count)
    
if __name__=='__main__':
    dir_path = 'E:/wu_test/color/picture3'
    imagelist_path = 'E:/wu_test/color/picture3.txt'
    #dir_path = sys.argv[1]
    #imagelist_path = sys.argv[2]
    creat_imagelist_NoLabel(dir_path,imagelist_path)