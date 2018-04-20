# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

# 使用isinstance(xx,Iterable)判断一个对象是否是Iterable对象
from collections import Iterable
print(isinstance([], Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance('abc', Iterable))  # True
print(isinstance((x for x in range(10)), Iterable))  #True
print(isinstance(100, Iterable))  # False
print()

# 使用isinstance(xx,Iterator)判断一个对象是否是Iterator对象
from collections import Iterator
print(isinstance([], Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance('abc', Iterator))  # False
print(isinstance((x for x in range(10)), Iterator))  # True
print(isinstance(100, Iterator))  # False
print()

# 使用iter()函数把list、dict、str等Iterable变成Iterator
print(isinstance(iter([]), Iterator))  # True
print(isinstance(iter({}), Iterator))  # True
print(isinstance(iter('abc'), Iterator))  # True

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# list、dict、str虽然是Iterable，却不是Iterator
# 因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误
# 可以把这个数据流看做是一个有序序列，但不能提前知道序列长度，只能不断通过next()函数按需计算下一个数据

# Python的for循环本质上就是通过不断调用next()函数实现的