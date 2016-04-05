# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 20:26:05 2016

@author: Administrator
"""

import os

print u'第一步从视频中提取人脸保存到save_path中'
video_path = 'E:/1-18/12mm/2.avi'
save_path = 'E:/practical_face/result/code/video/Output/Pictures'
suff = '.bmp'
if not os.path.exists(save_path):
    os.mkdir(save_path)
commnd_line = "vedio_to_pic.exe " + video_path +' ' + save_path +' ' + suff
os.system(commnd_line)
