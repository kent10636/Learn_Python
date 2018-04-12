age = 3
if age >= 18:  # 注意不要少写了冒号:
	print('adult')
elif age >= 6:  # elif是else if的缩写
	print('teenager')
else:
	print('kid')
print()
	
s = input('birth: ')
birth = int(s)  # input()返回的数据类型是str，str不能直接和整数比较，必须先使用int()函数把str转换成整数
if birth < 2000:
	print('00前')
else:
	print('00后')
print()

height=1.75
weight=80.5
bmi=float(weight)/(float(height)*float(height))
if bmi<18.5:
	print('过轻')
elif 18.5<=bmi<=25:  # 这也行的？经过验证，可以！
	print('正常')
elif 25<=bmi<28:
    print('过重')
elif 28<=bmi<=32:
    print('肥胖')
elif bmi>32:
    print('严重肥胖')
else:
	pass