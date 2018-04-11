# Python的字符串支持多语言
print('包含中文的str')
print()

# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print()

# 可以通过字符的整数编码，用十六进制来写字符串
print('\u4e2d\u6587')
print()

# bytes类型的数据用带b前缀的单引号或双引号表示
x = b'ABC'
print(x)
print()
# Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# 注意区分'ABC'和b'ABC'，前者是str，后者是bytes(虽然内容显示和前者一样，但每个字符都只占用一个字节)。

# str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print()

# bytes通过decode()方法可以变为str
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print()

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print()

# 用len()函数计算str的字符数
print(len('ABC'))
print(len('中文'))
print()

# 用len()函数计算bytes的字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
print()

# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码。
# 如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文。

# %s表示用字符串替换，%d表示用整数替换，%f表示用浮点数替换。
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。
# 如果只有一个%?，括号可以省略。
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)
print()

# 使用字符串的format()方法来格式化字符串，它会用传入的参数依次替换字符串内的占位符{0}、{1}……
# {1:.1f}表示替换第2个占位符，且该位置填入的是保留小数点后1位小数的浮点数
print( 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

if __name__ == '__main__':
    pass