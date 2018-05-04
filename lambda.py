# 不需要显式地定义函数时，直接传入匿名函数更方便
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数的限制：只能有一个表达式，返回值就是该表达式的结果，不用写return
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# lambda x: x*x ，即：
#def f(x):
#	return x * x
print()

f = lambda x: x * x
print(f)
print(f(5))
print()

# 匿名函数可以作为返回值返回
def build(x, y):
	return lambda: x * x + y * y
z=build(2,2)  # build()将函数2*2+2*2返回给z
print(z)  # z也成为一个函数，函数式为z()=2*2+2*2
print(z())