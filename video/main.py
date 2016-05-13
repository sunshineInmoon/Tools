# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 20:26:05 2016

@author: Administrator
"""

import os
import text_process
import vedio
import classficition

def process(vedio_path,pic_save_path,pic_imagelist,clean_save_path,proto,model,\
         clean_imagelist,feature_path,result_save_path,clean_dis=30,suff='.bmp'):
    print u'第一步从视频中提取人脸保存到save_path中'
    vedio.vedio_to_pic(vedio_path,pic_save_path,suff)
    print u'第二步，删去清晰度较小的图片，建议阈值设置在30左右'
    text_process.creat_imagelist_NoLabel(pic_save_path,pic_imagelist)
    vedio.sharpness_clean(pic_imagelist,clean_save_path,clean_dis)
    print u'第三步，提取特征'
    vedio.ext_feature(proto,model,clean_imagelist,feature_path)
    print u'第四步，分类'
    classficition.classficition(feature_path,result_save_path,clean_save_path,suff)
    
def main(vedio,out_path,modle_path,clean_dis=30,suff='.bmp'):
    pic_save_path = out_path + '/picture'
    pic_imagelist = out_path + '/pic_imagelist.txt'
    clean_save_path = out_path + '/clean'
    proto = modle_path + '/Net_deploy.prototxt'
    model = modle_path + '/Net.caffemodel'
    clean_imagelist = out_path + '/clean_imagelist.txt'
    feature_path = out_path + '/feature'
    result_save_path = out_path + '/result'
    process(vedio_path,pic_save_path,pic_imagelist,clean_save_path,proto,model,clean_imagelist,\
        feature_path,result_save_path)
        
if __name__ == '__main__':
    vedio_path = 'E:/1-18/12mm/3.avi'
    out_path = 'E:/practical_face/avi3'
    module_path = 'E:/practical_face/result/code/video/modle'
    main(vedio_path,out_path,module_path)

