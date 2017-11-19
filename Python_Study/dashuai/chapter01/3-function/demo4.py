#!/usr/bin/env python3
# --*-- coding: utf-8 --*--

"""
函数的参数

定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了
函数内部的复杂逻辑被封装起来，调用者无需了解。

Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，
还可以简化调用者的代码
"""


"""
位置参数
"""
def power(x):
    return x * x
# 对于power(x)函数，参数x就是一个位置参数。当我们调用power函数时，必须传入有且仅有的一个参数x
print(power(2))

# 修改后的power1(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值必须要严格按照位置的顺序依次赋给参数x和n。
def power1(x, n):
    s = 1;
    while n > 0:
        s = s * x
        n -= 1

    return s
# 计算 5 的 2次方
print(power1(5, 2)) # 25


"""
默认参数
"""
# print(power1(5)) # ypeError: power1() missing 1 required positional argument: 'n'
# Python的错误信息很明确：调用函数缺少了一个位置参数n。
# 这个时候，默认参数就排上用场了
def power2(x, n = 2):
    return power1(x, n)

print(power2(2)) # 4
print(power2(2, 3)) # 8

#默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
# 二是如何设置默认参数。
#       当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
#       使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，也可以不按顺序提供部分默认参数。
def getStuInfo(name, age, sex = '男', city = 'Beijing'):
    print(name)
    print(age)
    print(sex)
    print(city)

getStuInfo('李磊', 21)
getStuInfo('韩梅梅', 20, '女')
getStuInfo('李梅', 21, '女', 'tianjin')
getStuInfo('李响', 21, city = 'tianjin') # 当不按顺序提供部分默认参数时，需要把参数名写上
getStuInfo('张丽', 21, city = 'tianjin', sex = '女') # 当不按顺序提供默认参数时，需要把参数名写上


"""
默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下
"""
# 参数为空list，默认参数
def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1, 2, 3])) # [1, 2, 3, 'END']
print(add_end()) # ['END']
print(add_end()) # ['END', 'END']
print(add_end()) # ['END', 'END', 'END']
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，
# 默认参数的内容就变了，不再是函数定义时的[]

"""
定义默认参数要牢记一点：默认参数必须指向不变对象！
"""
# 可以用None这个不变对象来实现
def add_end1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end1()) # ['END']
print(add_end1()) # ['END']
print(add_end1()) # ['END']

# 为什么要设计str、None这样的不变对象呢？
# 因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


"""
可变参数

在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
"""
# 定义函数，如果参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n

    return sum
# 但是调用的时候，需要先组装出一个list或tuple：

# 如果利用可变参数，调用函数的方式可以简化成这样：
def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n

    return sum
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3]
calc1(nums[0], nums[1], nums[2])
# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
calc1(*nums)
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


"""
关键字参数

可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。

而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
"""
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
person('Michael', 30) # name: Michael age: 30 other: {}

# 也可以传入任意个数的关键字参数：
person('Bob', 35, city='Beijing') # name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer') # name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

# 关键字参数有什么用？
# 它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
# 当然，上面复杂的调用可以用简化的写法：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，

##### 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


"""
命名关键字参数

对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
"""
def person1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass

    print('name:', name, 'age:', age, 'other:', kw)
# 但是调用者仍可以传入不受限制的关键字参数：
# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person2(name, age, *, city, job):
    print(name, age, city, job)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person2('Jack', 24, city='Beijing', job='Engineer') # Jack 24 Beijing Engineer
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# person3('Jack', 24, 'Beijing', 'Engineer')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: person() takes 2 positional arguments but 4 were given

# 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。


# 命名关键字参数可以有缺省值，从而简化调用：
def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)
# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
person4('Jack', 24, job='Engineer')


# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass



"""
参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数

这5种参数都可以组合使用。

但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。