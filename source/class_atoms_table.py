# -*- coding: UTF-8 -*-

# Filename : try_class2.py
# author by : （学员ID)

# 目的： 学会建立类的列表
#       加深类的使用方法
#       加深理解函数返回值的使用


import os
"""
import sys
import io
"""
import pandas as pd
import numpy as np

# 读取原子类
from class_atom import Atom

# 解决输出显示汉字乱码的问题
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

class Atoms_Table:

    # 公共属性
    table_ver = ""

    # 私有属性
    __atoms = []         # 所有元素对象的 list
    __count = 0          # 本表容纳的原子个数
    __max_seq = 0      # 最大的原子序号
    __min_seq = 0      # 最小的原子序号
    __max_mass = 0.0
    __min_mass = 0.0

    # 创建 atoms 列表
    # 定义构造方法
    def __init__(self):
        # 原子表名称
        table_ver = "元素周期表 Ver1.0 "

        # 将 CSV 文件内容读入内存
        # 设定 CSV 文件所在的路径 path （注意在 ATOM 和 CMD 环境下当前工作路径有所差异）
        # for ATOM
        csv_path = os.getcwd() + '\\' + 'config\\all_atoms.csv'
        # for cmd Python
        #filepath = os.getcwd() + '\\' + '..\\config\\all_atoms.csv'
        # for PyCharm
        #filepath = '..\\config\\all_atoms.csv'
        df = pd.read_csv(csv_path, sep=',')
        # 将CSV内容转化为二维数组
        data = np.array(df.loc[:, :])

        # 顺序读取所有元素，并初始化每个实例化的类
        for row in data:
            # 新生成一个空白的原子类
            self.__atom = Atom()
            # 读取每一行的原子信息，并存入相应的类属性
            self.__atom.seq = row[0]
            self.__atom.symbol = row[1]
            self.__atom.name = row[2]
            self.__atom.set_spell_zh(row[3])
            self.__atom.mass = row[4]
            self.__atom.set_name_en(row[5])
            self.__atom.period = row[6]
            self.__atom.family = row[7]
            self.__atom.catalog = row[8]
            # 将填好信息的原子类加入列表
            self.__atoms.append(self.__atom)

        # 更新计数器
        self.__count = len(self.__atoms)
        # 更新最大最小值
        self.__refresh_maxmin()

        return

    # 遍历所有元素，更新最大&最小 原子序数及相对质量
    def __refresh_maxmin(self):
        # 建立比较基准
        max_seq = -1
        max_mass = -1
        min_seq = 9999
        min_mass = 9999

        # 遍历，寻找最大最小值
        for atom in self.__atoms:
            if atom.seq > max_seq:
                max_seq = atom.seq
            if atom.seq < min_seq:
                min_seq = atom.seq
            if atom.mass > max_mass:
                max_mass = atom.mass
            if atom.mass < min_mass:
                min_mass = atom.mass

        # 更新内部属性
        self.__max_seq = max_seq
        self.__min_seq = min_seq

        self.__max_mass = max_mass
        self.__min_mass = min_mass

        return


    # ---------- 以下为供外部调用的函数 --------------
    # 获取原子列表的个数
    def get_count(self):
        return self.__count
    # 获取最大最小值 原子序号
    def get_max_seq(self):
        return self.__max_seq
    def get_min_seq(self):
        return self.__min_seq
    # 获取最大最小值 相对原子量
    def get_max_mass(self):
        return self.__max_mass
    def get_min_mass(self):
        return self.__min_mass
    # 获取指定原子序号的原子信息（返回一个 atom 类）
    def get_atom(num):
        found_atom = Atom()
        # 遍历搜寻
        for atom in self.__atoms:
            if atom.seq == num:
                found_atom.seq      = atom.seq
                found_atom.symbol   = atom.symbol
                found_atom.name     = atom.name
                found_atom.set_spell_zh(atom.get_spell_zh())
                found_atom.mass     = atom.mass
                found_atom.set_name_en(atom.get_name_en())
                found_atom.period   = atom.period
                found_atom.family   = atom.family
                found_atom.catalog  = atom.catalog
        return found_atom
