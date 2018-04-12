# set和dict类似，是一组key的集合，但不存储value
s = set([1, 2, 3])
print(s)  # 显示的{1, 2, 3}只表示set内部有1、2、3这3个元素，显示的顺序也不表示set是有序的
print()

# 重复元素在set中自动被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)
print()

# 通过add(key)方法添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
s.add(4)
print(s)
print()

# 通过remove(key)方法删除元素
s.remove(4)
print(s)
print()

# set可以看成数学意义上的有序和无重复元素的集合
# 因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # 交集符号是&
print(s1 | s2)  # 并集符号是|
print()

# set和dict的唯一区别仅在于没有存储对应的value

# 对于可变对象list，对list进行操作，list内部的内容会变化
a = ['c', 'b', 'a']
a.sort()  # sort()用于排序
print(a)
print()

# 对于不可变对象str，调用对象自身的任意方法，不会改变该对象自身的内容。
# 这些方法会创建新的对象并返回，这样保证了不可变对象本身永远是不可变的
a = 'abc'
print(a)
print(a.replace('a', 'A'))  # 对str使用replace()方法，确实变出了'Abc'，但变量a最后仍是'abc'
print(a)
print()

# a本身是一个变量，它指向的对象的内容才是字符串对象'abc'
# 当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，
# 这个replace方法没有改变字符串'abc'的内容，而是创建了一个新字符串'Abc'并返回，
# 变量b指向该新字符串'Abc'，变量a仍指向原有的字符串'abc'
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)