print(abs(100))
print(abs(-20))
print(abs(12.34))
print()

max(1, 2)
max(2, 3, 1, -5)
print()

print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
print()

# 可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-1))
print()

# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号，
# 然后在缩进块中编写函数体，函数的返回值用return语句返回
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None，return None可以简写为return
def my_abs(x):
	if not isinstance(x, (int, float)):  # 数据类型检查用内置函数isinstance()实现
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

# 定义一个什么事也不做的空函数
# pass可以用来作为占位符
# 比如还没想好怎么写函数代码，可以先放一个pass，让代码能运行起来
def nop():
	pass

	
import math  # 导入math包，允许后续代码引用math包里的sin、cos等函数
def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
x, y = move(100, 100, 60, math.pi / 6)  # 返回多个值
print(x, y)
r = move(100, 100, 60, math.pi / 6)  # 其实只是一种假象，返回的仍然是单一值，是一个tuple
print(r)