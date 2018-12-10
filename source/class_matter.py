# -*- coding: UTF-8 -*-

# Filename : class_matter.py
# author by : （学员ID)

# 目的： 学会在一个类中使用其他类
#       加深类的使用方法
#       加深理解函数返回值的使用

"""
import sys
import io
"""
import random

# 读取原子类
from class_atom import Atom
from class_atoms_table import AtomsTable

# 解决输出显示汉字乱码的问题
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码

# 类定义


class Matter:

    # 定义类基本属性（可公开被外部直接调用）
    name = 'Unkown'                 # 物质的中文名称
    alias = 'Unkown'                # 物质的别名
    formula = 'Unkown'              # 物质的化学分子式
    catalog1 = 'Unkown'             # 分类1
    comment = 'Unkown'              # 物质简介

    _mass = 0.0                # 分子量
    _price = 0.0
    _elements = {'H': 2, 'O': 1}
    _atom_table = AtomsTable()

    def __init__(self):
        return

   # 定义类的自我展示
    def show_myself(self):
        print("本物质的中午名称为(%s)[%s]， 化学分子式为(%s)，化学分子量为(%.2f)，价格为(%0.2f)元/吨，简介[%s]"  \
              % ( self.name, self.alias, self.formula, self.get_mass(), self.get_price(), self.comment )  )
        print("构成本物质的元素为：")
        for key,value in self._elements.items():
            print("%s(%d)" % (key, value))
        return

    def show_myelements(self):
        for key,value in self._elements.items():
            print("%s(%d)" % (key, value))
        return

    def get_mass(self):
        mass = 0
        for key, value in self._elements.items():
            atom = self._atom_table.get_atom_by_symbol(key)
            mass += atom.mass * value
        return mass

    def get_price(self):
        price = random.random() * 10000
        return price
