# filter()接收一个函数和一个序列，用于过滤序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

def is_odd(n):
	return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))  # 在一个list中，删掉偶数，只保留奇数
print()

def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))  # 在一个list中，删掉空字符串
print()

def _odd_iter():  # 从3开始的无限奇数序列的构造函数
	n = 1
	while(True):
		n = n + 2
		yield n  # yield函数在每次循环都类似return返回yield后面紧跟着的值n
def _not_divisible(n):  # 返回筛选函数x%n>0
	return lambda x: x % n > 0  # lambda表示匿名函数，即：输入的是x，函数为x%n>0
def primes():
	yield 2  # 返回2
	it = _odd_iter() # 生成初始序列
	while(True):
		n = next(it)  # 获得序列中的下一个值
		yield n  # 返回序列的第一个数
		it = filter(_not_divisible(n), it) # filter过滤it序列，构造新序列
for n in primes():
	if n < 100:
		print(n)
	else:
		break