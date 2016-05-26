# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:45:41 2015

@author: Administrator
"""

import Tkinter as tk
import os


def make_list(dir_path,class_num=0,sub_image_num=0,total=0,suffix='.jpg',label_start=0,save_file_name='image_list.txt'):
    Class_num = class_num
    Image_num = sub_image_num
    Total = total
    with open(save_file_name,'a') as fr:
        if label_start == 'False':
            files = os.listdir(dir_path)
            for f in files:
                sub_dir_path = dir_path+'/'+f
                if os.path.isdir(sub_dir_path):
                    make_list(sub_dir_path,Class_num,Image_num,Total,suffix,label_start,save_file_name)
                    Class_num += 1
                else:
                    image_path = dir_path+'/'+f
                    path = os.path.splitext(image_path)
                    if path[1] == suffix:
                        str1=image_path
                        fr.write(str1+'\n')
                        Image_num += 1
            Total += Image_num
            #print image_path+''+str(label)
        else:
            label=int(label_start)
            files = os.listdir(dir_path)
            for f in files:
                sub_dir_path = dir_path+'/'+f
                if os.path.isdir(sub_dir_path):
                    make_list(sub_dir_path,Class_num,Image_num,Total,suffix,label,save_file_name)
                    label +=1
                    Class_num += 1
                else:
                    image_path = dir_path+'/'+f
                    path = os.path.splitext(image_path)
                    if path[1] == suffix:
                        str1=image_path+' '+str(label)
                        fr.write(str1+'\n')
                        Image_num += 1
            Total += Image_num
            #print image_path+''+str(label)
    result = u"转换已经结束！可打开%s"%(save_file_name)
    print u"第 %d 类中共有图片：%d"%(Class_num,Image_num)
    print u"图片总数：%d"%(Total)
    return result
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title('Make_Image_List')
    
    str1 = tk.StringVar()
    str2 = tk.StringVar()
    str3 = tk.StringVar()
    str4 = tk.StringVar()
    str5 = tk.StringVar()
    str6 = tk.StringVar()
    str7 = tk.StringVar()
    
    label1 = tk.Label(root,text=u'图像文件夹路径')
    label1.grid(row=0,column=0)
    
    entry1 = tk.Entry(root,textvariable=str1)
    entry1.grid(row=0,column=1)
    
    label2 = tk.Label(root,text=u'图片后缀（默认是.jpg）')
    label2.grid(row=1,column=0)
    
    str2.set('.jpg')
    entry2 = tk.Entry(root,textvariable=str2)
    entry2.grid(row=1,column=1)
    
    label3 = tk.Label(root,text=u'标签开始索引（默认是0）')
    label3.grid(row=2,column=0)
    
    str3.set('0')
    entry3 = tk.Entry(root,textvariable=str3)
    entry3.grid(row=2,column=1)
    
    label4 = tk.Label(root,text='保存文件的路径')
    label4.grid(row=3,column=0)
    
    entry4 = tk.Entry(root,textvariable=str4)
    entry4.grid(row=3,column=1)
    
    label5 = tk.Label(root,text=u'转换进度')
    label5.grid(row=4,column=0)
    
    entry5 = tk.Entry(root,textvariable=str5)
    entry5.grid(row=4,column=1)
    
    label6 = tk.Label(root,text=u'类别数')
    label6.grid(row=5,column=0)
    
    entry6 = tk.Entry(root,textvariable=str6)
    entry6.grid(row=5,column=1)
    
    label7 = tk.Label(root,text=u'图片总数')
    label7.grid(row=6,column=0)
    
    entry7 = tk.Entry(root,textvariable=str7)
    entry7.grid(row=6,column=1)
    
    #buttonOK = tk.Button(root,text=u'开始',command=lambda:str5.set(make_list(str1.get(),str2.get(),str3.get(),str4.get())))
    #buttonOK.grid(row=7,column=0)
    
    buttonOK = tk.Button(root,text=u'开始',command=lambda:str5.set((make_list(str1.get(),0,0,0,str2.get(),str3.get(),str4.get()))))
    buttonOK.grid(row=7,column=0)
    
    buttonExit = tk.Button(root,text=u'退出',command=root.quit())
    buttonExit.grid(row=7,column=1)
    
    root.mainloop()
    #files = make_list('F:/lfw')
