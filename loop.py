# for...in...循环，依次把list或tuple中的每个元素迭代出来，代入变量x，然后执行缩进块的语句
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)
print()

# 计算1-10的整数之和
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum + x
print(sum)
print()

# range()函数生成一个整数序列，再通过list()函数转换为list
print(list(range(5)))
print()

sum = 0
for x in range(101):  # range(101)生成0-100的整数序列
	sum = sum + x
print(sum)
print()

# 计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)
print()

L=['Bart','Lisa','Adam']
for a in L:
	print('Hello, '+a+'!')
print()

n = 1
while n <= 100:
    if n > 10:  # 当n=11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
print()

n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0:  # 如果n是偶数，条件满足，执行continue语句
		continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
	print(n)