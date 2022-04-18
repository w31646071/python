'''
peoples = ['1', '2', '3', '4', '5']
print(len(peoples))
print(peoples)
message = f'我想邀请{peoples}来参加晚餐'  # 嘉宾名单
print(message)
message = f'{peoples[0]}不能参加晚餐'  # 指出1号嘉宾不能参加晚餐
print(message)
popped_peoples = peoples.pop(0)  # 将1号嘉宾从邀请名单中删除
peoples.insert(0, '6')  # 将6号嘉宾添加到邀请名单的0号位置
print(peoples)
message = f'我想邀请{peoples}来参加晚餐'
print(message)
peoples.insert(0, '7')  # 使用insert（）将一位新嘉宾添加到名单开头
peoples.insert(3, '8')  # 使用insert（）将一位新嘉宾添加到名单中间
peoples.append('9')  # 使用append（）将最后一名新建吗添加到名单末尾
print(peoples)
message = f'我想邀请{peoples}来参加晚餐'
print(message)
message = f'我只能邀请两位嘉宾参加晚餐'
print(message)
for i in range(6):
    i = 1
    i += 1
    peoples.pop(i)
for n in range(1):
    n = 0
    n += 1
    del peoples[n]
del peoples[0]
print(peoples)
'''
'''
car = ['bmw','audi','toyota','subaru']
'''
'''
car.sort()
print(car)
car.sort(reverse=True)
print(car)
print(sorted(car))
print(car)
'''
'''
car.reverse()
print(car)
s = len(car)
print(s)
'''
'''
bings = ['1', '2', '3']
for bing in bings:
    print(f'i like {bing} pizza')
print(f' i really love pizza!')
'''
'''
dongwus = ['1','2','3']
for dongwu in dongwus:
    print(f'A {dongwu} make a great pet')
print(f'Any of these animals would make a great pet!')
'''
"""
for value in range(1,5):
    print(value)
for value in range(1,6):
    print(value)
for value in range(6):
    print(value)
"""
""""
numbers = list(range(1,7))
print(numbers)
"""
"""
numbers = list(range(2,11,2))
print(numbers)
"""
"""
squares = []  # 创建一个新的空列表
for value in range(1, 11): # 使用函数range（）便利1到10的值
    square = value ** 2  # 在python中，**表示乘方
    squares.append(square)  # 将乘方后的数据利用append添加到空列表squares中
print(squares)  # 输出变更后的列表squares
"""
"""
squares = []
for value in range(1,11):
    squares.append(value**2)  # 相对于上一个代码，此处直接将value的值平方，并立即添加到空列表squares中（更为简洁）
print(squares)
"""
"""
digits = [1,2,3,4,5,6,7,8,9,0]
f1 = min(digits)  # min：列表中最小的数
f2 = max(digits)  # max：列表中最大的数
f3 = sum(digits)  # sum：列表中所有数相加
print(f1,f2,f3)
"""
"""
squares = [value ** 2 for value in range(1,11)]  # 指定一个描述性的列表名 
print(squares)
"""
"""
for value in range(1,20):
    print(value)
"""
"""
for value in range(1,1000001):
    print(value)
"""
"""
digits = [value for value in range(1,1000001)]  # 方括号中第一个函数应为for后的函数名 
f1 = min(digits)
f2 = max(digits)
f3 = sum(digits)
print(f1,f2,f3)
"""
"""
digits = [value for value in range(1,21,2)]  #直接创建一个列表，其中包含1到21中所有的奇数
print(digits)
"""
"""
digits = [value for value in range(3,31,3)]  # 直接创建一个列表，其中包含3到31中所有可以被3整除的数
print(digits)
"""
"""
for value in range(11):
    value = value ** 3  # 在python中，立方用**3表示
    print(value)
"""
"""
numbers = [value **3 for value in range(11)]  # 对上面前十个整数的立方用列表进行解析
print(numbers)
"""
"""
players = ['charles','martina','michael','florence','eli']
print(players[0:3])  # 从列表中的第0号元素开始，提取列表中第3号元素之前所有的元素，共3个元素
"""
"""
players = ['charles','martina','michael','florence','eli']
print(players[1:4])  #从列表中的第1号元素开始，提取列表中第4号元素之前所有的元素，共3个元素
"""
"""
players = ['charles','martina','michael','florence','eli']
print(players[:4])  # 从列表中第0到元素开始，提取列表中第4号元素之前所有的元素，共4个元素
"""
"""
players = ['charles','martina','michael','florence','eli']  
print(players[2:])  # 从列表中第2号元素开始，提取列表中最后一号元素之前所有的元素，不确定有多少元素
"""
"""
players = ['charles','martina','michael','florence','eli']
print(players[-3:])  # 复数索引返回距离列表末尾相应距离的元素，最后一号元素为-1
"""
"""
players = ['charles','martina','michael','florence','eli']
print("here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
"""
"""
first_list = ['1','2','3']
second_list = first_list[:]  # [:]：同时省略起始索引和终止索引，创建一个始于第一个元素并止于最后一个元素的切片，即整个列表的副本，可以用于复制列表
print(first_list)
print(second_list)
"""
"""
lists = ['1','2','3','4','5']
print('the first three items in the list are:')
for list in lists[:3]:
    print(list)
"""
"""
lists = ['1','2','3','4','5']
print('three items form the middle of the list are:')
a = int(len(lists)/2)  # 使用len()函数获取列表list的长度，并赋予int整型类型，将长度除2获取中位数并赋值于a
for list in lists[a-1:a+1]:  # a-1，a+1获取列表lists中间三个数在列表lists中的元素位置
    print(list)
"""
"""
lists = ['1','2','3','4','5']
print("the last three items in the list are:")
for list in lists[-3:]:  # 打印列表末尾三个元素
    print(list)
"""
"""
my_pizzas = ['pizza','falafel','carrot cake']
friend_pizzas = my_pizzas[:]
my_pizzas.append('ah hhh')
friend_pizzas.append('wuhu')
print(my_pizzas)
print(friend_pizzas)
for food in friend_pizzas[0:]:
    print(food)
for foods in my_pizzas[0:]:
    print(foods)
"""
"""
dimensions = (200,50)  # python不能修改元组中的元素，可以修改列表中的元素   元组：()  列表：[]
print(dimensions[0])
print(dimensions[1])
"""
"""
tuples = (1,2,3,4,5)
for num_tup in tuples:
    print(num_tup)
"""
"""
foods = (1,2,3,4,5)
for food in foods:
    print(food)
"""
"""
foods[1] = 2  # 元组不允许赋值
print(foods)
"""
"""
foods = (1,2,3,4,5)
print("old foods:")
for food in foods:
    print(food)
foods = (2,4,6,8,10)
print("\n new foods:")
for food in foods:
    print(food)
"""
"""
cars = ['audi','bmw','subaru','toyota']  # 创建一个新的列表
for car in cars:
    if car == 'bmw':  # 条件测试              #  =：赋值   ==：判断
        print(car.upper())  # 条件为True时执行
    else:  # 条件为False时执行
        print(car.title())
"""
"""
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':  # !=：检查两个值是否不相等，其中，!表示“不”
    print("Hold the anchovies!")
"""
"""
answer = 17
if answer != 42:
    print("that is not the correct answer."
          "Please try again ")
"""
"""
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21  # False
"""
"""
age_0 = 22
age_1 = 21
age_0 >= 21 and age_1 >= 21  # True
 # 使用and条件检查多个条件，即为”与“门： 0 and 1 = 0   1 and 1 = 1  0 and 0 = 0   1 and 0 = 0
"""
"""
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21  #True
"""
"""
age_0 = 18
age_1 = 18
age_0 >= 21 or age_1 >= 21  #False
  # 使用or条件检查多个条件，即为“非”门：0 or 0 = 0   1 aor 0 = 1  1 or 1 = 1   0 or 1 =1 
"""
"""
requested_toppings = ['mushrooms','onions','pineapple']
'mushrooms' in requested_toppings  # True
'pepperoni' in requested_toppings  # False
"""
"""
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:  # 检查特定值是否不包含在列表中
    print(f'{user.title()},you can post a response if you wish.')
"""
"""
age = 19                                  # if语句格式：
if age >= 18:                             # if conditional_test:
    print('you are old enough to vote !')#   do something
"""
"""
age = 19
if age >= 18:
    print(' you are old enough to vote !')
    print(' have you registered to vote yet ? ')
"""
"""
age = 17
if age >= 18:
    print(' you are old enough to vote !')
    print(' have you registered to vote yet ? ')
else:  # 当if的条件未满足时执行else后的操作
    print('sorry,you are too young to vote !')
"""
"""
age = 12
if age < 4:
    print('free')
elif 4 <= age <= 18:  # 当if条件未通过时执行elif条件
    print('25')
else:  # else后直接跟":"，当elif条件未通过时执行else条件
    print('40')
"""
"""
age = 12
if age < 4:
    price = 0
elif 4 <= age <= 18:
    price = 25
else:
    price = 40
print(f' you should pay {price}! ')  # 相较于上一个程序，简化了条件测试过程
"""
"""
age = 12  # 使用多个elif代码块进行判断
if age < 4:
    price = 0
elif 4 <= age <= 18:
    price = 24
elif 18 <= age <= 65:
    price = 40
else:
    price = 20
print(f' you should pay {price} ')
"""
"""
age = 12
if age < 4:
    price = 0
elif 4 <= age < 18:
    price = 24
elif 18 <= age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f' you should pay {price} ! ')  # 某些情况下省略else代码模块可以使判断条件更为清晰
"""
# if-elif-else代码模块仅仅适合于只有一个条件满足的情况，可以测试一个特定的条件。
# 下面的代码模块可以检查所有条件
"""
requested_toppings = ['mushrooms','extra-cheese']
if 'mushrooms' in requested_toppings:
    print('adding mushrooms')
if 'extra-cheese' in requested_toppings:
    print('adding extra-cheese')
if 'pepperoni' in requested_toppings:
    print('adding pepperoni')
print("\n finished making your pizza!")
"""
"""
alien_color = ['green','yellow','red']
if 'green' in alien_colour:
    print('5')
"""
"""
alien_color = ['yellow','red']
if 'green' in alien_colour:
    print('5')
"""
"""
alien_color = ['green','yellow','red']
if 'green' in alien_color:
    print('5')
else:
    print('10')
"""
"""
alien_color = ['yellow','red']
if 'green' in alien_color:
    print('5')
else:
    print('10')
"""
"""
alien_color = ['green','yellow','red']  # 总体版本
if 'green' in alien_color:
    print('5')
elif 'yellow' in alien_color:
    print('10')
else:
    print('15')
"""
"""
alien_color = ['green']  # 绿色  
if 'green' in alien_color:
    print('5')
elif 'yellow' in alien_color:
    print('10')
else:
    print('15')
"""
"""
alien_color = ['yellow']  # 黄色  
if 'green' in alien_color:
    print('5')
elif 'yellow' in alien_color:
    print('10')
else:
    print('15')
"""
"""
alien_color = ['red']  # 红色
if 'green' in alien_color:
    print('5')
elif 'yellow' in alien_color:
    print('10')
else:
    print('15')
"""
"""
age = 70
if age < 2:
    print('婴儿')
elif 2 <= age < 4:
    print('幼年')
elif 4 <= age < 13:
    print('儿童')
elif 13 <= age < 20:
    print('青少年')
elif 20 <= age < 65:
    print('成年人')
else:
    print('老年人')
"""
"""
favorite_fruits = ['1','2','3']
if '1' in favorite_fruits:
    print('you really like 1 !')
if '2' in favorite_fruits:
    print('you really like 2 !')
if '3' in favorite_fruits:
    print('you really like 3 !')
if '4' in favorite_fruits:
    print('you really like 4 !')
if '5' in favorite_fruits:
    print('you really like 5 !')
"""
"""
requested_toppings = ['mushrooms','green-peppers','extra cheese']
for requested_topping in requested_toppings:
    print(f' adding {requested_topping}')
print('/n finished making your pizza !')
"""
"""
requested_toppings = ['mushrooms', 'green-peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green-peppers':  # if语句可以检查特殊元素
        print('sorry,we are out of green peppers right now')
    else:
        print(f' adding {requested_topping}')
print('/n finished making your pizza !')
"""
"""
# if语句可以用于检查列表是否为空
requested_toppings = []
if requested_toppings:
# 先对列表进行一个简单的检查，而不是直接执行for循环，在列表至少有一个元素时返回true，在列表为空时返回false并执行else语句
    for requested_topping in requested_toppings:
        print(f' adding {requested_topping}')
else:
    print('are you sure you want a plain pizza?')
"""
"""
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requester_toppings = ['mushrooms','french-fries','extra cheese']
for requester_topping in requester_toppings:
    if requester_topping in available_toppings:
        print(f'adding {requester_topping}')
    else:
        print(f'sorry we do not have {requester_topping}')
    print('\n finished making your pizza !')
"""
"""
# 以特殊方式跟管理员打招呼
yhms = ['admin','1','2','3','4']
for yhm in yhms:  # 利用for函数遍历列表yhms的内容
    if yhm == 'admin':  # yhm的值为admin
        print('hello admin,would you like to see a status report?')
    else:  # yhm值不是admin
        print(f' hello {yhm},thank you for logging in again')
"""
"""
yhms = []
if yhms:  # 利用if语句对列表yhms进行判空
    for yhm in yhms:  # 列表yhms不为空列表
        if yhm == 'admin':
            print('hello admin,would you like to see a status report?')
        else:
            print(f' hello {yhm},thank you for logging in again')
else:  # 列表yhms为空列表
    print('没用户？什么玩意儿？')
"""
"""
current_users = ['1','2','3','4','5']
new_users = ['1','2','6','7','8']
for new_user in new_users:
    if new_user in current_users:
        print('换个用户名吧')
    else:
        print('欸嘿，这个可以用喔')
"""
"""
nums = ['1','2','3','4','5','6','7','8','9']
for num in nums:
    if num == '1':
        print(f'{num}st')
    elif num == '2':
        print(f'{num}nd')
    elif num == '3':
        print(f'{num}rd')
    else:
        print(f'{num}th')
"""
"""
# 字典数据类型，用{}表示，一对一对应，格式为'键':'内容'，两个键值之间用‘，’隔开
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
"""
"""
alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print(f' you have get {new_points} points !')
"""
"""
alien_0 = {'color':'green','points':5}
print(alien_0)
# 向字典里添加键值对的方法
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
"""
"""
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
"""
"""
#下面是修改字典里值的过程：
alien_0 = {'color':'green','points':5}
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
"""
"""
alien_0 = {'x_position': 0,'y_position':25,'speed':'medium'}
print(f"original position:{alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"new position: {alien_0['x_position']}")
"""
"""
#下面是删除键值对的过程：
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['color']
print(alien_0)
"""
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah is favorite_languages is {language}.")
"""
"""
#使用get()访问字典中的值，当指定的键不存在时，返回一个默认值，可以避免键值错误
alien_0 = {'color':'green','speed':'slow'}
point_alien = alien_0.get('point','no point value assigned')  # get()函数中，第一个值为要访问的键值，第二个值为当要访问的键值不存在时，返回的默认值
print(point_alien)
"""
"""
people = {
    'first_name':'wang',
    'last_name':'yu jia',
    'city':'qinhuangdao',
    'age':21,
}
print(people)
"""
"""
num = {
    'wang1':1,
    'wang2':2,
    'wang3':3,
    'wang4':4,
    'wang5':5,
}
print(num)
"""
"""
zidian = {
    'for':'用于循环',
    'if':'用于循环，也可以用于判断列表是否为空列表',
    'else':'用于if循环，在特殊情况下可以省略用elif代替',
    'len':'用于统计列表长度',
    'upper':'用于大写内容',
}
print(f"for:{zidian['for']} \n if:{zidian['if']} \n else:{zidian['else']} \n len:{zidian['len']} \n upper:{zidian['upper']}")
"""
""""
#遍历字典的过程：当遍历字典时，默认遍历所有的键
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():  # items():包含字典名和方法,返回一个键值对列表，之后，for循环依次将每个键值对赋值给指定的两个变量
    print(f"\n Key:{key}")
    print(f"value:{value}")
