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

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 调用原子周期表类 ，自动生成一张原子周期表
at = AtomsTable()

print("原子周期表读取完毕！总计读入了(%d)个原子 " % ( at.get_count() ) )
print("其中最小的原子序号是(%d), 最大的原子序号是(%d)" % (at.get_min_seq(), at.get_max_seq()))
print("其中最小的相对质量是(%.3f)，最大的相对质量是(%.3f)" % (at.get_min_mass(), at.get_max_mass()))

x = at.get_atom_by_seq(58)
x.show_myself()

x = at.get_atom_by_symbol('H')
x.show_myself()

for atom in at.atoms_iterator:
    print("Seq=(%d)-%s" % (atom.seq, atom.symbol))
