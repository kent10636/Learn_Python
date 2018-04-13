# 理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰
# 使用递归函数需要注意防止栈溢出。
# 函数调用是通过栈（stack）这种数据结构实现的，
# 每进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以递归调用的次数过多，会导致栈溢出。
def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)
print(fact(1))
print(fact(5))
print(fact(100))
print()

# 解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归是指，在函数返回的时候调用自身本身，且return语句不能包含表达式。
# 这样，编译器或解释器就可以对尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
# 然而Python没有对尾递归做优化，故尾递归方式仍会栈溢出。
def fact(n):
	return fact_iter(n, 1)
def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)