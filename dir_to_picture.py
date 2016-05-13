# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:31:11 2016

@author: Administrator
"""

import shutil
import sys

def dir_to_picture(file_path,save_path):
    fr1 = open(file_path)
    lines = fr1.readlines()
    for i in range(len(lines)):
        old_name = lines[i].strip().split()[0]
        file_num = '%09d'%i
        new_name = '%s%s%s'%(save_path+'/',file_num,'.jpg')
        shutil.copyfile(old_name,new_name)
        
if __name__=='__main__':
    file_path = 'E:/wu_test/color/imageList.txt'
    save_path = 'E:/wu_test/color/picture3/'
    #file_path=sys.argv[1]
    #save_path=sys.argv[2]
    dir_to_picture(file_path,save_path)