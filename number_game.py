import random

def game():
    name = input('как тебя зовут?')
    print(f'{name}, компьютер загадал число от 1 до 100. Отгадай его за 7 попыток')
    secret_number = random.randint(1,100)
    tries = 7
    while tries >0:
        tries -=1
        print(f'Попыток: {tries}')
        user_number =input (f'{name},введи число')
        user_number = int(user_number)
        if user_number == secret_number:
            print(f'{name} ты победил')
        elif secret_number < user_number:
            print('ваше число больше моего')
        elif secret_number > user_number:
            print('ваше число меньше моего')
