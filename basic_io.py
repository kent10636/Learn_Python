print('hello, world')
print("hello, world")
# print()中使用单引号、双引号无区别

print('The quick brown fox','jump over','the lazy dog')
print('The quick brown fox''jump over','the lazy dog')
# 遇到逗号","会输出一个空格,否则直接拼接

print(300)
print(100+200)
print('100 + 200 =',100+200)
# 也可在print()中进行计算

name=input()
# 等待输入

name
print(name)
# 输出变量name的内容

name=input('please enter your name: ')
# input中允许打印显示一个字符串来提示用户
print('hello,',name)