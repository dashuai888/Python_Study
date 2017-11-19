#!usr/bin/env python3

"""
字符串和字符的编码

字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。

因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。

最早的计算机在设计时采用8个bit作为一个byte，所以，一个字节能表示的最大的整数就是255，如果要表示更大的整数，就必须用更多的字节。
比如两个字节可以表示的最大整数是65535，4个字节可以表示的最大整数是4294967295。

由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，
比如大写字母A的编码是65，小写字母z的编码是122。

要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。

全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。
因此，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。

现在，捋一捋ASCII编码和Unicode编码的区别：

1、ASCII编码是1个字节，而Unicode编码通常是2个字节。

2、字母A用ASCII编码是十进制的65，二进制的01000001；

3、字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；

4、汉字 中 已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。

如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。
新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。
但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。

所以本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。
UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。
如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间
UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。

搞清楚了ASCII、Unicode和UTF-8的关系，就可以总结一下现在计算机系统通用的字符编码工作方式：

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器
所以你看到很多网页的源码上会有类似<meta charset="UTF-8" />的信息，表示该网页正是用的UTF-8编码
"""

"""
Python的字符串

在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
"""
print('大家好hahahaaha') # 大家好hahahaaha

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
a = ord('1') # 49
print(a)
a = chr(a) # '1'
print(a)
print(type(a)) # <class 'str'>，Python的字符串类型是str，在内存中以Unicode表示
# 一个字符对应若干个字节。如果要在网络上传输str，或者保存str到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
a = b'1'
print(a) # b'1'
print(type(a)) # <class 'bytes'>

a = b"1"
print(a)
print(type(a))

# b'1' 虽然内容显示得和 '1' 一样，但bytes的每个字符都只占用一个字节

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
a = '中文字符串'
print(a) # 中文字符串
# 含有中文的str可以用UTF-8编码为bytes。
a = a.encode('utf-8')
print(a) # b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'

a = '123'
print(a) # 123
# 纯英文的str可以用ASCII编码为bytes，内容是一样的
a = a.encode('ascii')
print(a) # b'123'

# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示

"""
反过来，如果从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
"""
a = b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
print(a) # b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
a = a.decode('utf-8')
print(a) # 中文字符串

# 如果bytes中包含无法解码的字节，decode()方法会报错
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
a = b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
print(a)
a = a.decode('ascii', errors='ignore') # 什么都不会打印

a = b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
print(a)
# a = a.decode('ascii') # 报错  UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)

"""
要计算str包含多少个字符，可以用len()函数
"""
print(len('1')) # 1
print(len('11')) # 2
print(len('中')) # 1

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
a = b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
print(a) # b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2'
print(len(a)) # 15
print(len(a.decode('utf-8'))) # 5 a 解码为 '中文字符串'
# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节

"""
在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。

由于Python源代码也是一个文本文件，所以，当源代码中包含中文的时候，在保存源代码时，就需要指定保存为UTF-8编码。

当Python解释器读取源代码时，为了让它按UTF-8编码读取，通常在文件开头写上这两行：

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则在源代码中写的中文输出可能会有乱码。

!!!!! 申明UTF-8编码并不意味着 .py 文件就是UTF-8编码，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：
"""

"""
格式化

最后一个常见的问题是如何输出格式化的字符串。

% 运算符用来格式化字符串。

在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号(元组)可以省略
"""
# 在Python中，采用的格式化方式和C语言是一致的，用%实现
a = 'dashuai'
print('hi, %s' % a) # hi, dashuai
print('%s, %d' % (a, 666)) # dashuai, 666

# 常见的占位符有：
#
# 占位符	替换内容
# %d	    整数
# %f	    浮点数
# %s  	字符串
# %x	    十六进制整数

# 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%02d' % 1) # 表示用2位表示，不足2位的补0
# 01
print('%02d' % 11)
# 11
print('%2d' % 1) # 1 虽然也是1，但是位数为2位
#  1
print('%.3f' % 1)
# 1.000
print('%.3f' % 3.141592653)
# 3.142

"""
如果不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
"""

"""
有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
"""
print('增长率是%d%%' % 100) # 增长率是100%

"""
format()

另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多
"""

