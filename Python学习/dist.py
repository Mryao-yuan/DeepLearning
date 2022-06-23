# 字典的学习
print('字典的练习')
# 字典的创建
print('*** 字典的创建 ***')
'''第一种创建方式 {}'''
score = {'jack': 100, 'ryan': 200}
print(score, type(score))
'''第二种创建方式 dict'''
student = dict(name='jack', age=23)
print(student, type(student))
# 字典的元素获取
print('字典的元素获取')
print('使用 []')
print(score['jack'])
# print(score['ja'])
print('使用 get()')
print(score.get("jack"))
print(score.get("jck"))
# 字典的常用操作
print('字典的常用操作')
# 键的判断
print('键的判断')
print(score)
print('jack in score:', 'jack' in score)
print('tom not in score:', 'jack' not in score)
# 元素的删除
print('键的删除')
del score['jack']
print(score)
# 元素的增加
print('*** 元素的增加 ***')
score['tom'] = 346
print(score)
# 字典获取视图的办法
print('字典获取视图的办法')
score = {'jack': 100, 'ryan': 200}
# 获取所有的 key
print('获取所有的 key')
keys = score.keys()
print(type(keys))
print(list(keys))
# 获取所有的 value
print('获取所有的 value')
keys = score.values()
print(type(keys))
print(list(keys))
# 获取所有的键值对
print('获取所有的键值对')
print(score)
item = score.items()
print(type(item))
print(list(item))
# 字典的特点
# key 不允许重复
score = {'Jack': 100, "jack": 200}
print(score)
# 字典生成式
print('字典生成式')
item = ['fruit', 'vegetable', 'juice']
price = [100, 200, 300]
lst = zip(item, price)
print(list(lst))

# 整体输出
print("整体输出")
goods = {item: price for item, price in zip(item, price)}
print(goods)
