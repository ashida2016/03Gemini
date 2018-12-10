# -*- coding: UTF-8 -*-

# Filename : main.py
# author by : （学员ID)

# 目的： 学会初步创建类，及使用类的方法
#       学会从别的文件引用类


import os
import sys
import io

import pandas as pd
import numpy as np

# 读取原子类
from class_atom import Atom
# 引用原子周期表类
from class_atoms_table import AtomsTable
# 引用物质类
from class_matter import Matter

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 调用原子周期表类 ，自动生成一张原子周期表
m = Matter()

m.show_myself()
#m.show_myelements()

# 将 CSV 文件内容读入内存
# 设定 CSV 文件所在的路径 path （注意在 ATOM 和 CMD 环境下当前工作路径有所差异）
# for ATOM
# csv_path = os.getcwd() + '\\' + 'config\\all_matters.csv.csv'
# for cmd Python
# csv_path = os.getcwd() + '\\' + '..\\config\\all_matters.csv.csv'
# for PyCharm
csv_path = '..\\config\\all_matters.csv'
df = pd.read_csv(csv_path, sep=',')
# 将CSV内容转化为二维数组
data = np.array(df.loc[:, :])

# 将CSV内容转化为二维数组
data = np.array(df.loc[:, :])
# 查看二维数组内容
#print(data)
print(len(data))





