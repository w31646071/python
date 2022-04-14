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














