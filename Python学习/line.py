# 程序的顺序
print('===程序的顺序结构===')
# 对象的布尔值
print('对象的布尔值')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(list()))  # 空列表
print(bool([]))  # 空列表
print(bool(()))  # 空元祖
print(bool(tuple()))  # 空元祖
print(bool([]))  # 空字典
print(bool(set()))  # 空集合
print('======其他的对象的布尔值均为True')
print('============单分支结构==========')
money = 100
s = int(input('输入取出金额:'))
if money >= s:
    print('取款成功,余额:', money - s)
print('============双分支结构==========')
money = 100
s = int(input('输入取出金额:'))
if money >= s:
    print('取款成功,余额:', money - s)
else:
    print('取出金额超过余额')
print('============多分支结构==========')

mark = int(input('输入考试成绩:'))
if mark >= 90 and mark <= 100:
    print('取得 A')
elif mark >= 80 and mark <= 89:
    print('取得 B')
elif mark >= 70 and mark <= 79:
    print('取得 C')
elif mark >= 60 and mark <= 69:
    print('取得 C')
elif mark < 60 and mark >= 0:
    print('不及格')
else:
    print('非法输入')
# 嵌套 if
print('--- 嵌套 if的使用---')
card = int(input('\n输入是否是会员:'))
money = int(input('输入购买的金额:'))
if card == 1:
    if money > 1000:
        money *= 0.8
    else:
        money *= 0.9
else:
    pass
print('最后的金额为 :', money)
# 条件表达式
print('--- 条件表达式的使用 ---')
num_a = int(input('输入第一个整数:'))
num_b = int(input('输入第二个整数:'))

#   if num_a > num_b:
#        print(num_a, '大于', num_b)
#    else
#        print(num_a, '小于等于',num_b)

print(str(num_a) + ' 大于 ' + str(num_b) if num_a >
      num_b else str(num_a) + ' 小于 '+str(num_b))
# pass 语句
print('--- pass 语句的使用 ---')
answer = input('你是会员吗？')
if answer == 'y':
    pass
else:
    print('该充钱了！')
# range 函数的使用
print('*** range 函数的使用 ***')

'''
# 第一种创建方式
'''
print('第一种方式:')
r = range(10)
print(list(r))

'''
# 第二种创建方式
'''
print('第二种方式:')
r = range(1, 12)
print(list(r))
'''
# 第三种创建方式
'''
print('第三种方式:')
r = range(1, 12, 2)  # start  stop step
print(list(r))
print('10 在 range(1,12,2):', 10 in list(r))
# while 的使用
print('*** while 的使用 ***')
print('计算 x ~ 100 的和')
sum = 0
a = int(input('输入一个数字:'))
print(a, '到 100 的值为:')
while a < 100:
    a += 1
    sum += a
print(sum)
# while 的练习 1~100 之间的偶数和
print('while 的练习 1~100 之间的偶数和')
a = 1
sum = 0
while a <= 100:

    if a % 2 == 0:
        sum += a
    else:
        pass
    a += 1
print('1~100 之间的偶数和为:', sum)
# for-in 的使用
print('*** for-in 的使用 ***')
for item in 'python':
    print(item)
# 用整数作为可迭代对象
for i in range(10):
    print(i)
# 不需要使用自定义变量，使用 _
for _ in range(2):
    print('helloWorld')
# 通过 for-in 计算 1~100 的偶数和
print('通过 for-in 计算 1~100 的偶数和')
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
    else:
        pass
print('结果为:', sum)

# for-in 练习 输出 100 ~ 999之间的水仙花数
# 水仙花数：153=1^3+5^3+3^3
print('输出 100 ~ 999之间的水仙花数:')
for i in range(100, 1000):
    b = i // 100
    s = i // 10 % 10
    g = i % 10
    if(i == g*g*g+s*s*s+b*b*b):
        print(i)
    else:
        pass

# 流程控制语句 break
print('*** 流程控制语句 ***')
times = 0
for ietm in range(3):
    pwd = input('输入密码:')
    if pwd == '888':
        print('输入正确')
        times += 1
        break
    else:
        print('密码不正确')
        times += 1
if times == 3:
    print('超过三次锁住')
# 流程控制语句 continue
print('*** continue 使用 输出 1~50 之间可以被 5 整除的数 ***')
for item in range(1, 50):
    if(item % 5 != 0):
        continue
    print(item)
# 嵌套循环
print('*** 嵌套循环的使用 ***')
print('输出三行四列的矩形')
for i in range(1, 4):  # 行表，执行三次
    for j in range(1, 5):  # 个数，四个
        print('*', end='\t')  # 不换行输出
    print('\n')
# 输出指教三角新
print('输出直角三角形')
for i in range(1, 6):  # 5行
    for j in range(1, i+1):  # i+1
        print('*', end='')
    print()
# 输出 九九乘法表
print('九九乘法表的输出')
for i in range(1, 10):
    for j in range(1, i+1):  # i +1
        print(i, '*', j, '=', i*j, end='\t')
    print("\n")
# 二重循环中的 break 和 continue
print("二重循环中的 break 和 continue")
print('*** break ***')
for i in range(1, 6):
    for j in range(1, 11):
        if j % 2 == 0:
            break
        print(j, end='\t')
    print()
print('*** continue ***')
for i in range(1, 6):
    for j in range(1, 11):
        if j % 2 == 0:
            continue
        print(j, end='\t')
    print()
