#XOR - исключающий или
#1^1=0
#0^0=0
#1^0=1
#0^1=1

# a = 10#1010
# b = 5#0101
# print(a,b)
# a = a ^ b# 1010 ^ 0101 = 1111
# print(a)
# b = a ^ b# 1111 ^ 0101 = 1010
# print(b)
# a = a ^ b# 1010 ^ 1111 = 0101
# print(a)
# print(a,b)

def crypt_password(password,key):
    '''
    Шифрование пароля
    '''
    crypt=""
    for bukva in password:
       # print(ord(bukva))
        crypt +=chr(ord(bukva) ^(key))
    return (crypt)

def registration():
    '''регистрация нового пользователя'''
    print('теперь вы зарегестрировались')