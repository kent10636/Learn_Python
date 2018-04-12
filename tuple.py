# tuple就是把list的[]改为()
# tuple一旦初始化就不能修改，也没有append()，insert()等方法
# 获取元素的方法和list是一样的，使用classmates[0]，classmates[-1]
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print()

# 空的tuple
t=()
print(t)
print()

# 只有1个元素的tuple
# 不能写成t=(1)，因为括号()既可以表示tuple，又可以表示数学公式中的小括号，产生了歧义，Python规定，这种情况下，按小括号进行计算，计算结果自然是1
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)
print()

# tuple的“不变”是说，tuple的每个元素指向永远不变，
# 即指向'a'，就不能改成指向'b'；指向list，就不能改成指向其他对象，但指向的这个list本身是可变的！
# tuple的元素没有变，变的是tuple中list的元素
t=('a','b',['A','B'])
t[2][0]='X'
t[2][1]='Y'
print(t)