# 列表
# 列表的创建
lst = [1, 'hello', 'world']
print(id(lst))
print(type(lst))
print(id(lst[0]))
print(id(lst[1]))
print(id(lst[2]))
print('列表的创建')
# 第一种创建方式
lst = ['1', '2', 'world', '3', '4', 'world']
# 第二种创建方式
lst1 = list(['1', '2'])
print('lst:', lst)
print('lst2:', lst)
print(type(lst))
print(type(lst[1]))
# 索引
print('指定元素的索引')
print(lst. index('world'))  # 列表的操作故是 . 不是 ，
print(lst. index('world', 3, 6))
# 索引为 2 的值
print(lst[2])
# 索引为 -1 的值
print(lst[-1])
# 切片操作
print('*** 切片操作 ***')
lst = [10, 20, 30, 40, 50, 60, 70]
lst2 = lst[1:6:1]
print(lst)
print('原列表ID:', id(lst))
print(lst2)
print('切的片段:', id(lst2))
print('步长为2')
lst3 = lst[1:6:2]
print(lst3)
# 省略步长：默认 1
lst4 = lst[1:6]
print("省略步长:", lst4)
# 省略start:默认0
lst5 = lst[:6:2]
print("省略start:", lst5)
# 省略stop: 默认结局
lst6 = lst[1::2]
print("省略stop:", lst6)
# step 为负数
print('=============== step 为负数===================')
print('原列表:', lst)
lst1 = lst[::-1]
print('step 为 -1:', lst1)
# 列表元素的遍历
print('===============列表元素的遍历=================')
for item in lst:
    print(item, end='\t')
# 列表元素的添加
print('===============列表元素的添加=================')
# append
lst = list([1, 2, 3, 4])
lst2 = ['hello', 'world']
print('append 的使用')
print('before:', lst, id(lst))
lst.append(5)
print('now:', lst, id(lst))
lst.append(lst2)
print(lst)
# extend
print('extend 的使用')
print('before:', lst, id(lst))
lst.extend(lst2)  # extend 是将元素分开插入列表中，append是将整个列表作为元素插入列表中
print('now:', lst, id(lst))
# insert
print('insert 的使用')
lst.insert(1, 20)
print(lst)
# 切片的使用
lst[1:] = lst2  # 没有写结束，lst的第一个开始放入lst2
print(lst)
# 列表的删除
print('***  列表的删除 ***')
lst = [1, 2, 3, 4, 5, 6]
# remove 的使用
print('remove 的使用')
print('before:', lst)
lst.remove(2)
print("new:", lst)
# pop 的使用
print('pop 的使用')
print('before:', lst)
lst.pop(0)
print("new:", lst)
lst.pop()
print("未指定元素：", lst)
# 切片操作
print('*** 切片操作---删除至少一个元素,将产生新的列表对象 ***')
lst = [1, 2, 3, 4, 5, 6]
new_list = lst[1:5]
print('before:', lst)
print('now:', new_list)
print('切片操作,不产生新列表:只是将删除的地方用空列替代')
lst[1:5] = []
print(lst)
# 清除列表 clear
print('清除列表---clear')
print(lst)
lst.clear()
print(lst)
# 删除列表
'''
print('删除列表---del')
print(lst)
del(lst)
print(lst)
'''
# 列表元素的修改操作
print('列表元素的修改操作')
lst = [10, 20, 30, 40, 50, 30]
print("before:", lst)
# 一次修改一个值
print('一次修改一个值')
lst[0] = 100
print('new:', lst)
print('一次修改多个值')
lst[1:] = [200, 300, 400, 500, 600]
print('new:', lst)

# 排序操作
print("*** 列表的排序操作 ***")
lst = [1, 2, 4, 10, 3, 5]
print('before:', lst, id(lst))
lst.sort()
print('new:', lst, id(lst))
lst.sort(reverse=True)
print('降序:', lst, id(lst))

print('sorted 操作')
lst1 = sorted(lst, reverse=False)
print('lst1:', lst1, id(lst1))
# 列表生成
print('列表的生成')
lst = [item for item in range(0, 10, 2)]
print(lst)
