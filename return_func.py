# 高阶函数还可以把函数作为结果值返回

# 可变参数的求和函数
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax
print(calc_sum(1,3,5,7,9))
print()

# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum  # 返回求和的函数sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
f1 = f()  # 调用函数f时，才真正计算求和结果
print(f1)
print()

# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)
print()

# 返回闭包时牢记：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
	fs = []
	for i in range(1, 4):  # 1 2 3
		def f():
			return i*i
		fs.append(f)
	return fs
f1, f2, f3 = count()
print(f1(),f2(),f3())  # 结果为9 9 9，而不是1 4 9
# 原因在于返回的函数引用了变量i，但并非立刻执行，
# 等到3个fs函数都返回时，它们所引用的变量i已经变成了3，因此最终结果均为9
print()

# 若一定要引用循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
	return fs
f1, f2, f3 = count()
print(f1(),f2(),f3())  # 结果为1 4 9