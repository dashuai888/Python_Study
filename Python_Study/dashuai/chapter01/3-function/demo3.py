#!/usr/bin/env python3
# --*-- coding: utf-8 --*--
import math  # 表示导入math包，并允许后续代码引用math包里的sin、cos等函数。

"""
返回多个值
"""
# 在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
def move(x, y, step, angle = 0):
    newx = x + step * math.cos(angle)
    newy = y + step * math.sin(angle)

    return newx, newy

# 可以同时获得返回值
x, y = move(1, 2, 3)
print(x, y) # 4.0 2.0

# 其实这只是一种假象，Python函数返回的仍然是单一值
print(type(move(1, 2, 3))) # <class 'tuple'>
# 原来返回值是一个tuple，但是在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。