import random
coin = random.randint(1,2)
if coin ==1:
    print("решка")
else:
    print("орёл")
flag = False
while flag == False:
    login = input ('введите ваш логин:' )
    password = input ('введите ваш пароль:')
    #print(f'вы ввели : {login} и {password}')
    if login == "its savee" and password == "62184t82":
        print("вы вошли в аккаунт")
        flag = True
    elif login == 'ок яндекс' and password == "тумба юмба":
        print("привет создатель!")
        flag = True
    elif login =='':
        print("вы забыли ввести логин")
    elif password == '':
        print("вы забыли ввести пароль")
    else:
        print("ты кто такой давай до свидания")
if flag == True:
    vegatables = 116
    children = 23
    print(vegatables//children)
    buble_gum = 17
    money = 38564
    print('Саша купит ' + str(money//buble_gum) + ' жвачек')
    print('Останется ' +str(money%buble_gum) + ' рублей')
    money = 5000
    fruits = 60/2 + 20*3
    fruits_with_sale = 0.8 * fruits
    sweets = 500
    print(money - (fruits_with_sale) - sweets)
    note = 35 + 0.1* 35
    print(700//note)
    print(f'макксимум (700//note) блокнотов')
    eggs = True
    if eggs == True:
        bread = 'батон'
    print(10*bread)
    print(bread)
