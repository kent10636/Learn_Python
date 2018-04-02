# 用r''表示''内部的字符串默认不转义
print('\\\t\\\n\\')
print(r'\\\t\\\n\\')

# 用'''xxx'''的格式表示多行内容
print('''line1
line2
line3
line4''')

# 布尔值True和False(注意大小写)
print(True)
print(False)
print(3 > 2)
print(3 > 5)

# 布尔运算,and or not
print(True and True)
print(True and False)
print(False and False)
print(5 > 3 and 3 > 1)
print(True or True)
print(True or False)
print(False or False)
print(5 > 3 or 1 > 3)
print(not True)
print(not False)
print(not 1 > 2)

# 布尔运算用于条件判断
age=int(input('please enter the age: '))
if age >= 18:
    print('adult')
else:
    print('teenager')

# None表示空值,不能理解为0
print(None)

# /除法计算结果是浮点数
print(9 / 3)
# //除法(地板除)计算结果仍是整数,即使除不尽
print(10 // 3)

