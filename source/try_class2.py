# -*- coding: UTF-8 -*-

# Filename : try_class2.py
# author by : （学员ID)

# 目的： 学会初步创建类，及使用类的方法
#       学会使用 pandas 读 CSV 文件
#       批量为类赋值
#       了解矩阵库 numpy

import os
import sys
import io

import pandas as pd
import numpy as np


# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 打开一个文件，顺序读每一行
# for ATOM
# csv_path = os.getcwd() + '\\' + 'config\\all_atoms.csv'
# for cmd Python
# csv_path = os.getcwd() + '\\' + '..\\config\\all_atoms.csv'
# for PyCharm
csv_path = '..\\config\\all_atoms.csv'

# 练习一
# 将 CSV 文件内容读入内存
df = pd.read_csv(csv_path, sep=',')
# 查看读入后内容
print("\n读入CSV文件，并转换成如下格式----------")
print(df)

# 练习二，了解 pandas
print("\n矩阵前5行内容是----------")
print(df.head(5))
print("\n矩阵后5行内容是----------")
print(df.tail(5))
print("\n矩阵表头是----------")
column_headers = list(df.columns.values)
print(column_headers)

# 练习三， 了解 numpy
# 将CSV内容转化为二维数组
data = np.array(df.loc[:, :])
# 查看二维数组内容
print("\n转化为二维数组（表格）后的形式如下----------")
print(data)

rows_columns = data.shape
print(rows_columns)
total_rows = int(rows_columns[0])
total_columns = int(rows_columns[1])

# 练习四， 通过numpy 随意调用二维数组的数据
# 按行/列方式随意调用
row = 5
col = 2
print("\n打印（%d行，%d列）的数据----------" % (row, col))
print(data[row][col])

row = 10
print("\n打印第(%d)行的数据----------" % (row))
for i in range(0, total_columns):
    print(data[row-1][i])

col = 2
print("\n打印第(%d)列的数据----------" % (col))
for j in range(0, total_rows):
    print(data[j][col-1])

