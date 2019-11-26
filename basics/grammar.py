# 基础语法
print('result=',ord('A'))  # result=65, ord()把字符串转换成Unicode整数表示

print('result=',chr(66))  # result=B, chr()把Unicode整数转换成字符串表示

# 字符串拼接
s = 'zhan'+'san'
print(str)

# bytes类型
byte = b'ABC'
print(byte)     # b'ABC'

# bytes转化成str类型
str_byte = byte.decode('ascii')
print(str_byte)  # ABC

# str转化成bytes类型
print(str_byte.encode('ascii'))  # b'ABC'

# 字符串长度
print(len(str_byte)) # 3

# list 有序集合
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates[-2]) # 倒数第二个
print(classmates[len(classmates) - 1])  #最后一个
print(classmates[1:3])  # 左闭右开 第2和第3个

# 末尾插入
classmates.append('Adam')
print(classmates)

# 特定位置插入一个
classmates.insert(2,'jane')  #把jane放在下标=2的位置
print(classmates)

# 删除末尾
classmates.pop()
print(classmates)

# 删除特定位置
classmates.pop(2)  #把下标=2的位置删除
print(classmates)

# list里面的元素的数据类型也可以不同
someDiff = ['Apple', 123, True]

# list 元素也可以是另一个list
listInList = ['python', 'java', ['asp', 'php'], 'scheme']

# tuple 有序列表 (元组) 一旦初始化就不能修改
t = (1, 2)
print("====",t[0])
d = (3,)    # 一个元素时要加上 ','

# 循环
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# dict 字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael'] # 95

d.get('Michael',0)  # 95 假如不存在返回自己定义的0

# set(不重复) 要创建一个set，需要提供一个list作为输入集合
s = set([1, 1, 2, 2, 3, 3])
print(s) # 1,2,3 
s.add(4) # 添加
s.remove(4) # 删除


# 字符串 -- 保留字符串格式
peotry = '''上邪:
吾欲与君相知,
长命无绝衰.
山无陵,
江水为竭.
冬雷震震,
夏雨雪.
天地合,
乃敢与君绝.
'''
print(peotry)

# 转义 (\)
meaning = '\"print string\"'
print(meaning) # "print string"

# 占位符
placeholder = '这是一个%3.5s'%('占位符')
print(placeholder) # %3.5s 代表3-5位字符

# 格式化字符串
aint = 123456
print('aint=',aint)
print('aint=%d'%aint)
format = f'aint={aint}'
print(format)

# 字符串的复制
copy = 'abc'
copy *= 2
print(copy) # abcabc

# 变量类型 (type)
ty = 123
print(type(ty))
print(type(1.5))
print(type('type'))
print(type(True))   
print(type(None))
#<class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>

print(id(ty)) # id() 获取变量的内存地址

ty = 9//2  # // 取模
print(ty)


ty = 9%2  # % 取余
print(ty)

# 三元运算
s1 = 2
s2 = 4
s3 = s1 if s1>s2 else s2
print(s3)


# if 
num = 15
if 10 < num < 20 :
    print(num)

# list 
my_list = [1,2,3] + [4,5,6]
print(my_list)

print(1 in (my_list))
print(1 not in (my_list))

# 元素第一次出现时的索引
print(my_list.index(2))

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import time;  # 引入time模块
 
ticks = time.time()
print ("当前时间戳为:%s"%ticks)

localtime = time.localtime(time.time())
print(localtime)        # time.struct_time(tm_year=2019, tm_mon=10, tm_mday=15, tm_hour=9, tm_min=23, tm_sec=7, tm_wday=1, tm_yday=288, tm_isdst=0)
print(localtime[0])     # 2019

# 格式化时间
format1 = "%Y-%m-%d %H:%M:%S"
format2 = "%a %b %d %H:%M:%S %Y"
# 格式化成2016-03-20 11:45:39形式
format_time = time.strftime(format1, time.localtime()) 
print(format_time)

# 将格式字符串转换为时间戳
print(time.mktime(time.strptime(format_time,format1)))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime(format2, time.localtime()) )
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,format2)))

import func
print(func.sum(20,20))

from func import sum
print(sum(30,30))

content = dir(func)
print(content)

reload(func)  # 只加载一次