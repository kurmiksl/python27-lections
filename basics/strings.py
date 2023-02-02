"==========================Строки========================"
# строки - неизменеямый тип данных, предназначенный для хранение текста (последовательности символов)

trings1 = 'строка в одинарных кавычках'
strings2 = "строка в двойных кавычках"
strings3 = "Don't"
strings4 = 'Study in "Makers Incubator"'
string5 = '''
 Многострочный 
текст 
тут можно использовать 'любые' "кавычки"
'''
string7 = 'hello' + '' + 'world'  # 'hello world'

strings8 = 'hello' *  3 # 'hellohellohello'
strings9 = 'hello ' + str(1) 

"=========================Экранизация строк========================"
print('hello/nwotld')
'/n' # перенос на новую строку
'/t' # отступ (табуляция)
print('/n - это перенос на новою строку')
'//' # отображение /
'/'' # отображение '
"/"" # отображение "
'/r' # перенос каретки в начало строки
'/v' # аеренос на новую строку сосмещением вправона длину предыдущей строки

# hello  world
'hello/vworld/vmakers'
# hello
#      world
#           makers
'123456789/rhello'
# hello6789



"=====================================Индексы================================="
# Индекс - порядковый номер символа в строке (начиная с 0)
'h e l l o' 
'0 1 2 3 4'
#      -2 -1

string = 'hello world'
print(string[-3])
string[0] # 'h' 
string[-1] # 'd'
string[5] # ' '
# срез - часть строки
string[6:9] #'wor'
string[0:5] # 'hello'
string[0:6] # 'hello '
string[:6] # 'hello '
string[7:] # 'orld'
string[:] # 'hello world'
string[0:11:2] # 'hlowrd'
string[::2] # 'hlowrd'
string[::-1] # 'dlrow olleh'



"=================================Форматипование строк================================="
title = 'Пирог'
price = 35
string =  f'Название:{title}, цена: {price}'
# Название: Пирог, цена: 35


format1 = 'Название: %s, цена: %s'
print(format1 % ('rice', 80))

# Название: rice, цена: 80
format2 = 'Название: {}, цена: {}'
print(format2.format('груша', 60)) 
# Название: груша, цена: 60

"=================================================Медоты строк========================================"
# Метод это функция, которая принадлежит определенноиу типу данных, обращаемся к ней через точку
print(dir(str)) 
dir(str) # посмотреть все доступные методы для данного типа данных

'hello' . upper() # 'HELLO'
'HELLO' . lower() # 'hello'
'hello WORLD' . swapcase() # 'HELLO world'
'HeLLo'. swapcase() # 'hEllO'
'hello world' . title() # 'Hello World'
'hello world' . capitalize() # 'Hello world'
'hello'.center(11) # '     hello    '
'hello'.center(11, '-')   # '---hello---'

'hello'.count('l') #2
'hello'.count('ll') #1
'Hello'.count('hello') #0
'hello'.count('') #6

'hello world'.split() #['hello', 'world']
'hello world'.split('o') # ['hell', ' w', 'rld']

' '.join(['hello', 'world']) # 'hello world'
'%'.join(['hello', 'world']) # 'helloworld'

'hello world'.find('w') # 6
'hello world'.find('wor') # 6
'hello world'.find('o') # 4
'hello world'.rfind('o') # 7
