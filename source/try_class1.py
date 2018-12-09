# -*- coding: UTF-8 -*-

# Filename : try_class1.py
# author by : （学员ID)

# 目的： 学会初步创建类，及使用类的方法
#       学会从别的文件引用类

from class_atom import Atom


# 属于哪个周期（行）
# all_periods = (1, 2, 3, 4, 5, 6, 7)

# 属于哪个族（列）
all_families = ( 'I-A', 'II-A', \
               'III-B', 'IV-B', 'V-B', 'VI-B', 'VII-B',
               'VIII', \
               'I-B', 'II-B',  \
               'III-A', 'IV-A', 'V-A', 'VI-A', 'VII-A', \
               '0' )

# 分类
all_types = ( '金属', '非金属', '稀有气体')


# ---  使用类开始 --

# 练习一： 创建一个类
print("开始创建一个原子类：")
x = Atom()
x.show_myself()

# 练习二：修改类的公有成员
print("\n对1个原子类赋值：")
x.seq = 1           # 原子序号
x.name = '氢'        # 元素中文符号
x.symbol = 'H'      # 元素英文符号
x.mass = 1.008       # 精确的相对原子质量
x.period = 1         # 属于哪个周期（行）
x.family = 'I-A'     # 属于哪个族（列）
x.catalog = '非金属'  # 属于哪个分类

x.set_name_en('Hydrogen')
x.set_spell_zh('qīng')
x.show_myself()

# 练习三：创建两个类，并使用其成员进行运算
print("\n再生成一个原子类：")
y = Atom()
y.seq = 8           # 原子序号
y.name = '氧'        # 元素中文符号
y.symbol = 'O'      # 元素英文符号
y.mass = 16       # 精确的相对原子质量
y.period = 2         # 属于哪个周期（行）
y.family = 'VII-A'     # 属于哪个族（列）
y.catalog = '非金属'  # 属于哪个分类

y.set_name_en('Oxygen')
y.set_spell_zh('yǎng')
y.show_myself()

# 燃烧反应方程式： 2H2 + O2 点燃 2H2O
# 前的分子量
mass_before = 2 * ( x.mass * 2) + y.mass * 2
mass_after = 2 * ( x.mass * 2 + y.mass)

print("Before: (%.3f) - After:(%.3f)" % (mass_before, mass_after))






