# -*- coding: UTF-8 -*-

# Filename : try_class1.py
# author by : （学员ID)

# 目的： 学会初步创建类，及使用类的方法
#       学会读 CSV 文件
#       批量为类赋值

import os
import sys
import io

import pandas as pd
import numpy as np

# 读取原子类
from class_atom import Atom

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 打开一个文件，顺序读每一行
filepath = os.getcwd() + '\\' + 'config\\all_atoms.csv'
#filepath = os.getcwd() + '\\' + '..\\config\\all_atoms.csv'
#filepath = '..\\config\\all_atoms.csv'

# 将 CSV 文件内容读入内存
df = pd.read_csv(filepath, sep=',')
# 查看读入后内容
print(df)
#print(df.head())
# 查看表头
column_headers = list(df.columns.values)
print(column_headers)

# 将CSV内容转化为二维数组
data = np.array(df.loc[:, :])
# 查看二维数组内容
print(data)

# 按行/列方式随意调用
for i in range(10):
    print(data[i][5])

for j in range(9):
    print(data[3][j])
