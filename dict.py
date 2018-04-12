# Python内置字典：dict，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Michael'])
print()

# 除了初始化时指定外，还可以通过key将数据放入dict
d['Adam'] = 67
print(d['Adam'])
d['Adam'] = 90
print(d['Adam'])
print(d)
print()

# 通过in判断key是否存在
print('Thomas' in d)
print()

# 通过dict提供的get()方法判断key是否存在
print(d.get('Thomas'))  # 如果key不存在，返回None
print(d.get('Thomas', -1))  # 如果key不存在，返回自己指定的value
print()

# 用pop(key)方法删除一个key，这个key对应的value也会从dict中删除
d.pop('Bob')
print(d)
print()

# 注意：dict内部存放的顺序和key放入的顺序是没有关系的！
#       dict是用空间来换取时间的一种方法
#       dict的key必须是不可变对象，list是可变的，不能作为key
#       通过key计算位置的算法称为哈希算法（Hash）

