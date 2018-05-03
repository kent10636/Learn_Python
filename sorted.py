# Python内置的sorted()函数对list排序
print(sorted([36, 5, -12, 9, -21]))
print()

# sorted()也是高阶函数，可以接受一个key实现自定义排序
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted([36, 5, -12, 9, -21], key=abs))  # 按绝对值排序
print()

# 字符串排序，按照ASCII的大小比较，由于'Z' < 'a'，因此大写字母Z会排在小写字母a之前
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print()

# 若想使排序忽略大小写，按字母序排序，只要用一个key函数把字符串映射为忽略大小写排序即可
# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或都变成小写），再比较
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))  # key表示都变成小写再排序（但实际上原列表元素的大小写不变，只是排序时临时变成小写）
print()

# 反向排序应传入参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
print()