"""
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name,language in favorite_languages.items():
    print(f"{name.title()}  favorite language is {language.title()}")
"""
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in favorite_languages.keys():  # keys():当在不需要使用字典中的值时，可以用keys()函数遍历字典中的键
    print(name.title())
"""
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
friends = ['phil','sarah']
for name in favorite_languages:
    print(f"hi,{name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t {name.title()},i see you love {language}!")
"""
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
if 'erin' not in favorite_languages.keys():  # keys()可以检查内容是否为字典中的键
    print('erin,please take our poll!')
"""
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
if 'eric' not in favorite_languages.keys():  # keys()可以返回一个列表，其中包含字典中所有的键
    print("erin,please take our poll!")
"""
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in sorted(favorite_languages.keys()):  # 可以使用sorted()来获得按特定顺序排列的键列表的副本
    print(f"{name.title()},thank you for taking the poll.")
"""
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("the following languages have been mentioned:")
for language in favorite_languages.values():  # value()可以返回一个值列表，不包含任何键
    print(language.title())
"""
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("the following languages have been mentioned:")
for language in set(favorite_languages.values()):  # 集合set函数可以剔除重复项
    print(language.title())
"""
"""
dicts = {
    'list':'列表',
    'var':'变量',
    'int':'整型',
    'boolean':'布尔',
    'str':'字符串',
}
for keys,value in dicts.items():
    print(keys,value)
