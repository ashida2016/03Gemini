# -*- coding: UTF-8 -*-

# Filename : try_class2.py
# author by : （学员ID)

# 目的： 学会建立类的列表
#       加深类的使用方法


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

class Atoms_Table:

    # 公共属性
    count = 0           # 总共容纳的原子个数
    max_number = 0      # 最大的原子序号
    min_number = 0      # 最小的原子序号

    # 私有属性
    _csv_path = ""
    # 所有元素对象的 list
    _atoms = []

    # 创建 atoms 列表
    # 定义构造方法
    def __init__(self):
        # 将 CSV 文件内容读入内存
        df = pd.read_csv(get_csv_path(), sep=',')
        # 查看读入后内容
        print(df)

        # 将CSV内容转化为二维数组
        data = np.array(df.loc[:, :])

        # 顺序读取所有元素，并初始化每个实例化的类
        for row in data:


            # 新生成一个空白的原子类
            _atom = Atom()
            # 读取每一行的原子信息，并存入相应的类属性
            _atom.seq = row[0]
            _atom.symbol = row[1]
            _atom.name = row[2]
            _atom.set_spell_zh(row[3])
            _atom.mass = row[4]
            _atom.set_name_en(row[5])
            _atom.period = row[6]
            _atom.family = row[7]
            _atom.catalog = row[8]
            # 将填好信息的原子类加入列表
            _atoms.append(_atom)

        return

    # 获取指定原子序号的原子信息（返回一个 atom 类）
    def get_atom(number):
        atom = Atom()
        return atom

    # 获取 源数据文件路径的方法
    def get_csv_path():
        # 设定 CSV 文件所在的路径 path （注意在 ATOM 和 CMD 环境下当前工作路径有所差异）
        # for ATOM
        _csv_path = os.getcwd() + '\\' + 'config\\all_atoms.csv'
        # for cmd Python
        #filepath = os.getcwd() + '\\' + '..\\config\\all_atoms.csv'
        # for PyCharm
        #filepath = '..\\config\\all_atoms.csv'
        return
