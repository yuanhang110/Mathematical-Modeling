# -*- coding: utf-8 -*-
# 批量读取微软出租车数据
# Python 2.7
import os
import csv


# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    pathtxt_list = []
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        pathtxt_list.append(child.decode('gbk'))  # .decode('gbk')是解决中文显示乱码问题
    return pathtxt_list


# 定义读取txt函数
def readFile(filename):
    fopen = open(filename, 'r')  # r 代表read
    f_list = []
    for eachLine in fopen:
        f_list.append(eachLine.strip('\n'))  # 注意别忘了去掉换行符'\n'
    fopen.close()
    return f_list


# 定义csv保存文件
def csvsave(taxi_list_1):
    with open('taxi.csv', 'wb') as myFile:
        myWriter = csv.writer(myFile)
        myWriter.writerow(['taxi_id', 'date_time', 'lon', 'lat'])
        myWriter.writerows(taxi_list_1)
# 主程序
pathtxt_list = eachFile("C:\\Users\\xyh\\Desktop\\microsoft\\taxi_log_2008_by_id")
taxi_list = []
for filename in pathtxt_list:
    print(filename,'导入成功')
    f_list = readFile(filename)
    # taxi_list.append(f_list); # 以整个list添加
    taxi_list.extend(f_list)# 一条条的合并
taxi_list_1 = []
for taxi in taxi_list:
    taxi_list_1.append(taxi.split(','))
csvsave(taxi_list_1)