"""
"""
places = {
    "中国":"长江",
    "埃及":"尼罗河",
    "巴西":"亚马逊河",
}
for place, river in places.items():
    print(f"the {river} runs through {place}")
for river in places.values():  # values()函数：只打印内容
    print(river)  # 打印河流名字
for place in places.keys():  # keys()函数：只打印键
    print(place)  # 打印国家名字
"""
"""
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
invited_people = ['jen','sarah','wang']
for name in invited_people:
    if name in favorite_languages.keys():
        print(f'{name.title()},thank you !')
    else:
        print(f'{name.title()},can you want get my invited ?')
"""
"""
alien_0 = {'color':'green','point':5}
alien_1 = {'color':'yellow','point':10}
alien_2 = {'color':'red','point':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
"""
"""
aliens = []  # 创建一个用于存储外星人的空列表
for alien_number in range(30):  # 创建30个外星人
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:  # 显示前5个外星人
    print(alien)
print(len(aliens))
"""
"""
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
for alien in aliens[:5]:
    print(alien)
"""
"""
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
for alien in aliens[0:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15
for alien in aliens[0:5]:
    print(alien)
"""
"""
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese'],  # 可以在字典中存储一个列表
         }
print(pizza['crust'])
print(f"\npizza['toppings']")
for topping in pizza['toppings']:
    print(topping)
"""
"""
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'c'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"{name.title()} favorite languages are:")
    for language in languages:
     print(f"{language.title()}")
