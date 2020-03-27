# 批量读取b北京市2008年的出租车数据，转换成csv格式。
import os
import csv
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    pathtxt_list = []
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        pathtxt_list.append(child.encode('utf-8').decode('gbk'))
    return pathtxt_list

def readFile(filename):
    fopen = open(filename, 'r')
    f_list = []
    for eachLine in fopen:
        f_list.append(eachLine.strip('\n'))
    fopen.close()
    return f_list

def csvsave(taxi_list_1):
    with open('taxi.csv', 'wb') as myFile:
        myWriter = csv.writer(myFile)
        myWriter.writerow(['taxi_id', 'date_time', 'lon', 'lat'])
        myWriter.writerows(taxi_list_1)
# 主程序
pathtxt_list = eachFile("\\microsoft\\taxi_log_2008_by_id")
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