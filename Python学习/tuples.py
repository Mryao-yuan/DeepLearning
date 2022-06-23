# 元组的练习

"""不可变序列的增加元素操作"""
s = "hello"
print(s, id(s))
s += 'world'
print(s, id(s))

print('*** 元组的练习 ***')
# 第一种使用 ()
print('第一种使用 ()')
y = ('hello', 'world', 111)
print(y)
# 省略小括号
t1 = '123', 456, '12'
print(t1, type(t1))
# 第二种使用内置函数  tuple()
print('第二种使用内置函数  tuple()')
y = tuple(('hello', 'world', 111))

print(y)

# 只含又一个元组数据的时候
print('只含又一个元组数据的时候')
t = (1,)
print(t, type(t))
t = tuple(('1'))
print(t, type(t))

# 空数据结构的练习
print('======================= 空数据结构的练习==========')
# 空列表
print('*** 空列表 ***')
lst = []
lst1 = list()
print("lst:", lst, type(lst), "lst1", lst1, type(lst1))
# 空字典
print('*** 空字典 ***')
dct = {}
dct1 = dict()
print("dct:", dct, type(dct), "dct1", dct1, type(dct1))
# 空元组
print('*** 元组 ***')
t = ()
t1 = tuple()
print("t:", t, type(t), "t1", t1, type(t1))

# 元组的遍历
print('======================= 元组的遍历 ==========')
t = (10, 20, 30, 'hello', 'world')
for item in t:
    print(item)