"""
"""
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'c'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()} favorite language is")  # 加入一个判定条件，如果只有一个语言，那按单数语句输出
    else:
        print(f"{name.title()} favorite languages are:")
    for language in languages:
        print(f"{language.title()}")
"""
"""
users = {
    'aeinstein': {
        'first': 'albert',
        'lost': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'maire',
        'lost': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():  # 遍历字典users，将每个键赋给变量username，同时将与当前键相关联的字典赋值给变量user_info
    print(f"\nUsername:{username}")
    fullname = f"{user_info['first'].title()} {user_info['lost'].title()}"  # 访问内部字典
    location = user_info['location']
    print(f"\tFull name:{fullname}")
    print(f"\tLocation:{location.title()}")
"""
"""
lisa = {
    'first_name': 'li',
    'last_name': 'chen',
    'age': 18,
    'city': 'nanchang',
}
mary = {
    'first_name': 'wang',
    'last_name': 'fang',
    'age': 25,
    'city': 'chengdu',
}
jack = {
    'first_name': 'zhang',
    'last_name': 'peng',
    'age': 12,
    'city': 'shanghai',
}
people = [lisa, mary, jack]  # 将字典存储于列表中时，字典名不需要加引号
for peo in people:
    print(peo)
for peo in people:
    print(f"name:{peo['first_name']}{peo['last_name']}")
    print(f"age:{peo['age']}")
    print(f"city:{peo['city']}")
"""
"""
first = {
    'zhonglei':'mao',
    'zhuren':'wang',
}
second = {
    'zhonglei':'eyu',
    'zhuren':'wang2',
}
third = {
    'zhonglei':'she',
    'zhuren':'wang3'
}
pets = [first,second,third]
for pet in pets:
    print(f"zhonglei:{pet['zhonglei']}")
    print(f"zhuren:{pet['zhuren']}")
"""
"""
favorite_places = {
    'wang1': ['1', '2', '3'],
    'wang2': ['4', '5', '6'],
    'wang3': ['7', '8', '9'],
}
for name,places in favorite_places.items():
    print(f"{name.title()}:{places}")
"""
"""
cities = {
    'hengshui': {
        'country': 'zhongguo',
        'population': 'shiwuwan',
        'fact': 'jiaoyu',
    },
    'qinhuangdao':{
        'country':'zhongguo',
        'population':'shisiwan',
        'fact':'jiaoyuhao,'
    },
    'beijing':{
        'country':'zhongguo',
        'population':'shiduowan',
        'fact':'henfu',
    },
}
for city,city_info in cities.items():  # 遍历字典时不要忘记.items()
    print(f"name:{city}")
    print(f"国家:{city_info['country']}")
    population = city_info['population']
    print(f"人口:{population}")
    fact = city_info['fact']
    print(f"事实:{fact}")
"""
# 第七章:用户输入和while循环
"""
message = input("tell me something,and i will repeat it back to you:")
# input()让程序暂停运行，等待用户输入一些文本，获取输入后，将其赋值给一个变量
print(message)
"""
"""
name = input("please enter your name:")
print(f"hello,{name}!")
"""
"""
prompt = "if you tell us who you are,we can personalize the messages you see"
prompt += "\nwhat is your first name?"
name = input(prompt)
# 可以将提示赋值给一个变量a，再将该变量a传递给函数input()
print(f"\nhello,{name}")
"""
"""
age = input("how old are you?")
age = int(age)  # int()函数将用户的输入视为数值,在不使用int()函数的情况下，用户输入为字符串，不能作为数字使用
if age < 4 :
    print('free')
elif 4 <= age < 18:
    print('25')
elif 18 <= age < 65:
    print('40')
else:
    print('20')
"""
"""
height = input("how tall are you,in inches?\n")
height = int(height)
if height >= 48:
    print('收费')
else:
    print('不收费')
"""
"""
number = input("enter a number,and i can tell you if it is even or odd:\n")
number = int(number)
if number % 2 == 0:  # %：求模运算，即求余数，如果一个数可以被另一个数整除，则返回值为0，否则，返回余数
    print(f"{number} is even")
else:
    print(f"{number} is odd")
"""
"""
car = input('what car would you like?\n')
print(f"let me see if i can find a {car.title()}")
"""
"""
number = input("你有多少人就餐？\n")
number = int(number)
if number >= 8:
    print("没座")
else:
    print("有座")
"""
"""
number = input()
number = int(number)
if number % 10 == 0:
    print(f"{number}是10的整数倍")
else:
    print(f"{number}不是10的整数倍")
"""
# while循环  while循环语句格式: while (表达式):    当表达式为真时，执行下面的语句，如果表达式为假，则跳出循环
#                               {
#                                   语句
#                               }
"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
"""
"""
prompt = "\ntell me something,and i will repeat it back to you:"
prompt += "\n enter 'quit' to end the program \n"
message = ""  # 创建变量message，用于记录输入的值
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
"""
"""
prompt = "\ntell me something,and i will repeat it back to you:"
prompt += "\n enter 'quit' to end the program \n"
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
"""
# break语句使用
"""
prompt = "\nplease enter the name of city you have visited:"
prompt += "\nenter 'quit' when you are finished \n"
while True:  # 以while True开头的循环，如果没有遇到break语句，将不断运行
    city = input(prompt)
    if city == 'quit':
        break  # break语句可以立即推出while循环，用于控制程序流程
    else:
        print(f"i would love to go to {city.title()}")
"""
# continue语句使用  与break语句不同的是，可以根据条件测试结果决定是否继续执行循环
"""
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # 当if语句为真时，执行continue语句，忽略后面的语句并返回循环的开头
    print(current_number)
"""
"""
prompt = "\n输入一系列pizza配料:"
prompt += "\n当你完成pizza配料时请输入'quit' \n"
active = True
while active:
    peiliao = input(prompt)
    if peiliao == 'quit':
        active = False
    else:
        print(f"我们将添加{peiliao}到你的pizza中")
"""
"""
message = "请告知你的年龄："
while True:
    age = input(message)
    age = int(age)
    if int(age) < 3:
        print("free")
        continue
    elif 3 <= int(age) < 12:
        print("10")
        continue
    elif int(age) >= 12:
        print("15")
        continue
"""
"""
message = "请告知你的年龄："
active = True
while active:
    age = input(message)
    if age == 'quit':  
        break
    elif int(age) < 3:
        print("free")
        continue
    elif 3 <= int(age) < 12:
        print("10")
        continue
    elif int(age) >= 12:
        print("15")
        continue
"""
"""
i = 1  # 一个无限循环的while循环
active = True
while active:
    i = i+1
    print(i)
"""
# 在列表中使用while循环
"""
unconfirmed_users = ['alice','brain','candace']
confirmed_users = []
while unconfirmed_users:  # while循环不断运行，直到目标列表为空
    current_user = unconfirmed_users.pop()
    print(f"verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print(f"\nthe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
"""
# 利用while循环删除为特定值的所有列表元素
"""
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
"""
"""
# 利用while循环使用用户输入填充字典
responses = {}  # 建立一个空字典responses
polling_active = True  # 设置一个while循环的标志
while polling_active:
    name = input("\nwhat is your name?\n")
    response = input("which mountain would you like to climb today?\n")
    responses[name] = response  # 将回答存储于字典中
    repeat = input("would you like to let another person respond?(yes/no)\n")
    if repeat == 'no':
        polling_active = False
print("\n--poll results--")
print(responses)  # 顺便打印一下字典
for name,response in responses.items():
    print(f"{name} would like to climb {response}")
"""
"""
sandwich_orders = ['1','2','3','4']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwiche = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwiche)
    print(f"i made your {finished_sandwiche}")
"""
"""
print("店里的五香烟熏牛肉卖完了")
sandwich_orders = ['1','2','3','pastrami','pastrami','pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
"""
"""
shengdi = {}
active = True
while active:
    name = input("\nwhat is your name?\n")
    place = input("\nwhere would you want to visit?\n")
    shengdi[name] = place
    respeat = input("would you like to let another person respond?(yes/no)\n")
    if respeat == 'no':
        break
print("\n--poll results--")
for name, place in shengdi.items():
    print(f"{name} want to {place}")
"""

# 第八章 函数
# 定义函数
'''
def greet_user():  # 在python中，创建函数使用关键字def，创建函数的格式为：def 函数名(完成任务所需要的信息):
    """显示简单的问候语"""
    print("hello!")  # 指出函数所需要进行的工作


greet_user()
'''
# 向函数传递信息
"""
def greet_user(username):  # 当调用函数时，需要赋值给username  其中，”uesrname“为形参，即函数完成工作所需要的信息
    print(f"hello!{username.title()}")


greet_user('jesse')  # “jesse”为实参，即调用函数时传递给函数的信息  在调用函数时，应将形参置于圆括号中
"""
"""
def display_message():
    print(f"这一章学习函数的相关知识")


display_message()
"""
"""
def favorite_book(title):
    print(f"one of my favorite book is {title.lower()}")


favorite_book('alice in wonderland')
"""
# 位置实参
"""
def describe_pet(animal_type, pet_name): 
    print(f"\ni have a {animal_type}")
    print(f"\n my {animal_type} name is {pet_name}")
# 在调用语句describe_pet('she','wyj')中，‘she’被赋值给‘animal_type’,'wyj'被赋值给'pet_name'
                                    # 函数调用时，实参的顺序应与函数定义中的形参的顺序一致

describe_pet('she', 'wyj')
"""
# 多次调用函数
"""
def describe_pet(animal_type, pet_name):
    print(f"\ni have a {animal_type}")
    print(f"\n my {animal_type} name is {pet_name}")


describe_pet('she', 'wyj')
describe_pet('dog', 'dillie')
"""
# 关键字实参  使用关键字实参时，可以不考虑函数调用中实参的顺序.  当使用关键字形参时，应准确指定函数定义中的形参名
"""
def describe_pet(animal_type, pet_name):
    print(f"\ni have a {animal_type}")
    print(f"my {animal_type} name is {pet_name}")


describe_pet(                 # 此处语句等效于：describe_pet(
    animal_type='hamster',                      pet_name='harry',
    pet_name='harry'                            animal_type='hamster'
)                                            ) 即为关键字实参是顺序无关紧要
"""
# 默认值  可以给形参指定默认值，如果在函数调用的过程中没有实参输入，则使用形参的默认值
"""
def describe_pet(pet_name, animal_type='dog'):
    print(f"\ni have a {animal_type}")
    print(f"\nmy {animal_type} name is {pet_name}")


describe_pet('she')  # 此处语句可以等价为：describe_pet(pet_name='she')
"""
# 有默认值的形参被赋予实参时的示例
"""
def describe_pet(pet_name, animal_type='dog'):
    print(f"\ni have a {animal_type}")
    print(f"\nmy {animal_type} name is {pet_name}")


describe_pet('she','little dog')  # 当函数调用时，有默认值的形参被赋予了实参，运行结果将表示实参而不是默认值
"""

# 避免实参错误
# 实参错误内容：Traceback(most recent call last)
"""
def make_shirt(chima, ziyang):  # 关键字实参调用函数
    print(f"这件{chima}大的T恤是印有{ziyang}的字样")


make_shirt(
    chima='175',
    ziyang='我爱你'
)
"""
"""
def make_shirt(chima, ziyang):  # 位置实参调用函数
    print(f"这件{chima}大的T恤是印有{ziyang}的字样")


make_shirt('175','我爱你')
"""
"""
def make_shirt(chima, ziyang='i love python'):
    print(f"这件{chima}大的T恤印有{ziyang}的字样")


make_shirt('175')  # 印有默认字样的大号T恤
make_shirt('165')  # 印有默认字样的中号T恤
make_shirt('155','我爱你')  # 印有‘我爱你’字样的小号T恤
"""

"""
def descrbie_city(chengshi, guojia='中国'):
    print(f"{chengshi} is in {guojia}")


descrbie_city('beijing')
descrbie_city('niuyue')
descrbie_city('hengshui')
"""

# 返回值  函数返回的值为返回值，可使用return语句将值返回调用函数的代码行
# 返回简单值
"""
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()  # 将内容按要求转换，并将结果返回到函数调用行 


musician = get_formatted_name('jimi', 'hendrix')  # 需要提供一个变量以便将返回值的值赋给变量
print(musician)
"""

# 让实参变为可选项
"""
def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
"""
"""
def get_formatted_name(first_name, last_name, middle_name=''):  # 默认形参应在非默认形参之后
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john',  'hooker')
print(musician)
"""

# 返回字典
"""
def build_person(first_name, last_name):
    person = {
        'first': first_name,
        'last': last_name,
    }
    return person


musician = build_person('jimi', 'hendrix')
print(musician)
"""
"""
def build_person(first_name, last_name,age=None):
    person = {
        'first': first_name,
        'last': last_name,
    }
    if age:
    person['age'] = age
    return person


musician = build_person('jimi', 'hendrix',age=27)
print(musician)
"""

# 结合使用函数和while循环
"""
def get_formatted_name(first_name, last_name,medium=''):
    full_name = f"{first_name} {last_name} {medium}"
    return full_name.title()


while True:
    print(f"\nplease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    m_name = input("Medium name:")
    if m_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,m_name,l_name)
    print(formatted_name)
"""

"""
def city_country(city, country):
    ims = f"{city} {country}"
    return ims.title()


print(city_country('santiago', 'chile'))
print(city_country('hengshui', 'china'))
print(city_country('shijiang', 'china'))
"""
"""
def make_album(singers,songs,num=None):
    album = {
        'singer':singers,
        'song':songs,
    }
    if num:
        album['num'] = num
    return album


ims = make_album('zjl','daoxiang',6)
print(ims)
ims = make_album('cyz','shinian',6)
print(ims)
ims = make_album('wyj','7777',6)
print(ims)
"""
"""
def make_album(singers,songs,num=None):
    album = {
        'singer':singers,
        'song':songs,
    }
    if num:
        album['num'] = num
    return album


active = True
while active:
    singer = input()
    if singer == 'q':
        break
    song = input()
    if song == 'q':
        break
    yn = input()
    if yn == 'no':
        active = False
    ims = make_album(singer,song)
    print(ims)
"""

# 传递列表:在函数调用的过程中，列表名可以作为实参调用，此时，函数可以直接访问列表中的内容
"""
def greet_users(names):
    for name in names:
        msg = f"hello,{name.title()}!"
        print(msg)


names = ['hannah', 'ty', 'margot']
greet_users(names)  
"""
# 在函数中修改列表
"""
def print_models(unprinted_designs,completed_modesls):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing models:{current_design}")
        completed_modesls.append(current_design)
def show_completed_models(completed_models):
    print("\nthe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
"""

# 禁止函数修改列表
"""
def print_models(unprinted_designs, completed_modesls):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing models:{current_design}")
        completed_modesls.append(current_design)


def show_completed_models(completed_models):
    print("\nthe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print(completed_models)
"""

"""
def show_messages(news):
    for new in news:
        print(new)


img = ['1', '2', '3']
show_messages(img)
"""
"""
def send_messages(show_messages,sent_messages):
    while show_messages:
        message = show_messages.pop()
        sent_messages.append(message)


show_messages = ['1','2','3']
sent_messages = []
send_messages(show_messages,sent_messages)
print(show_messages)
print(sent_messages)
"""
"""
def send_messages(show_messages,sent_messages):
    while show_messages:
        message = show_messages.pop()
        sent_messages.append(message)


show_messages = ['1','2','3']
sent_messages = []
send_messages(show_messages[:],sent_messages)
print(show_messages)
print(sent_messages)
"""

# 传递任意数量的形参  *形参名:创建一个”形参名“的空元组，并将收到的所有值都封装到这个元组中
"""
def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
"""
"""
def make_pizza(*toppings):
    print(f"\nmaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{toppings}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
"""
# 结合使用位置实参和任意数量实参
"""
def make_pizza(size,*toppings):
    print(f"\nmaking a {size}-pizza with the following toppings:")
    for topping in toppings:
        print(f"-{toppings}")


make_pizza(16,'pepperoni')
make_pizza(16,'mushrooms', 'green peppers', 'extra cheese')
"""

# 使用任意数量的关键字实参
"""
def build_profile(first, last, **user_info):  # **形参名:创建一个以”形参名“为名的字典
    user_info['first'] = first
    user_info['last'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
"""
"""
def sanmingzhi(*shicais):
    for shicai in shicais:
        print(f"{shicai}")


sanmingzhi('1')
sanmingzhi('1','2')
sanmingzhi('1','2','3')
sanmingzhi('1','2','3','4')
"""

"""
def build_profile(first, medium, last, **user_info):
    user_info['first'] = first
    user_info['medium'] = medium
    user_info['last'] = last
    return user_info


user_profile = build_profile('wang', 'yu', 'jia', location='qinhuangdao', field='physics')
print(user_profile)
"""

"""
def build(zhizhaoshang, xinghao, **qita):
    qita['zhizhaoshang'] = zhizhaoshang
    qita['xinghao'] = xinghao
    return qita


xinxi = build('audi', 'RS7', color='blick', tow_package=True)
print(xinxi)
"""
# 将函数存储在模块中
# 将函数存储在称为”模块“的独立文件中，再使用“import”语句将模块导入到主程序中
# 导入整个模块
"""
import mokuai  # 在此处，import语句导入了外部创建的pizza模块文件中的make_pizza()函数

mokuai.make_pizza(16, 'pepperoni')  # 调用模块中函数的语句:module_name.function_name()
mokuai.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
"""
# 导入特定的函数:from module_name import function_name//可根据需要从模块中导入任意数量的函数
"""
from mokuai import make_pizza

make_pizza(16,'pepperoni')
make_pizza(16,'mushrooms','green peppers','extra cheese')
"""
# 当导入的函数名过长或与程序中现有的名称冲突时，可以使用“as”指定简短的别名:from module_name import function_name as fn
"""
mp(16,'pepperoni')
mp(16,'mushrooms','green peppers','extra cheese')
"""
# 同时，”as”也可以给模块指定别名:import module_name as mn
"""
import mokuai as m

m.make_pizza(16, 'pepperoni')
m.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
"""
# 导入模块中所有函数:from module_name import * ‘*’ 可以导入模块中所有函数
"""
from mokuai import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
"""
"""
from mokuai import print_models as pm
unprinted_models = ['phone case','robot pendant','dodecahedron']
completed_models = []
pm(unprinted_models,completed_models)
print(unprinted_models)
print(completed_models)
"""

# 第九章 类
# 类的使用方法:
# 对类进行实例化:实例名 = 类名
# 使用类中的值:实例名.属性
# 使用类中的函数:实例名.方法名(参数列表)
# 创建和使用类
'''
class dog:  # 定义了一个名为dog的类  定义类的格式:class 类名
    """--一次模拟小狗的简单尝试--"""  # 描述这个类的功能

    def __init__(self, name, age):
        # 类中的函数成为方法。即方法本质也是一种函数
        # 在方法中，形参self必不可少且位于其他形参前面
        # 在调用这个方法创建实例时，每个与实例相关联的方法调用都自动传递实参self
        # self是一个指向实例本身的引用，让实例能够访问类中的属性和方法
        """--初始化属性name和age--"""
        self.name = name
        self.age = age
        # 以self为前缀的变量可供类中所有的方法使用，可以通过类的任何实例访问

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over")
'''

# 根据类创建实例
'''
class dog:
    """--一次模拟小狗的简单尝试--"""

    def __init__(self, name, age):
        """--初始化属性name和age--"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over")


my_dog = dog('willie', 6)  # 此处语句访问了类dog中的属性
your_dog = dog('lucy',3)  # 此处语句创建了第二个实例your_dog，同时也访问了类dog中属性
my_dog.sit()
my_dog.roll_over()
# 此处语句调用了类dog中的方法
# 调用方法需要指定实例的名称和要调用的方法，并用'.'间隔
your_dog.sit()
your_dog.roll_over()
# 创建的第二个实例调用了类dog中的方法
print(f"my dog name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old")
print(f"your dog name is {your_dog.name}")
print(f"your dog is {your_dog.age} years old")
'''

"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening")


restaurant = Restaurant('wyj', '111')
print(f"{restaurant.restaurant_name} {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant = Restaurant('ddd','222')
restaurant.describe_restaurant()
restaurant = Restaurant('zzz','333')
restaurant.describe_restaurant()
restaurant = Restaurant('aaa','444')
restaurant.describe_restaurant()
"""

"""
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"mr/miss.{self.first_name}，how are you")


user = User('wang', 'yujia')
user.describe_user()
user.greet_user()
user = User('ddd', 'www')
user.describe_user()
user.greet_user()
user = User('www','aaa')
user.describe_user()
user.greet_user()
"""

# 使用类和实例
# 由于修改属性的值注释符太多，迫不得已开一个新的文件存放这一次的实例
'''
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is opening")

    def read_served(self):
        print(f"有{self.number_served}人在这里就餐")

    def set_number_server(self, number):
        self.number_served = number

    def increment_number_server(self, number):
        self.number_served += number


restaurant = Restaurant('www', 'ddd')
restaurant.describe_restaurant()
restaurant.open_restaurant()
"""restaurant.number_served = 23
restaurant.read_served()
restaurant.set_number_server(23)
restaurant.read_served()"""
restaurant.increment_number_server(23)
restaurant.read_served()
'''

"""
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"mr/miss.{self.first_name}，how are you")

    def increment_login_attempts(self, number):
        self.login_attempts = number + 1
        print(f"={self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'={self.login_attempts}')


user = User('wang', 'yujia')
user.increment_login_attempts(0)
user.reset_login_attempts()
"""

# 继承  在继承中，当一个类继承另一个类时，被继承的类为父类，继承的类为子类，子类继承了父类所有的属性和方法，同时还可以定义自己的属性和方法
# 在子类中，属性和方法应为子类内容特有的内容
# 子类的方法__init__()
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} mile on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# 创建子类时，父类必须包含在当前的文件夹中，同时要位于子类前面
class ElectricCar(Car):  # 定义子类时应在圆括号‘()’中指定父类的名称
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # super()函数:可以调用父类中的方法__init__()


my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
"""

# 给子类定义
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} mile on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"this car has a {self.battery_size}-kwh battery")


