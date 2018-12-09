# -*- coding: UTF-8 -*-

# Filename : class_product.py
# author by : （学员ID)

# 要点：类的基本概念
import class_atom

class Product:

    # 定义类基本属性（可公开被外部直接调用）
    name = '氧气'          # 中文产品名称
    formula = 'O2'          # 化学分子式
    price = 10              # 工业品价格 （元/吨）

    #struct = ('2', )

    # 定义构造方法
    def __init__(self, name, formula, price):
        self.name = name
        self.formula = formula
        self.price = price
