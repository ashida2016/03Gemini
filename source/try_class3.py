# -*- coding: UTF-8 -*-

# Filename : try_class2.py
# author by : （学员ID)

# 目的： 学会初步创建类，及使用类的方法
#       学会读 CSV 文件并转化为二维数组


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

# 设定 CSV 文件所在的路径 path （注意在 ATOM 和 CMD 环境下当前工作路径有所差异）
filepath = os.getcwd() + '\\' + 'config\\all_atoms.csv'
#filepath = os.getcwd() + '\\' + '..\\config\\all_atoms.csv'
#filepath = '..\\config\\all_atoms.csv'

# 将 CSV 文件内容读入内存
df = pd.read_csv(filepath, sep=',')
# 查看读入后内容
#print(df)

# 将CSV内容转化为二维数组
data = np.array(df.loc[:, :])
# 查看二维数组内容
#print(data)
print(len(data))

# 所有元素对象的 list
atoms = []

# 顺序读取所有元素，并初始化每个实例化的类
for row in data:
    atom = Atom()
    atom.seq = row[0]
    atom.symbol = row[1]
    atom.name = row[2]
    atom.set_spell_zh(row[3])
    atom.mass = row[4]
    atom.set_name_en(row[5])
    atom.period = row[6]
    atom.family = row[7]
    atom.catalog = row[8]

    atoms.append(atom)

print(len(atoms))

# 打印所有的类
for atom in atoms:
    print("(%d) - %s(%s)" % (atom.seq, atom.name, atom.symbol))

# 计算所有原子的平均原子量
total_mass = 0.0

for atom in atoms:
    total_mass += atom.mass

average_mass = total_mass / len(atoms)
print("所有元素平均原子量是：%.3f" % (average_mass))

# 计算所有特定原子的平均原子量
total_mass1 = 0.0
total_mass2 = 0.0
total_mass3 = 0.0
for atom in atoms:
    if atom.catalog == '非金属':
        total_mass1 += atom.mass
    elif atom.catalog =='金属':
        total_mass2 += atom.mass
    else:
        total_mass3 += atom.mass

average_mass = total_mass1 / len(atoms)
print("所有非金属元素平均原子量是：%.3f" % (average_mass))

average_mass = total_mass2 / len(atoms)
print("所有金属元素平均原子量是：%.3f" % (average_mass))

average_mass = total_mass3 / len(atoms)
print("所有稀有气体元素平均原子量是：%.3f" % (average_mass))
