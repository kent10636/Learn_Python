# 把函数本身赋值给变量
f = abs
print(f)  # <built-in function abs>
print(f(-10))  # 变量f现在指向abs函数本身，直接调用abs()函数和调用变量f()完全相同
print()

# abs=10，把abs指向10后，就无法通过abs(-10)调用该函数了，因为abs这个变量已经不指向求绝对值函数而是指向一个整数10
# 要恢复abs函数，请重启Python交互环境

# 一个函数接收另一个函数作为参数，这种函数称为高阶函数
def add(x, y, f):
	return f(x) + f(y)
print(add(-5, 6, abs))  # 计算过程：x = -5; y = 6; f = abs; f(x) + f(y) ==> abs(-5) + abs(6) ==> 11; return 11