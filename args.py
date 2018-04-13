# 必选参数在前，默认参数在后
# 函数有多个参数时，变化大的参数放前面，变化小的参数放后面
def power(x, n=2):  # 可以把第二个参数n的默认值设定为2
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print(power(5))
print(power(5,3))
print()

def enroll(name, gender, age=6, city='Beijing'):  # 把年龄和城市设为默认参数
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)
enroll('Sarah', 'F')
enroll('Bob', 'M', 7)  # 按顺序提供默认参数，除了name，gender外，最后1个参数用在参数age上，city参数由于没有提供，仍然使用默认值
enroll('Adam', 'M', city='Tianjin')  # 不按顺序提供部分默认参数，需要把参数名写上
print()

# Python函数在定义时，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
print(add_end())
print(add_end())
print()

# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
# 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
nums = [1, 2, 3]
print(calc(*nums))
print()

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，这个dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
print()

# 限制关键字参数的名字，可以用命名关键字参数，例如只接收city和job作为关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person1(name, age, *, city='Beijing', job):  # 命名关键字参数可以有缺省值
	print(name, age, city, job)
person('Jack', 24, city='Shanghai', job='Engineer')  # 命名关键字参数必须传入参数名
person('Jack', 24, job='Engineer')  # 由于命名关键字参数city具有默认值，调用时可不传入city参数

# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。