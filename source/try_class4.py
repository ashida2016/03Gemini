# -*- coding: utf-8 -*-

# Filename : try_class4.py
# author by : （学员ID)

# 目的： 复习学会初步创建类，及使用类的方法
#       复习学会使用 pandas 读 CSV 文件
#       复习批量为类赋值的一种做法（从文件读取生成类）
#       复习矩阵库 numpy

import os
import sys
import io

import pandas as pd
import numpy as np

# 引用物质类
from class_matter import Matter

# 引用物质表类
from class_matters_table import MattersTable


# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 打开一个文件，顺序读每一行
# for ATOM
csv_path = os.getcwd() + '\\' + 'config\\all_matters.csv'
# for cmd Python
# csv_path = os.getcwd() + '\\' + '..\\config\\all_matters.csv'
# for PyCharm
# csv_path = '..\\config\\all_matters.csv'

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

# 练习五，将二位数组内容批量赋予类，并建立一个类的列表
# 所有物质对象的 list
matters = []

# 顺序读取所有元素，并初始化每个实例化的类
for row in data:
    # 新生成一个空白的物质类
    matter = Matter()
    # 读取每一行的物质信息，并存入相应的类属性
    matter.name = row[0]
    matter.alias = row[1]
    matter.formula = row[2]
    matter.catalog1 = row[3]
    matter.comment = row[4]
    # 将填好信息的物质类加入列表
    matters.append(matter)

# 打印所有的类
print("\n总共转化了 (%d) 个物质类：" % (len(matters)))
for matter in matters:
    matter.show_myself()

# 练习五， 直接使用 matter_table 完成上述操作，体验类的便利性
mt = MattersTable()
for m in mt.matters_iterator:
    print(m.name)