my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
"""
# 重写父类的方法
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} mile on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"this car has a {self.battery_size}-kwh battery")

    def fill_gas_tank(self):
        print("this car does not need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
"""

# 将实例用作属性
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"this car has {self.odometer_reading} mile on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can not roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:  # 定义了一个新类Battery
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"this car has a {self.battery_size}-kwh battery")

    def get_range(self):
        if self.battery_size == '75':
            range = 260
        elif self.battery_size == '100':
            range = 315

    print(f"this car can go about {range} miles on a full charge")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
"""

# 模拟实物
"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业")

    def read_served(self):
        print(f"有{self.number_served}人在这里就餐")

    def set_number_server(self, number):
        self.number_served = number

    def increment_number_server(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['草莓味', '苹果味', '原味奶油']

    def describe_icecream(self):
        print(f"本店有三种冰激凌:")
        for flavor in self.flavors:
            print(flavor)


IceCreamStand = IceCreamStand('www', 'ddd')
IceCreamStand.describe_icecream()
"""

"""
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"mr/miss.{self.first_name}，how are you")

    def increment_login_attempts(self, number):
        self.login_attempts = number + 1
        print(f"={self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'={self.login_attempts}')


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"管理员有{privilege}权限")


Ad = Admin('www', 'sss')
Ad.show_privileges()
"""

