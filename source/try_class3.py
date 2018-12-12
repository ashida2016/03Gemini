# -*- coding: UTF-8 -*-

# Filename : try_class3.py
# author by : （学员ID)

# 目的： 复习学会创建类，将类实例化的方法
#       复习学会从别的文件引用类
#       复习学会调用实例化类的公有/私有属性方法
#       复习对单个类的一般操作（属性、方法）

import os
import sys
import io

# 解决输出显示汉字乱码的问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# print (sys.stdout.encoding)  # 确认当前的控制台显示字符的编码


from class_matter import Matter

from class_tool_split_to_elements import SplitToElements

# ---  使用类开始 --

# 练习一： 创建一个类
print("开始创建一个物质类...", end='')
x = Matter()

# 练习二：修改类的公有/私有成员
print("对 1 个物质类赋值：")
# 定义类基本属性（可公开被外部直接调用）
x.name = '氯化钠'  # 物质的中文名称
x.alias = '食盐'  # 物质的别名
x.formula = 'CuSO4•5H2O'  # 物质的化学分子式
x.catalog1 = '常见的盐'  # 分类1
x.comment = '经常吃的东东'  # 物质简介
x.show_myself()



# 测试分解
#x.formula = 'KAl(SO4)2•12H2O'
#x.formula = 'CuSO4•5H2O'
#x.formula = 'H2O'
#x.formula ='CuSO4'
#x.formula ='CH3COOH'
#x.formula = 'Cu2(OH)2CO3'
#x.formula = 'Cu12KAlCH3NH4HCO13Fe25O17'
#x.formula = 'Al2(SO4)3'
x.formula ='(NH4)2SO4'
print("\n测试分子式 = %s" % (x.formula))

tool = SplitToElements(x.formula)

output = tool._split1()
print("水合物  构成-", end='')
print(output)

output = tool._split2()
print("根     构成-", end='')
print(output)

output = tool._split3()
print("剩余部分构成-", end='')
print(output)

#output = tool._split_nomal(x.formula)
#print(output)
