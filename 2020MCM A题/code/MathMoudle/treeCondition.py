import csv
from collections import Counter

datas = []  # 温度


def importCSV(file_name):
    file_path = 'D:\\datas\\netCDF-CSV2\\' + str(file_name) + '.csv'
    try:
        with open(file_path, 'r') as targeFile:
            # 创建读入流
            reader = csv.reader(targeFile)
            # 读入数据
            datas.append(list(reader))

        targeFile.close()  # 关闭文件
        print('导入成功-' + str(file_name))
    except Exception as e:  # 异常处理
        print('Error: ' + str(e))


def exportCSV(maxs, mins, poss):
    name = ['maxs', 'mins', 'poss']
    for n in name:
        file_path = 'D:\\datas\\forecast\\' + n + '.csv'
        try:
            with open(file_path, 'w', newline='') as targeFile:
                # 创建写入流
                writer = csv.writer(targeFile)
                # 写入表头
                writer.writerow(('year', 'data'))
                # 写入数据
                data = []
                if n == 'maxs':
                    data = maxs
                elif n == 'mins':
                    data = mins
                else:
                    data = poss
                year = 1980
                for d in data:
                    writer.writerow((year, d))
                    year += 1
            print('导出成功-' + n)
            targeFile.close()  # 关闭文件
        except Exception as e:  # 异常处理
            print('Error: ' + str(e))


if '__name__==__main__':
    for i in range(1, 60):
        importCSV(i)

    maxs = [0] * 40  # 极好
    mins = [12] * 40  # 极劣
    poss = []  # 最可能
    for wj in range(len(datas)):
        year = 1980
        month = 1
        ma = 0
        mi = 12
        po = [0] * 12
        flag = 0
        num = 0
        pos = []
        for m in range(0, 480):
            d = datas[wj][m]
            if float(d[0]) < 3 or float(d[0]) > 10:
                flag = 1
                num += 1
            elif flag == 1:
                ma = max(ma, num)
                mi = min(mi, num)
                po[num] += 1
                num = 0
                flag = 0

            month += 1
            if month > 12:
                maxs[year - 1980] = max(maxs[year - 1980], ma)
                mins[year - 1980] = min(mins[year - 1980], mi)
                p = 1  # 计算出现最多次数的持续时间,0不计算
                for k in range(2, 12):
                    if po[k] > po[p]:
                        p = k
                pos.append(p)
                ma = 0
                mi = 12
                po = [0] * 12
                flag = 0
                num = 0
                year += 1
                month = 1
        poss.append(pos)

    pos = []
    for i in range(0, 40):
        p = [0] * 12
        for j in range(0, 59):
            p[poss[j][i]] += 1
        pp = 1
        for k in range(2, 12):
            if p[k] > p[pp]:
                pp = k
        pos.append(pp)

    print('maxs:')
    print(maxs)
    print('pos:')
    print(min)
    print('mins:')
    print(pos)

    exportCSV(maxs, mins, pos)
