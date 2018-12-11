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
# 应用物质类
from class_matters_table import MattersTable

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 调用原子周期表类 ，自动生成一张原子周期表
mt = MattersTable()

for matter in  mt.matters_iterator:
    matter.split_to_elements()
    print("物质名称：(%s) - (%s) -(%s)" % (matter.name, matter.formula))
    matter.show_my_elements()


