# -*- coding: UTF-8 -*-

# Filename : class_matter.py
# author by : （学员ID)

# 目的： 学会在一个类中使用其他类
#       加深类的使用方法
#       加深理解函数返回值的使用
# 配套练习：
#       try_class3.py


import random

# 引用元素周期表类
# from class_atoms_table import AtomsTable

# 类定义
class Matter:

    # 定义类基本属性（可公开被外部直接调用）
    name = 'Unkown'                 # 物质的中文名称
    alias = 'Unkown'                # 物质的别名
    formula = 'Unkown'              # 物质的化学分子式
    catalog1 = 'Unkown'             # 分类1
    comment = 'Unkown'              # 物质简介

    _elements = {}                  # 元素字典  - 比较复杂，不求掌握
    _mass = 0.0                     # 分子量    - 根据元素字典来计算

    _price = 0.0                    # 当前价格 - 将来动态的获取，目前暂时用 random 替代

    #__atoms_table = AtomsTable()     # 内部计算用的 元素

    def __init__(self):
        #__atoms_table = AtomsTable()
        #self.split_to_elements()
        return

    # 定义类的自我展示
    def show_myself(self):
        print("本物质的中文名称为(%s)[%s]， 化学分子式为(%s)，化学分子量为(%.2f)，价格为(%0.2f)元/吨，简介[%s]"  \
              % ( self.name, self.alias, self.formula, self.get_mass(), self.get_price(), self.comment )  )
        print("构成本物质的元素为：")
        for key,value in self._elements.items():
            print("%s(%d)" % (key, value))
        return

    # 显示构成本物质的所有原子及数量
    def show_myelements(self):
        for key,value in self._elements.items():
            print("%s(%d)" % (key, value))
        return

    # 获取本物质的当前价格
    def get_price(self):
        price = random.random() * 10000
        return price

    # 显示本物质的元素字典
    def show_my_elements(self):
        print("我的元素构成是：%s" % (self._elements))
        return

    # 依据本物质的元素构成计算分子量
    def get_mass(self):
        mass = -1
        #for key, value in self._elements.items():
        #    atom = self.__atoms_table.get_atom_by_symbol(key)
        #    mass += atom.mass * value
        return mass

    """
    # 依据本物质的分子式构筑本物质的
    def split_to_elements(self):
        atom_list = []  # 内部计算用的
        for atom in self.__atoms_table.atoms_iterator:
            atom_list.append(atom.symbol)

        p1 = 0
        p2 = 1

        special = ['(', ')', '•']   # 分子式中可能出现的特殊字符
        sub1 = ''
        sub2 = ''
        sub3 = ''
        cur_atom = ''
        cur_volum = 0

        while p2<=len(self.formula):
            sub1 = self.formula[p1]
            sub2 = self.formula[p2]

            if sub1 in special:   # 当前为“(”
                p1 += 1
                p2 += 1

            if sub1.isupper() and sub2.islower():
                cur_atom = sub1 + sub2
                p1 += 2
                p2 += 2
                if p2<len(self.formula):
                    sub3 = self.formula[p1+1]
                    if sub3.isdigit():
                        cur_volum = int(sub3)
                        p1 += 1
                        p2 += 1
                    else:
                        cur_volum = 1
                else:
                    cur_volum = 1
            if sub1.isupper() and sub2.isupper():
                cur_atom = sub1
                p1 += 1
                p2 += 1

            # 创建一个元素键值
            self._elements[cur_atom] = cur_volum
            print(self._elements)
        return
    """
