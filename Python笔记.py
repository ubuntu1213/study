Python练习笔记
// 注释用井号（#）标识

字符串大小写转换
    name="ada lovelace"
    print(name.title())     # title() 以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。
    print(name.upper())     # upper() 将所有字母转换为大写 
    print(name.lower())     # lower() 将所有字母转换为小写  

合并（拼接）字符串:
    first_name="ada"
    last_name="lovelace"
    full_name=first_name + " " + last_name  #Python使用加号（+ ）拼接字符串
    print("Hello," + full_name)

删除空白
    favorite_language=' Python '
    favorite_language.rstrip()      # rstrip() 临时删除末尾空白
    favorite_language.lstrip()      # lstrip() 临时删除开头空白
    favorite_language.strip()       # strip() 临时删除两端空白

使用函数str()避免类型错误
    age=23
    message="Happy " + str(age) + "rd Brithday!"  # 在字符串中使用整数时，需要显式地指出你希望Python将这个整数用作字符串
    print(message)


Python列表
    列表：由一系列按特定顺序排列的元素组成(有序集合)。在Python中，用方括号[]来表示列表，并用逗号来分隔其中的元素。
    列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，在Python中，第一个列表元素的索引为0，而不是1。要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内
    注意：Python计算列表元素时从1开始（索引是从0开始）
            bicyles=['trek','cannondale','redline','specialized']
            print(bicyles[0].title()) #从列表bicycles中提取第一款自行车,可使用方法title() 让元素'trek' 的格式更整洁
            print(bicyles[3])
            print(bicyles[-1])      #通过将索引指定为-1，可让Python返回最后一个列表元素
        修改列表元素：
            motorcycles=['honda','yamaha','suzuki']
            motorcycles[0]='ducati'     #指定列表名和要修改的元素的索引，再指定该元素的新值。
        在列表末尾添加元素
            motorcycles.append('ducati')    #方法append()将元素'ducati' 添加到了列表末尾
        在列表中插入元素
            motorcycles.insert(0,'ducati')    #方法insert()在索引0处添加空间，并将值'ducati' 存储到这个地方。每个元素都右移一个位置
        从列表中删除元素
            使用del 语句删除元素：//删除后，将无法再访问它了
                del motorcycles[0]      #使用del删除了列表motorcycles中的第一个元素'honda'
             使用方法pop() 删除元素：//删除后，能够接着使用它
                popped_motorcycle = motorcycles.pop()   #删除最后一个元素，并将其存储到变量popped_motorcycle中
                                    motorcycles.pop(1)   #指定要删除的元素的索引
                print(popped_motorcycle)
        根据值删除元素 
            如果不知道要从列表中删除的值所处的位置，只知道要删除的元素的值，可使用方法remove()，删除后，也可接着使用它的值
                motorcycles.remove('ducati')    #只删除第一个指定的值，如果要删除的值可能在列表中出现多次（使用循环）
        列表排序
            使用方法sort()对列表进行'永久性排序'
                cars=['bmw','audi','toyota','subaru']
                cars.sort() #按字母顺序排列
                cars.sort(reverse=True) #逆序排序，向sort()方法传递参数reverse=True
                print(cars)
            使用函数sorted()对列表进行'临时排序'
                print(sorted(cars))
                rcars=sorted(df,reverse=True) #也可使用reverse=True参数，将排序后的结果保存到rcars中
                print(rcars)
            反转列表元素的排列顺序，可使用方法reverse() #不是指按与字母顺序相反的顺序排列，而只是反转列表元素的排列顺序
                cars.reverse()  #永久性地修改列表元素的排列顺序，可再次调用reverse()恢复到原来的排列顺序
        获取列表长度，使用方法len()
                len(cars)



for循环(注意缩进关系)

magicians=['alice','david','carolina']
for magician in magicians:   #从列表magicians中取出一个名字，并将其存储在变量magician中。for语句末尾的冒号告诉Python，下一行是循环的第一行。
        print(magician)      #每个缩进的代码行都是循环的一部分，且将针对列表中的每个值都执行一次

创建数值列表,使用函数range()
for value in range(1,5):    #打印数字1~4，从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值（这里为5）。
    print(value)

使用range()创建数字列表
numbers=list(range(1,6))    #函数list()将range()的结果直接转换为列表。
print(numbers)


#创建一个列表，包含前10个整数的平方
squares=[]
for i in range(1,11):
    squares.append(i**2)
    print(squares)

指定步长
even_numbers=list(range(2,11,2)) #从2开始数，然后不断地加2，直到达到或超过终值（11）
even_numbers=list(range(1,100,2)) #
print(even_numbers)

几个专门用于处理数字列表的Python函数
digits=list(range(1,10))
min(digits)
max(digits)
sum(digits)


列表解析：将for循环和创建新元素的代码合并成一行，并自动附加新元素。
squares=[value**2 for value in range(1,11)]
print(squares)
b=[i for i in range(1,21)] #创建一个包含1-20数字的列表解析


切片
players=['charles','martina','michael','florence','eli']
print(players[0:3]) #到达你指定的第二个值后停止,提取前3个元素
print(players[1:4]) #例如，如果你要提取列表的第2~4个元素，可将起始索引指定为1 ，并将终止索引指定为4
print(players[:4])  #如果你没有指定起始索引，Python将自动从列表开头开始：
print(players[2:])  #提取从第3个元素到列表末尾的所有元素，省略终止索引
print(players[-3:])  #负数索引返回离列表末尾相应距离的元素,输出最后三名队员

遍历切片
players=['charles','martina','michael','florence','eli']
#遍历前三名队员，并打印他们的名字
for i in players[:3]:
    print(i)

复制列表
    要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引[:]。这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。
my_foods=['pizza','falafel','carrot','cake']
friend_foods=my_foods[:]


元组
    Python将不能修改的值称为不可变的，而不可变的列表被称为元组。使用圆括号而不是方括号来标识
        dimensions=(200,50)
        print(dimensions[0]) #打印第一个元组200
        for i in dimensions: #遍历元组
            print(i)
    修改元组变量
        dimensions=(400,100) #不能修改元组中的元素，但可以给存储元组的变量赋值。




if语句
    if语句的核心都是一个值为True 或False 的表达式，这种表达式被称为条件测试。Python根据条件测试的值为True还是False来决定是否执行if语句中的代码。如果
条件测试的值为True，Python就执行紧跟在if语句后面的代码；如果为False，Python就忽略这些代码。

car='bmw'   #一个等号表示赋值
car=='bmw'  #两个等号是'相等运算符'。忽略大小写时，可将变量的值转换为小写car.lower()==car
car!='bwm'  #要判断两个值是否不等，可结合使用惊叹号和等号（!= ），其中的惊叹号表示不

数字比较：=,!=,>,<,>=,<=
检查多个条件：and,or

cars=['audi','bmw','subaru','toyota']
for i in cars: #遍历cars列表
      if i=='bmw': #如果是bmw,则改为大写，其他首字母大写
         print(i.upper())
      else:
         print(i.title())

    //检查特定值是否包含在列表中，使用关键字 in ;不包含则使用 not in
    requested_toppings=['mushrooms','onions','pineapple']
    'mushrooms' in requested_toppings   #True
    'pepperoni' in requested_toppings   #Flase

    布尔表达式，结果要么为True,要么为False
