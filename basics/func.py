# -*- coding: utf-8 -*-
# 调用函数
# abs取绝对值
print(abs(100))  # 100
print(abs(-100)) # 100

# max返回最大的值
print(max(1,2,3)) # 3

# 类型转化
s = '123'
print(int(s))
print(float(s))
print(str(s))
print(bool(1))

# hex 把一个整数转换成十六进制表示的字符串
print(hex(100))   # 0x64

# 定义函数
def my_abs(x):
    # 参数检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -1*x

print(my_abs(-9))

# 默认参数
def add(x,y=100):
    return x*y

print(add(3)) # y 不传时默认是100
print(add(2,200))

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
print(calc(*nums)) # 14 *把nums的每一个元素取出来传进去

# 不可变
def calc2(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc2(nums))

# 递归函数 
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))  # 120

# 迭代(遍历) 字典
d = {'name':'张三','age':20}
for k, v in d.items():
    print("key:",k,' value:',v)


from collections import Iterable         # 导包
isIterable = isinstance('abc', Iterable) # 是否可以遍历
print(isIterable)

list_str = ["A","B0","CC"]
for k,v in enumerate(list_str):  # enumerate 把list变成索引对,可以获得index
    print("key:",k,' value:',v)

# 列表生成式
list1 = list(range(1,11))  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)

import os
fileList = [d for d in os.listdir('./')]
print(fileList)

# 匿名函数  lambda
sum = lambda arg1, arg2 : arg1 + arg2
print(sum(10,20))

# 生成器,yield会暂停程序,再次启用会继续
def myGen():
    print("生成器被执行:")
    yield 1
    yield 2
myG = myGen()
print(next(myG))
print(next(myG))