#!/usr/bin/env python
# fileObject = open('DownLoadedLink.txt', 'w')  #保存已经下载的链接
# try:
#     openFile = open('notExistsFile.txt','r')
#     fileContent = openFile.readlines()
# except IOError:
#     print ('File not Exists')        #执行
#     fileObject.write('File not Exists')  # 将下载好的连接保存在txt中
#     fileObject.write('\n')
#     fileObject.close()  # 关闭文件
# except:
#     print ('process exception')      #不执行
# else:
#     print ('Reading the file')       #不执行

# with open("spider.txt", "a") as f:
#     f.write("11")
#     f.write('\n')
#     f.close()
#     print("完成")

# f = open('DownLoadedLink.txt', "r")
# a=f.readlines()   #将文件内容以列表的形式存放
# print(a)

import time
import signal
from time import sleep

def CtrlCHandler(signum, frame):
    current_time = time.time()
    print("66")
    sys.exit(0)



for i in range(100):
    print("22")
    sleep(5)
signal.signal(signal.SIGINT, CtrlCHandler)