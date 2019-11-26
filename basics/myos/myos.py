# 打开个关闭文件
import os

def saveFile(dir,file,str_content): 
    content = str_content.encode("utf-8")
    dir_name = dir
    file_name = dir_name + '/' +file
    # 判断文件夹是否存在
    dir_exist = os.path.exists(dir_name)
    if dir_exist == False:
        # 创建文件夹
        os.mkdir(dir_name)
    # 检查文件是否存在和可读写
    fd = open(file_name, 'wb+')
    res = fd.write(content)
    fd.close()
    return res

