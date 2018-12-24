# import os
# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         print(root) #当前目录路径
#         print(dirs) #当前路径下所有子目录
#         print(files) #当前路径下所有非目录子文件
#
# file_name("E:\sxl_Programs\Python\PDF")


#导入os包
import os
#设定文件路径
path="E:\\sxl_Programs\\Python\\PDF2\\"
i=1
#对目录下的文件进行遍历
for file in os.listdir(path):
#判断是否是文件
    if os.path.isfile(os.path.join(path,file))==True:
#设置新文件名
        new_name=file.replace(file,"%d.pdf"%(i+1027))
#重命名
        os.rename(os.path.join(path,file),os.path.join(path,new_name))
        i+=1
#结束
print ("End")