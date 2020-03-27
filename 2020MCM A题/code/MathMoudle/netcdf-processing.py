import netCDF4
from netCDF4 import Dataset
import csv

lat = []  # 纬度
lon = []  # 经度
time = []  # 日期
depth_std = []  # 深度
temp = []  # 温度


def iniData(year, month):
    nc_obj = Dataset('D:\\datas\\original\\CZ16_1_2000m_Temp_year_' + str(year) + '_month_' + month + '.nc')
    # print('读取数据值')
    global lat  # 纬度
    lat.append((nc_obj.variables['lat'][:]))
    global lon  # 经度
    lon.append((nc_obj.variables['lon'][:]))
    global time  # 日期
    time.append((nc_obj.variables['time'][:]))
    global depth_std  # 深度
    depth_std.append((nc_obj.variables['depth_std'][:]))
    global temp  # 温度
    temp.append((nc_obj.variables['temp'][:]))
    print('导入成功-' + str((nc_obj.variables['time'][:])))

def exportCSVWJ(file_name, w, j):
    file_path = 'D:\\datas\\netCDF-CSV2\\' + str(file_name) + '.csv'
    try:
        with open(file_path, 'a', newline='') as targeFile:
            # 创建写入流
            writer = csv.writer(targeFile)
            # # 写入表头
            # writer.writerow(('trmperature', 'latitude', 'longitude'))
            # 写入数据
            for wj in range(len(temp)):
                l = lon[0][j]
                if l > 180:
                    l -= 360
                writer.writerow((temp[wj][w][j][0], lat[0][w], l))

        targeFile.close()  # 关闭文件
        print('导出成功-' + str(file_name))
        print('---------------******-------------------')
    except Exception as e:  # 异常处理
        print('Error: ' + str(e))


if '__name__==__main__':
    # 起始编号
    year = 1980
    month = 1
    # 遍历nc文件
    while True:
        if year == 2020:
            break
        m = month
        if m < 10:
            m = '0' + str(m)
        else:
            m = str(m)

        # 初始化数据
        iniData(year, m)

        month += 1
        if month > 12:
            year += 1
            month = 1

    num = 1
    for w in range(len(lat[0])):  # w为纬度
        for j in range(len(lon[0])):  # j为经度
            if temp[0][w][j][0] != '--' and lat[0][w] >= 55 and lat[0][w] <= 59 and (
                    (lon[0][j] <= 5 and lon[0][j] >= 0) or (lon[0][j] <= 360 and lon[0][j] >= 350)):  # 英格兰海域范围
                exportCSVWJ(num, w, j)
                num += 1
