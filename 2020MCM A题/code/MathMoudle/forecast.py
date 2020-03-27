import csv

temp = []  # 温度

def importCSV(file_name):
    #file_path = 'D:\\datas\\ending\\' + file_name + '.csv' #预测数据
    file_path = 'D:\\datas\\netCDF-CSV2\\' + file_name + '.csv' #原始数据
    try:
        with open(file_path, 'r') as targeFile:
            # 创建读入流
            reader = csv.reader(targeFile)
            # 读入数据
            temp.append(list(reader))

        targeFile.close()  # 关闭文件
        print('导入成功-' + file_name)
    except Exception as e:  # 异常处理
        print('Error: ' + str(e))

def exportCSV(month, year, type, wj):
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)
    time = str(year) + month
    file_path = ''
    if type == 0:
        # file_path = 'D:\\datas\\Mackerel\\' + time + '.csv' #预测数据
        file_path = 'D:\\datas\\netCDF-CSV3\\Mackerel\\' + time + '.csv' #原始数据
    else:
        # file_path = 'D:\\datas\\Herring\\' + time + '.csv' #预测数据
        file_path = 'D:\\datas\\netCDF-CSV3\\Herring\\' + time + '.csv' #原始数据
    try:
        with open(file_path, 'w', newline='') as targeFile:
            # 创建写入流
            writer = csv.writer(targeFile)
            # 写入表头
            writer.writerow(('latitude', 'longitude'))
            # 写入数据
            for n in range(len(wj)):
                writer.writerow((wj[n][0], wj[n][1]))
        print('导出成功-' + time)
        targeFile.close()  # 关闭文件
    except Exception as e:  # 异常处理
        print('Error: ' + str(e))

if '__name__==__main__':
    # 起始编号
    num = 1
    # 遍历nc文件
    while num < 65:
        # 初始化数据
        importCSV(str(num))
        num += 1
    print('导入成功-全部')
    print('---------------******-------------------')

    #year = 2020 #预测数据
    year = 1980 #原始数据
    month = 1
    # for m in range(0, 600): #预测数据
    for m in range(0, 480): #原始数据
        mackerel = []
        herring = []
        for wj in range(len(temp)):
            t = temp[wj][m]
            if float(t[0]) > 6 and float(t[0]) < 10:
                mackerel.append([float(t[1]), int(float(t[2]))])
            if float(t[0]) > 3 and float(t[0]) < 6:
                herring.append([float(t[1]), int(float(t[2]))])
        exportCSV(month, year, 0, mackerel)
        exportCSV(month, year, 1, herring)

        month += 1
        if month > 12:
            year += 1
            month = 1

    print('导出成功-全部')
    print('---------------******-------------------')
