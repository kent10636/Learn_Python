print(list(range(1, 11)))  # 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]（从1开始，不含11）
print()

L=[]
for x in range(1,11):  # 循环构造[1x1, 2x2, 3x3, ..., 10x10]的列表
	L.append(x*x)
print(L)
print()

# 写列表生成式时，把要生成的元素x*x放到前面，后面跟for循环，就可以把list创建出来
print([x * x for x in range(1, 11)])  # 列表生成式构造[1x1, 2x2, 3x3, ..., 10x10]的列表
print()

print([x * x for x in range(1, 11) if x % 2 == 0])  # for循环后面可以加上if判断，筛选出偶数的平方
print()

print([m + n for m in 'ABC' for n in 'XYZ'])  # 使用两层循环，生成全排列
print()

import os  # 导入os模块
print([d for d in os.listdir('.')])  # 列出当前目录下的所有文件和目录名
print()

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():  # 同时迭代dict的key和value
	print(k, '=', v)
print()

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])  # 列表生成式使用两个变量来生成list
print()

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])  # lower()函数把一个list中所有的字符串变成小写
print()

L = ['Hello', 'World', 18, 'Apple', None]  # 非字符串类型没有lower()方法
print([s.lower() for s in L if isinstance(s,str)])