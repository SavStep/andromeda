import random

file = open('logins.txt',mode="w",encoding='utf-8')
file.write('i owl')
file.close()

file = open('passwords.txt',mode="w",encoding='utf-8')
file.write('wasd 123456')
file.close()

def read_users(filename):
    file = open('file.txt',mode="w",encoding='utf-8')
    data = file.read()
    file.close()
    return data.split()
coin = random.randint(1,2)
if coin ==1:
   print("решка")
else:
   print("орёл")
flag = False
while flag == False:
   login = input ('введите ваш логин:' )
   password = input ('введите ваш пароль:')
print(f'вы ввели : {login} и {password}')
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