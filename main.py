from cmath import pi
from copy import deepcopy
from typing import List

# 第一章 快速上手:基础知识
# 通过另一本基础知识巩固一下
# 函数
"""
i = pow(2,3)  # pow():乘方函数
print(int(i))
"""
"""
import turtle
from turtle import *

active = True
while active:
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    keys = input()
    if keys == 'q':
        break
"""
# 第二章 列表和元组
# 数据结构:以某种方式组合起来的数据元素集合
"""
edward = ['edward gumby',42]
john = ['john smith',50]
database = [edward,john]
print(database)
"""
# 通用的序列操作
# 索引  序列中的所有元素都有编号，这些编号从0开始递增
"""
greeting = 'Hello'
print(greeting[0])  # 打印第一个元素
print(greeting[-1])  # 打印列表中最后一个元素
print(greeting[1])  # 打印列表中第二个元素
"""
# 如果函数调用返回一个序列，可以直接对其执行索引操作
"""
froth = input('Year:')[3]
print(froth)
"""
"""
months = [
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december',
]
endings = ['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']
year = input('Year:')
month = input('Month:')
day = input('Day:')

month_number = int(month)
day_number = int(day)

month_name = months[month_number-1]
ordinal = day + endings[day_number-1]
print(f"{month_name}  {ordinal}  {year}")
"""
# 切片:使用两个索引，并用冒号分隔，其中，第一个索引指定的元素包含在切片内，第二个索引指定的元素不包含在切片内
"""
num = [1,2,3,4,5,6,7,8,9,10]
img = num[3:6]  
print(img)
"""
"""
url = input('Please enter the URL:')
domain = url[4:-4]
print(f"domain name is {domain}")
"""
# 更大的步长  在切片中，第三个参数为步长  步长为正，向右移动，步长为负，向左移动
"""
num = [1,2,3,4,5,6,7,8,9,10]
img = num[0:10:1]  # 索引10代表第11个元素，它并不存在，但确实是到达最后一个元素后在前进一步所处的位置
print(img)
"""
# 序列相加  一般来说，不能拼接(此处的拼接指使用‘+’拼接)不同类型的序列
""""
f_x = [1,2,3]
s_x = [4,5,6]
p_x = f_x + s_x
print(p_x)
"""
"""
f_x = ([1,2,3])
s_x = 'world'
print(f"{f_x}  {s_x}")
"""
# 乘法
"""
img = ['python']
mis = img * 5
print(mis)
"""
# None 空列表 初始化
"""
img = [None]
msi = img * 10
print(msi)
"""
# 在合适的位置在一个方框内打印一个句子
"""
sentence = input("Sentence:")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print()
print('' * left_margin + '+' + '-' * (box_width - 2) + '+')
print('' * left_margin + '| ' + ' ' * text_width + '   |')
print('' * left_margin + '| ' + sentence + '   |')
print('' * left_margin + '| ' + ' ' * text_width + '   |')
print('' * left_margin + '+' + '-' * (box_width - 2) + '+')
print()
"""
# 成员资格
"""
database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843'],
]
username = input("User name:")
pin = input("PIN Code:")
if [username, pin] in database:
    print("登录成功")
else:
    print("用户名或密码错误")
"""
# 长度，最小值和最大值
"""
numbers = [100,34,678]
print(len(numbers))
print(max(numbers))
print(min(numbers))
"""
# 列表:python的主力
# 函数list  任何序列都可以作为list的参数
"""
print(list('Hello'))
"""
# 基本的列表操作
# 修改列表:给列表赋值:应使用索引表示法给特定位置的元素赋值
""""
x = [1,2,3]
x[0] = 12  
print(x)
"""
# 删除元素: del语句
"""
x = [1,2,3]
del x[0]
print(x)
"""
# 给切片赋值  可以将切片替换成长度与其不同的序列  还可以再不替换原有元素的情况下插入新元素
"""
x = list('perl')
print(x)
x[2:] = list('12')
print(x)
"""
"""
x = [1,2]
print(x)
x[0:] = [1,2,3,4,5]
print(x)
"""
"""
x = [1,2]
print(x)
x[0:] = []  # 将切片的值替换为空列表，可以作为一种删除列表内元素的方法
print(x)
"""
# 列表方法
# 调用语句: object.method(arguments)
# append()方法:将一个对象附加到列表末尾  '()'中为指定的元素
"""
x = [1,2]
print(x)
x.append(3)
print(x)
"""
# clear方法:就地清空列表的内容
"""
x = [1,2]
print(x)
y = x[:]
print(y)
x.clear()
print(x)
"""
# copy方法:复制列表，常规复制只是将另一个名称关联到列表
"""
x = [1,2,3]
print(x)
y = x.copy()  # 此方法等价于y = x[:]以及y = list(x)
print(y)
"""
# count()方法:计算指定的元素在列表中出现多少次  ’()‘中为指定的元素
"""
x = [1,1,1,1,1,2,2,3,4,3,3,5,]
y = x.count(1)
print(y)
"""
# extend()方法:同时将多个值附加到列表末尾  ’()'中为指定内容
# 与拼接操作不同，拼接操作不会修改原列表
"""
x = [1,2,3]
y = [4,5,6]
x.extend(y)
print(x)
"""
# index操作:在列表中查询指定值第一次出现的位置
"""
x = [8,2,3,4,5,6,1,1]
try:
    m = x.index(0)
except:
    print("0没有出现在列表中")
else:
    print(m)
y = x.index(1)
print(y)
"""
# insert()方法:将指定元素插入到指定位置,具有两个参数，第一个参数为插入的指定位置，第二个参数为插入的指定元素
"""
x = [1,2,3,4,5]
x.insert(0,1)
print(x)
"""
'''
x = [1,2,3,4,5]
"""
x.pop(0)
print(x)
"""
x.remove(5)
print(x)
'''
# pop()方法:从列表中删除一个元素，并返回这一元素
# 方法pop()与方法remove()区别:
# 方法pop()删除指定位置的元素
# remove()删除指定元素
# pop()方法:
"""
x = [1,2,3,4,5]
x.pop(0)  # 删除列表x中位置为0号的元素
print(x)
# 结果为:[2,3,4,5]
"""
# remove方法:
"""
x = [1,2,3,4,5]
x.remove(5)  # 删除列表x中值为5的元素
print(x)
# 结果为:[1,2,3,4]
"""
# reverse方法:按相反顺序排列列表中的元素
"""
x = [1,2,3,4,5]
x.reverse()
print(x)
"""
# sort()方法:对列表就地排序
"""
x = [4,6,2,1,7,9]
x.sort()
print(x)
"""
# 高级排序
# sort()方法接受两个可选参数key和reverse
"""
x = ['aardvark','abalone','acme','add','aerate']
x.sort(key=len)
print(x)
"""
# reverse=Ture为降序，reverse=False为升序
"""
x = [4,6,2,1,7,9]
x.sort(reverse=True)
print(x)
"""
# 元组:不可修改的元素
"""
x = (1,2,3)
print(x)
"""
"""
x = (1,2,3)
try:
    x[0] = 2
except:
    print("不能修改元组的内容")
else:
    print(x)
"""
# 元组可以是空元组
"""
x = ()
print(x)
"""
# 当元组中只有一个值时，需要在值后加上','，如果不加','，即表示为一个某种类型的值
"""
x = (42,)
print(x)
"""
# 元组将一个序列作为参数，并将其转化为元组，如果参数已经是元组，就原封不动的返回参数
# 第三章 使用字符串
# 字符串基本操作
# 字符串是不可变的，因此所有的元素赋值和切片赋值都是非法的
# 设置字符串格式:
# 调用方法format,并提供要设置其格式的值
# 替换字段的组成:
# 字段名:索引或标识符，指出要设置哪个值的格式并使用结果来代替该字段
# 转换标志:跟在叹号‘!’后面的单个字符，当前支持的字符包括r:repr,s:str,a:ascii
# 格式说明符:跟在冒号后面的表达式，可以详细的指定最终的格式，包括格式类型，字段宽度以及数的精度
# 替换字段名
""""
ims = "{foo} {} {bar} {}".format(1,2,bar=4,foo=3)
print(ims)
"""
"""
ims = "{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3)
# 可以通过索引来指定要在哪个字段中使用相应的未命名参数
print(ims)
"""
"""
fullname = ['Alfred', 'Smoketoomuch']
ims = "Mr{name[0]}".format(name=fullname)
print(ims)
# 在这里将列表fullname的内容赋值给name，则列表name的内容与列表fullname的内容相同，name[0]表示在name列表中处于第0号位置的元素
"""
# 基本转换
# 首先应提供一个转换标志，用于指定转换格式
"""
print("{pi!s}{pi!r}{pi!a}".format(pi='Π'))
"""
"""
ims = "the number is {num}".format(num=42)
print(ims)
ims = "the number is {num:f}".format(num=42)
print(ims)  # 转化为小数
ims = "the number is {num:x}".format(num=42)
print(ims)  # 转化为小写字母的十六进制数
ims = "the number is {num:b}".format(num=42)
print(ims)  # 转化为二进制数
"""
# 宽度，精度与千位分隔符
# 设置浮点数的格式时，默认在小数点后面显示6位小数，同时根据需要设置字段的宽度，而不进行任何形式的填充
# 同时，数和字符串的对对齐方式不同
"""
ims = "{num:10}".format(num=3)
print(ims)  # 数的对齐方式:         3
"""
"""
ims = "{num:10}".format(num='Bob')
print(ims)  #字符串的对齐方式: Bob       
"""
# 精度使用整数指定，但需要在前面加上一个表示小数点的句点'.'
"""
ims = "pi day is {pi:.2f}".format(pi=pi)
print(ims)
"""
"""
ims = "{pi:10.2f}".format(pi=pi)
print(ims)
"""
# 添加千位分隔符
"""
ims = "{:,}".format(10**100)
print(ims)
"""
# 符号 对齐 0填充
"""
ims = "{:010.2f}".format(pi)
print(ims)  # 0000003.14
ims = "{0:<10.2f}".format(pi)
print(ims)  #3.14
ims = "{0:>10.2f}".format(pi)
print(ims)  #       3.14
ims = "{0:^10.2f}".format(pi)
print(ims)  #   3.14   
"""
# 用符号填充
"""
ims = "{:$^15.2f}".format(pi)
print(ims)
"""
# 说明符=:指定将填充字符放在符号和数字之间
"""
print('{0:10.2f}\n{1:10.2f}'.format(pi,-pi))
#       3.14
#      -3.14
print('{0:10.2f}\n{1:=10.2f}'.format(pi,-pi))
#      3.14
#-     3.14
"""
"""
print('{0:-.2}\n{1:-.2}'.format(pi, -pi))
# 3.1
# -3.1
print('{0:+.2}\n{1:+.2}'.format(pi, -pi))
# +3.1
# -3.1
print('{0: .2}\n{1: .2}'.format(pi, -pi))
# 3.1
#-3.1
"""
# 井号’#‘:触发另一种转换方式，转换细节碎类型而异
"""
print('{:b}'.format(45))  # 101101
print('{:#b}'.format(45))  # 0b101101
print('{:g}'.format(45))  # 45
print('{:#g}'.format(45))  # 45.0000
"""
"""
width = int(input("please enter width:"))

price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}'.format(item_width,price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width,price_width)

print('='*width)
print(header_fmt.format('Item','Price'))
print('-'*width)

print(fmt.format('apple',0.4))
print(fmt.format('pears',0.5))
print(fmt.format('cantaloupes',1.92))
print(fmt.format('dried apricots(16 oz.)',8))
print(fmt.format('prunes(4 lbs.)',12))
print('='*width)
# please enter width:35
# ===================================
# Item                     
# -----------------------------------
# apple                          0.40
# pears                          0.50
# cantaloupes                    1.92
# dried apricots(16 oz.)         8.00
# prunes(4 lbs.)                12.00
# ===================================
"""
# 字符串方法
# center()方法:在两边添加填充字符(默认为空格)让字符居中  第一个参数为希望得到的填充后的字符数，第二个参数为希望用来填充的符号
"""
print("the middle by jimmy eat world".center(39))
print("the middle by jimmy eat world".center(39,'*'))
"""
# find()方法:在字符串中查找子串，如果找到则返回子串的第一个字符的索引，找不到返回-1
"""
print('with a moo-moo here,and a moo-moo there'.find('moo'))
title = 'monty python is flying circus'
i = title.find('monty')
q = title.find('python')
r = title.find('1')
print(i,q,r)
"""
"""
subject = '$$$ get rich now ! $$$'
i = subject.find('$$$')
print(i)
"""
# join()方法:合并序列的元素
"""
dirs = '','user','bin','env'
i = '/'.join(dirs)
print(i)
"""
"""
dirs = '','user','bin','env'
print('C:'+'\\'.join(dirs))
"""
# lower()方法:返回字符串的小写版本
# 可以用于不区分大小写
"""
i = 'ABCDEFG'
print(i.lower())
"""
# replace()方法:将指定的子串都替换成另一个字符串，并返回替换后的结果
# 第一个参数为想要替换的目标子串，第二个参数为期望替换目标子串的字符串
"""
i = 'this is a test'
w = i.replace('is','eez')
print(w)
"""
# split方法:将字符串拆分为序列
# 第一个参数为指定的分隔符，默认为空格，第二个参数为分隔次数，默认为-1，即分隔所有
# 分隔符应为原本字符串中的字符
"""
i = '1+2+3+4+5'
m = i.split('+')
print(m)
i = '1+2+3+4+5'
m = i.split('+',5)
print(m)
"""
# strip()方法:用于删除字符串中开头和末尾的空白
# rstrip()方法:用于删除字符串末尾的空白
# lstrip()方法:用于删除字符串开头的空白
# 当()内有参数时，则删除指定的字符
# translate方法:替换字符串中的特定部分，只能进行单字符替换，可以同时替换多个字符
# 第一个字符和第二个字符的长度应相同
# 同时，其第三个参数可选，功能为指定删除某些字符
# 在使用方法translate时，应先创建一个转换表
"""
table = str.maketrans('cs','kz')
i = 'this is an incredible test'.translate(table)
print(i)
"""
# 判断字符串是否满足特定的条件
# 第四章 字典
# 创建和使用字典
# 函数dict()  # 利用函数dict()可以创建一个字典
"""
items = [
    ('name','gumby'),
    ('age',42)
]
d = dict(items)
print(d)
"""
"""
people = {
    'Alice':{
        'phone':'2341',
        'addr':'foo drive 23',
    },
    'Beth':{
        'phone':'9012',
        'addr':'bar street 42',
    },
    'Cecil':{
        'phone':'3158',
        'addr':'baz avenue 90',
    },
}
labels = {
    'phone':'phone number',
    'addr':'address',
}
name = input("Name:")
request = input("phone number(p) or address(a)?")
if request == 'p':
    key = 'phone'
elif request == 'a':
    key = 'addr'

if name in people:
    print(f"{name}的{labels[key]}是{people[name][key]}")
"""
# 字典的基本操作:
# len(d):返回字典d包含的键值对的数量
# d[k]:返回与键k相关联的值
# d[k] = v:将值v关联到键k
# del d[k]:删除键为k的项
# k in d:检查字典d是否包含键为k的项
# 字典方法
# clear()方法:删除所有的字典项
"""
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)
returned_value = d.clear()
print(d)
print(returned_value)
"""
# copy方法: 返回一个新字典，其包括的键值对与原来的字典相同  修改副本时会影响到原件
# deepcopy方法:返回一个新字典，其包括的键值对与原来的字典相同 deepcopy()方法复制的字典在修改时不会影响到原件
"""
x = {
    'username': 'admin',
    'machines': ['foo', 'bar', 'baz'],
}
y = x.copy()
print(x)
print(y)
y['username'] = 'mlh'
print(y)
print(x)
y['machines'].remove('foo')
print(y)
print(x)
# 第三对输出与第二对输出表明，在copy()方法中，如果修改(不是替换)副本，则会影响到原件
x = {
    'username': 'admin',
    'machines': ['foo', 'bar', 'baz'],
}
y = deepcopy(x)
y['machines'].remove('foo')
print(x)
print(y)
# 这对输出表明，在deepcopy方法中，修改副本不会影响到原件
"""
# fromkeys方法:返回具有指定键和值的字典
# 包括两个参数
# 第一个参数keys为必填，指定新字典的键,参数形式为列表形式,参数应包含在单引号中，多个参数用’,‘隔开
# 第二个参数为value为选填，默认值为None,再指定特定值时，无论如何指定值，多个键都会指向同一个值
"""
i = dict.fromkeys(['name','age'])
print(i)
"""
"""
i = dict.fromkeys(['name','age'],['wyj','21'])
print(i)
"""
# get()方法:当访问字典中没有的键时，返回none，当访问字典中存在的键时，返回键所对应的值
# get()方法有两个参数
# 第一个参数为访问的键，第二个键为当访问的键不存在时，返回的值
"""
d = {}
i = d.get('name')
print(i)
"""
"""
d = {
    'name': 'wyj',
    'age': '21',
}
i = d.get('age','none')
print(i)
"""
"""
people = {
    'Alice':{
        'phone':'2341',
        'addr':'foo drive 23',
    },
    'Beth':{
        'phone':'9012',
        'addr':'bar street 42',
    },
    'Cecil':{
        'phone':'3158',
        'addr':'baz avenue 90',
    },
}
labels = {
    'phone':'phone number',
    'addr':'address',
}
name = input("Name:")
request = input("phone number(p) or address(a)?")
if request == 'p':
    key = 'phone'
elif request == 'a':
    key = 'addr'
person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not available')
if name in people:
    print(f"{name}的{labels[key]}是{people[name][key]}")
"""
# items方法:返回一个包含所有字典项的列表
# keys()方法:返回一个字典视图，包含指定字典中的键
# pop()方法:获取与当前指定键相关联的值，并将改键值对从字典中删除
"""
d = {
    'x': 1,
    'y': 2,
}
i = d.pop('x')
print(i)
print(d)
# 第二个输出表示，pop()已经将键值对’x‘:1从字典d中删除
"""
# popitem()方法:随机删除一对键值对
# setdefault()方法:获取与指定键相关联的值，同时也可以再字典不包括指定的键时，在字典中添加指定的键值对
"""
d = {}
i = d.setdefault('name','none')
print(i)
print(d)
# 第二个输出表明，方法setdefult()在空字典d中添加了’name':'none'键值对
d = {}
i = d.setdefault('name','wyj')
print(i)
print(d)
"""
# update()方法:使用一个字典中的项来更新另一个字典
# 对于通过参数提供的字典，将键值对添加到当前字典最后
# 如果当前字典包含键相同的键值对，就替换它
"""
d = {
    'title': 'python web site',
    'url': 'http://www.python.org',
    'changed': 'mar 14 22:09:15 met 2016',
}
x = {
    'title': 'python language website'
}
d.update(x)
print(d)
y = {
    'url': 'www.baidu.com'
}
d.update(y)
print(d)
# 第二个输出表明，当在字典中存在与想更新的字典相同的键时，将原本字典中相应的键的值替换为更新的键值对的值的内容
"""
