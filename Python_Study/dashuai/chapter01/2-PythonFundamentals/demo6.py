#!/usr/bin/env python3
# --*-- coding: utf-8 --*--

"""
循环
"""

# 计算1+2+3+ ... + 10
sums = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sums += x
print(sums) # 55

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
sums = 0
sumsTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for x in sumsTuple:
    sums += x
print(sums) # 55

# 要计算1-100的整数之和，从1写到100有点困难，Python提供了一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
# 比如range(5)生成的序列是从0开始小于5的整数，前闭后开区间
print(range(5)) # range(0, 5)
print(list(range(5))) # [0, 1, 2, 3, 4]

sums = 0
for x in range(101):
    sums += x
print(sums) # 5050


# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环
sums = 0
n = 99
while n > 0:
    sums += n
    n -= 2
print(sums) # 2500 计算100以内所有奇数之和


# break
# 在循环中，break语句可以提前退出循环
sums = 0
n = 99
while n > 0:
    if n < 50:
        break # n < 50 ， break语句会结束当前循环

    sums += n
    n -= 2
print(sums) # 1875 计算50-100以内所有奇数之和


# continue
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    print(n) # 打印 0 到 9
    n += 1

# 如果只想打印奇数
n = 0
while n < 10:
    if n % 2 == 0:
        n += 1
        continue

    print(n)
    n += 1


"""
有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。
"""

