# 集合的练习
print('=================== 集合的练习 =================')
# 集合的创建
print('*** 集合的创建 ***')
print('使用 {} ')
s = {1, 2, 3, 'Hello', 'World', 1}
print(s)
s = set(range(11))
print('使用 set')
print(s, type(s))
lst = [1, 2, 3, 4, 5]
print('列表变成集合')
print(lst, type(lst))
s2 = set(lst)
print(s2, type(s2))
print('字符串变成集合')
s3 = 'python'
print(s3, type(s3))
s3 = set(s3)
print(s3, type(s3))
# 定义空集合
s4 = set()
print('空集合:', s4, type(s4))
# 集合的操作
print("*** 集合的操作 ***")
s = set(range(1, 11))
# 判断操作
print("--- 判断操作 ---")
print('s:', s, type(s))
print("100 in s:", 100 in s)
print("100 not in s:", 100 not in s)
# 添加操作
print('=== 添加操作 === ')
s.add('helloWorld')
print(s)
s.update({'hello', 'world'}, [100, 20])
print(s)
# 删除操作
print("=== 删除操作 === ")
# 1. remove
print('1.remove')
s.remove('hello')
print(s)
# 2. discard
print('2.discard')
s.discard('world1')
print(s)
# 3. pop
print('3. pop')
s.pop()
print(s)
# 4. clear
print('4. clear')
s.clear()
print(s)

# 集合间的关系
print('===================== 集合间的关系 =========================')
# 相等与否
set_1 = set(range(10))
set_2 = set(range(11))
print('相等与否')
print('set_1', set_1)
print('set_2', set_2)
print('set_1 == set_2:', set_1 == set_2)
print('set_1 != set_2:', set_1 != set_2)
print('超集')
print('set_1 是 set_2 的子集:', set_1.issubset(set_2))
print('set_1 是 set_2 的超集:', set_1.issuperset(set_2))
print('交集')
print('set_1 和 set_2 是否没有交集:', set_1.isdisjoint(set_2))
# 集合的数学操作
print('++++++++++++++++ 集合的数学操作 ++++++++++')
set_2.add(100)
print('set_1:', set_1)
print('set_2:', set_2)
# 1.交集
print('1.交集: intersection  &')
print(set_1.intersection(set_2))
print(set_1 & set_2)
print(set_1)
print(set_2)
# 2.并集
print('2.并集: union |')
print(set_1.union(set_2))
print(set_1 | set_2)
print(set_1)
print(set_2)
# 3.差集
print('3.差集: difference -')
print(set_2.difference(set_1))
print(set_2 - set_1)
print(set_1)
print(set_2)
# 4.对称差集
print('4.对称差集: symmetric_difference ^')
print(set_1.symmetric_difference(set_2))
print(set_1 ^ set_2)
print(set_1)
print(set_2)

# 列表生成式
l = [item for item in range(1, 11)]
print(l)
# 集合生成式
s = [item for item in range(1, 11)]
print(s)
