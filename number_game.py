import random
print('Компьютер загадал число от 1 до 100. Отгадай его за 7 попыток')
secret_number = random.randint(1,100)
tries = 7
while tries <0:
    tries -=1
    user_number =input ('введите число')
    user_number = int(user_number)
    if user_number == secret_number:
        print('ты победил')
    elif secret_number < user_number:
        print('ваше число больше моего')
    elif secret_number > user_number:
        print('ваше число меньше моего')
