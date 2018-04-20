# map()函数接收两个参数，一个是函数，一个是Iterable，
# map()将传入的函数依次作用到Iterable序列的每个元素，并把结果作为新的Iterator返回
def f(x):
	return x * x
m = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(m)
print(list(m))  # r是一个Iterator惰性序列，因此通过list()函数把整个序列都计算出来并返回一个list
print()

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))  # 把list所有数字转为字符串
print()

# reduce()函数接收两个参数，把一个函数作用在一个序列[x1, x2, x3, ...]上，
# reduce()将函数对序列元素的运算结果，继续和序列的下一个元素做累积计算
# 即：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
	return x + y
r = reduce(add, [1, 3, 5, 7, 9])
print(r)
print()

from functools import reduce
def fn(x, y):
	return x * 10 + y
r = reduce(fn, [1, 3, 5, 7, 9])
print(r)
print()

# map和reduce结合使用
from functools import reduce
def fn(x, y):
	return x * 10 + y
def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]
r = reduce(fn, map(char2num, '13579'))  # map函数将字符串“13579”变为数字序列，reduce函数再将该数字序列进行fn的累积运算
print(r)