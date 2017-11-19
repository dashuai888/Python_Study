#!/usr/bin/env python3
# --*-- coding: utf-8 --*--

"""
条件判断
"""

# 输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现
age = 22
# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则执行else语句。
if age == 21:
    print(22)
else:
    print('不是 %d' % age)
# 注意不要少写了冒号:

# 上面的判断是很粗略的，完全可以用elif做更细致的判断
if age >= 100:
    print('百岁')
elif age >= 70: # elif是else if的缩写，完全可以有多个elif
    print('老年')
elif age >= 40:
    print('中年')
else:
    print('年轻')

# if判断条件还可以简写
# 非0数值、非空字符串、非空list等，就判断为True，否则为False。
if age:
    print('if') # 打印
else:
    print('else')

age = 0
if age:
    print('if')
else:
    print('else') # 打印

"""
input() 返回的是字符串
"""
age = input('请输入年龄：')
# if age < 0: # TypeError: unorderable types: str() < int()
#     print('不合法，年龄要大于0岁！')
# 因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
age = int(age)
if age < 0:
    print("error,don't < 0")