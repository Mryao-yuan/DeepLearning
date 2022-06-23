import keyword
from decimal import Decimal
print('helloWorld')
# 输出到文件
fp = open('text.text', 'a+')
print('helloworld', file=fp)
fp.close()
# 转义字符
print('老师说：\'大家好\'')
print('http:\\\\www.baidu.com')
# 原字符
print(r'http:\\\\www.baidu.com')
# 字符编码 0b : 表示二进制
print(chr(0b100111001011000))
print(ord('乘'))
# 输出保留字
print(keyword.kwlist)
# 变量定义和使用
name = 'Ryan'
print('\n', name)
print('标识', id(name))
print('类型', type(name))
print('值', name)
# 变量的多次使用
name = 'jack'
print(name)
# 整数类型
n1 = 100
n2 = 0
n3 = -100
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))
# 二/八/十/十六进制
print('十进制', 118)
print('八进制', 0o1650)
print('十六进制', 0xFFFF)
print('二进制', 0b11100)
# 浮点类型
float1 = 1.1
float2 = 2.2
print(float1+float2)
# 提高精确度
print(Decimal('1.1')+Decimal('2.2'))
# 布尔类型
f1 = True
f2 = False
print(f1+1)
print(f2+1)
# 字符串类型
str1 = '人生苦短,我用python'
str2 = "人生苦短,我用python"
str3 = """人生苦短,
我用python"""
str4 = '''人生苦短,
我用python'''
print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))
print(str4, type(str4))
# 数据类型转换
print('=================类型转换=====================')
name = 'jack'
age = 22
print(type(name), type(age))
# str 转化
print('我叫'+name+',今年'+str(age))
print('其他类型转化为 str 类型')
a = 10
b = 1.1
c = True
print(a, ':', type(a), '\b', b, ':', type(b), '\b', c, ':', type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))
print("======其他类型转化为int 类型=====")
a = '123'
b = 1.1
c = True
d = "hello"
print(a, ':', type(a), '\b', b, ':', type(b),
      '\b', c, ':', type(c), d, ':', type(d))
print(int(a), int(b), int(c), type(int(a)), type(int(b)), type(int(c)))
print("======其他类型转化为float 类型=====")
a = '12'
b = 123
c = True
d = "hello"
print(a, ':', type(a), '\b', b, ':', type(b),
      '\b', c, ':', type(c), d, ':', type(d))
print(float(a), float(b), float(c), type(
    float(a)), type(float(b)), type(float(c)))
# 输入函数的使用
print('===输入函数的使用====')
name = input('你叫什么名字:')
print('\n', name, type(name))
# 从键盘获取两个整数并且计算和
print('\n', '===求和计算===')
num1 = input('数值a:')
num2 = input('数值b:')
print(num1, '+', num2, '=', int(num1)+int(num2))

# 算术运算符
print('===算术运算符号的使用===')
a = 10
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # 除法
print(a//b)  # 整除(取整数)
print(a % 2)  # 取余运算
print(a**b)  # 幂运算
print('===一正一负取整===')
print(-9//-4)
print(9//-4)
# 赋值运算符
print('===赋值运算符的使用===')
a, b, c = 10, 20, 30  # 系列解包的使用
print('a=', a, 'b=', b, 'c=', c)
print('系列解包至交换两个值')
a, b = 10, 20
print('交换之前:', a, b)
a, b = b, a
print('交换之后:', a, b)
a = b = c = 20  # 链式赋值(a,b,c的id指向同一个位置)
print('a:', id(a), 'b:', id(b), "c:", id(c))
# 比较运算符
print('===比较运算符的使用===')
print('1 > 20 =', 1 > 20)
print('1 < 20 =', 1 < 20)
a = 12
b = 20

print('a==b:', a == b)  # 值比较
print('a is b :', a is b)  # 标识比较

lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print('lst1 == lst2', lst1 == lst2)
print('lst1 is lst2', lst1 is lst2)
print('lst1 is not lst2', lst1 is not lst2)
print('lst1_id:', id(lst1), 'lst2_id:', id(lst2))

# 布尔运算符
print('===布尔运算符===')
a, b = 1, 2
print('======and=========')
print(a == 1 and b == 2)  # true     true and true --> true
print(a == 1 and b < 2)  # false     true and false --> false
print(a != 1 and b == 2)  # fasle     false and true --> true
print(a != 1 and b != 2)  # false     false and false  --> false


print('======or=========')
print(a == 1 or b == 2)  # true      true or ture --> true
print(a == 1 or b < 2)  # true       true or false --> true
print(a != 1 or b == 2)  # true      false or true --> true
print(a != 1 or b != 2)  # false     false or false --> false
print('====== not =========')
f = True
f1 = False
print('f=True,not f :', not f)
print("f1 = false,not f1: ", not f1)
print('=== in and not in ===')
s = 'helloworld'
print('k is in ', s, ':', 'k' in s)
print('h is in ', s, ':', 'h' in s)
print('k is not in ', s, ':', 'k' not in s)
print('h is not in ', s, ':', 'h' not in s)
# 位运算
a = 4
b = 8
print('===位运算===')
print(a, '&', b, '=', a & b)
print(a, '|', b, '=', a | b)
print(a, '<<', b, '=', a << b)
print(a, '>>', b, '=', a >> b)
