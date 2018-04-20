# 在Python中，不必创建完整的list，一边循环一边计算的机制，称为生成器：generator

L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))  # 把列表生成式的[]改成()，就创建了一个generator
print(g)
print()

print(next(g))  # 打印generator的每一个元素，使用next()函数获得generator的下一个返回值
print(next(g))	# 每next一次，指针便指向下一个元素
print(next(g))
print()
# generator保存的是算法，
# 每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，
# 没有更多的元素时，抛出StopIteration的错误

g = (x * x for x in range(10))
for n in g:  # 打印generator的每一个元素，更好的方式是使用for循环（generator也是可迭代对象）
	print(n)
print()

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：1, 1, 2, 3, 5, 8, 13, ...
def fib(max):  # 函数实现
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b  # 表示“a=b,b=a+b”，即”t = (b, a + b); a = t[0]; b = t[1];“，不必显式写出临时变量t就可以赋值
		n = n + 1
	return 'done'
fib(6)
print()

def fib(max):  # 生成器generator实现，把print(b)改为yield b，
	n, a, b = 0, 0, 1
	while n < max:
		yield b  # 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
		a, b = b, a + b
		n = n + 1
	return 'done'
f = fib(6)
print(f)  # 输出的是首地址
for n in fib(6):
	print(n)
print()
# 函数是顺序执行，遇到return语句或最后一行函数语句就返回；
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)
o = odd()
next(o)
next(o)
next(o)
next(o)
# odd是generator，在执行过程中，遇到yield就中断，下次又继续从此处开始执行
# 执行3次yield后，已经没有yield可以执行，所以第4次调用next(o)报错