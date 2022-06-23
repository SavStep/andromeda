import random
import number_game
import mortal_combat
import game_store
KEY = 5

def crypt_password(password, key):


    '''
    Шифрование пароля
    '''
    crypt = ""
    for bukva in password:
       # print(ord(bukva))
        crypt += chr(ord(bukva) ^ (key))
    return (crypt)# возвращает пароль


def registration(): 
    '''регистрация нового пользователя'''
    print('Сейчас зарегистрируем вас')
    login = input('введите ваш логин: ')
    password = input('введите ваш парольчик: ')

    file = open('logins.txt', mode="a", encoding='utf-8')
    file.write(f'{login}' + ' ')
    file.close()
    file = open('passwords.txt', mode="a", encoding='utf-8')
    file.write(f'{crypt_password(password,key = KEY)}'+ ' ')
    file.close()
    print('Регистрация завершена. Пользуйтесь на здоровье!')



def read_users(filename):
    
    file = open(filename, mode="r", encoding='utf-8')
    data = file.read()
    file.close()
    return data.split()
def sign_in(flag):
    login_list = read_users('logins.txt')
    password_list = read_users('passwords.txt')
    login = input('введите ваш логин:')
    password = input('введите ваш пароль:')
    print(f'вы ввели : {login} и {password}')
    if login in login_list and crypt_password (password,key=KEY) in password_list:
       print("вы вошли в аккаунт")
       flag = True
    elif login =='':
       print("вы забыли ввести логин")
    elif password == '':
       print("вы забыли ввести пароль")
    else:
       print("ты кто такой давай до свидания")
    return flag, login

def chat(login):
    file = open('chat.txt', mode="r", encoding='utf-8')
    data = file.read()
    print(data)
    file = open('chat.txt', mode="a", encoding='utf-8')
    while True:
        your_message = input('Сообщение("выйти", чтобы остановить чат): ')
        if your_message == 'выйти':
            break
        file.write(f'{login} : {your_message}')
    file.close()


login_list = read_users('logins.txt')
password_list = read_users('passwords.txt')
flag = False
while flag == False:
    if flag == False:#если вы не вошли
        way = input('что вы хотите сделать? 1 - зарегестрироваться,  2 - войти  ')
        if way == '1':
            registration()
        elif way == '2':
            flag, login = sign_in(flag)
    else:
        way = input('''что вы хотите сделать? 
        1 - выйти из аккаунта 
        2 - выйти из программы 
        3 - открыть чат 
        4- cыграть в угадай число
        5- посмотреть MORTAL COMBAT
        6- зайти в стим''')
        if way == '1':
            flag = False
        elif way == '2':
            print('досвидания')
            break 
        elif way == '3':
            chat(login)
        elif way == '4':
            number_game.game()
        elif way == '5':
            mortal_combat.fighting()
        elif way == '6':
            game_store.store()
# coin = random.randint(1, 2)
# if coin == 1:
#    print("решка")
# else:
#    print("орёл")
