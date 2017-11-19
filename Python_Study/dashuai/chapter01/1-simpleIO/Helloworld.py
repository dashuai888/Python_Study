#!/usr/bin/env python3

# 命令行直接运行py文件的方法
# 在Windows上是不行的，但是在Mac和Linux上可以，方法是在.py文件的第一行加上一个特殊的注释

# 在linux命令行运行Python，需要通过命令给x.py以执行权限：
# chmod 744 x.py

# 用print()在括号中加上字符串，就可以向屏幕上输出指定的文字。
print('hello, world')  # hello, world

# print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出，print()会依次打印每个字符串，遇到逗号“,”会输出一个空格
print('wang', 'da', 'shuai')  # wang da shuai

# print()也可以打印整数，或者计算结果，这个功能最给力，直接就是一个计算器啊！
print(1 + 2) # 3
print(1111) # 1111

# 如果就想打印计算公式的字符串形式，就加引号
print('1 + 2') # 1 + 2

# Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里。比如输入用户的名字：
name = input()
print(name)
# 当解释器执行到name = input()，就会等待输入。这时，你可以输入任意字符，然后按回车后完成输入。

# 但是程序运行的时候，没有任何提示信息告诉用户，显得很不友好。
# input()可以显示一个字符串来提示用户
name = input('输入姓名：') # 运行，首先打印出 输入姓名：
print(name)

# 输入姓名：大帅
# 大帅