"""
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"mr/miss.{self.first_name}，how are you")

    def increment_login_attempts(self, number):
        self.login_attempts = number + 1
        print(f"={self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'={self.login_attempts}')


class Privileges:
    def __init__(self, privileges=[]):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"管理员有{privilege}权限")


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


vip_user = Admin('www', 'zzz')
vip_user.privileges.show_privileges()
"""

"""
class Car:
    def __init__(self, make, model, year):
        
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.miles = 0

    def get_desprective_name(self):
        
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        # 将里程值存储在odometer_reading中
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
       
        if miles >= self.miles:
            self.odometer_reading += miles
        else:
            print("You can't add the miles which is negative number!")

    def fill_gas_tank(self):
        print("This car have a  gas tank")


class Battery:

    def __init__(self, battery_size=70):

        self.battery_size = battery_size

    def describe_battery(self):

        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
"""
# 导入类
# 导入单个类  在同一个文件夹中创建了一个Car.py，其内容为定义一个类，类名为Car
"""
form car import Car

my_car_ = Car('audi','a4','2019')
print(my_new_Car.get_descriptive_name())

my_new_car.odometer.reading = 23
my_new_car.read.odometer()
"""
# 在一个模块中存储多个类
"""
from car import ElectricCar
my_tesla = ElectricCar('tesla','model s','2019')

print(my_tesla.get_desriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get.range()
"""
# 从一个模块中导入多个类
"""
from car import Car,ElectricCar

my_beetle = Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster','2019)
print(my_tesla.get_Descriptive_name())
"""
# 导入整个模块
"""
import car

my_tesla = car.ElectricCar('tesla','roadster',2019)
print（my_tesla.get_descriptive_name())
"""
# 导入模块中所有的类:from module_name import *
# 在一个模块中导入另一个模块
# 自定义工作流程
"""
from restaurant import Restaurant

# 创建一个实例
my_restaurant = Restaurant('Go Believe', 'steamed stuffed bun')
# 打印多少人就餐过
print(my_restaurant.number_served)
"""
"""
from user import User, Privileges, Admin

first_admin = Admin('Ac', 'Fun', 22, 'female')
first_admin.privileges.show_privileges()

"""
"""
from user import User
from privileges import Privileges, Admin

first_admin = Admin('Ac', 'Fun', 22, 'female')
first_admin.privileges.show_privileges()

"""