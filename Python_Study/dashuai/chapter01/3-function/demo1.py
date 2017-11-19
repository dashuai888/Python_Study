#!/usr/bin/env python3
# --*-- coding: utf-8 --*--

"""
函数

基本上所有的高级语言都支持函数，Python也不例外。Python不但能非常灵活地定义函数，而且本身内置了很多有用的函数，可以直接调用。

可以直接从Python的官方网站查看文档：http://docs.python.org/3/library/
也可以在交互式命令行通过help(xxx)查看xxx函数的帮助信息。
"""
a = -11
print(a) # -11
print(abs(a)) # 11

# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：abs()有且仅有1个参数，但给出了两个
# print(abs(a, a)) # TypeError: abs() takes exactly one argument (2 given)

# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型
# abs('-1') # TypeError: bad operand type for abs(): 'str'

# max() 函数可以接收任意多个参数，并返回最大的那个，min() 相反
print(max(1, 2, 3, 4, 5, 1111, -111, 13131, 131)) # 13131
print(min(1, 2, 3, 4, 5, 1111, -111, 13131, 131)) # -111


"""
数据类型转换

Python内置的常用函数还包括数据类型转换函数
"""
# int()函数可以把其他数据类型转换为整数
s = '123'
i = int(s)

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-1)) # 1


"""
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
然后，在缩进块中编写函数体，函数的返回值用return语句返回。
"""
# 定义一个求绝对值的my_abs函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-1))
print(my_abs(1))

# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return
def my_func():
    return

print(my_func()) # None

def my_func1(): # 不能为空实现体，不推荐这样写
    x = 1

print(my_func1()) # None

"""
空函数

如果想定义一个什么事也不做的空函数，可以用pass语句，推荐

pass语句什么都不做，那有什么用？
实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
"""
def nop():
    pass

# pass还可以用在其他语句里
def nop1(x):
    if x == 0:
        pass # 缺少了pass，代码运行就会有语法错误

"""
参数检查

调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
"""
# 如果参数类型不对，Python解释器就无法帮我们检查
# 之前自定义的my_abs函数
# print(my_abs('-1')) # TypeError: unorderable types: str() >= int()

# 系统自带的abs
# print(abs('-1')) # TypeError: bad operand type for abs(): 'str'

# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而自定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。

# 修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
def my_abs_1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        print(x)
    else:
        print(-x)

print(my_abs_1('-1'))
# 添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误

#     raise TypeError('bad operand type')
# TypeError: bad operand type