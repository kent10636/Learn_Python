d = {'a': 1, 'b': 2, 'c': 3}
for key in d:  # 迭代dict，默认情况下dict迭代的是key
	print(key)  # 因为dict的存储不是按照list的方式顺序排列，所以迭代出的结果顺序可能不一样
print()

for value in d.values():  # 迭代dict的value
	print(value)
print()
	
for k, v in d.items():  # 同时迭代dict的key和value
	print(k)
	print(v)
print()

for ch in 'ABC':  # 字符串也是可迭代对象
	print(ch)
print()

# 只要for循环作用于一个可迭代对象，就可以正常运行，我们不关心该对象究竟是list还是其他数据类型

from collections import Iterable  # 通过collections模块的Iterable类型判断是否可迭代
print(isinstance('abc', Iterable))  # str是否可迭代 -> True
print(isinstance([1,2,3], Iterable))  # list是否可迭代 -> True
print(isinstance(123, Iterable))  # 整数是否可迭代 -> False
print()

for i, value in enumerate(['A', 'B', 'C']):  # 使用enumerate函数把list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身，实现类似Java的下标循环
	print(i, value)
print()

for x, y in [(1, 1), (2, 4), (3, 9)]:  # for循环中同时引用两个变量
	print(x, y)