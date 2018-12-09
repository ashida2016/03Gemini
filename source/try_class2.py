# -*- coding: UTF-8 -*-

# Filename : try_class1.py
# author by : （学员ID)

# 目的： 学会初步创建类，及使用类的方法
#       学会读 CSV 文件
#       批量为类赋值

import pandas as pd
import numpy as np

# 读取原子类
from class_atom import Atom


# 打开一个文件，顺序读每一行
filepath = "..\\config\\all_atoms.csv"


df = pd.read_csv(filepath, sep=',')

data = np.array(df.loc[:, :])

#print(df)
print(df.head())


column_headers = list(df.columns.values)
print(column_headers)
#print(data)
#print(data.type)

for i in range(5):
    print(data[i][0])
