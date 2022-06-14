import random
a = random.randint(1,100)
b = int(input('Привет, введи число от 1 до 100: '))
while True:
    if a == b:
        print('Ты угадал!')
        break
    elif a < b:
        b = int(input('слишком много, болбес, надо лунтика смотреть!!!!!'))
    elif a > b:
        b = int(input('слишком мало, stupid, надо лунтика смотреть!!!!!'))















