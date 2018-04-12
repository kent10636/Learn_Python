classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print()

# 用len()函数可以获得list元素的个数
print(len(classmates))
print()

print(classmates[0])
print(classmates[1])
print(classmates[2])
print()

# -1做索引，直接获取list的最后一个元素
print(classmates[-1])
print(classmates[-2])  # 倒数第2个元素
print(classmates[-3])  # 倒数第3个元素
print()

# 往list可变有序表中追加元素到末尾
classmates.append('Adam')
print(classmates)
print()

# 把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates)
print()

# 删除list末尾的元素，用pop()方法
classmates.pop()
print(classmates)
print()

# 删除索引位置i的元素，用pop(i)方法
classmates.pop(1)
print(classmates)
print()

# 把某个元素替换成别的元素，直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)
print()

# list里面的元素的数据类型可以不同
L = ['Apple', 123, True]
print(L)
print()

# list元素也可以是另一个list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(len(s))  #长度为4，类似二维数组的概念
print()

# 空的list
emplylist = []
print(len(emplylist))

if __name__ == '__main__':
    pass