import random
import cowsay


def bulls_cows():

    cowsay.miki('компьютер загадал четырехзначное число,если вы угадали число но оно не на том месте то,компьютер скажет что есть корова.если число на том же месте то это бык')
    number = random.randint(1000,9999)
    number = str(number)
    user_number = ""
    while user_number != number:
        user_number =input ('введи число: ')
        if user_number.isdigit == False:
            print("Введите имменно число")
            continue
        if len(user_number) != 4:
            print('введите четырехзначное число')
            continue
        bulls = 0
        cows=0
        list=[]
        for letter in number:
            list.append(letter)
        for letter in user_number:
            if letter in list:
                cows+=1
        for i in range(4):
            if user_number[i] == list[i]:
                bulls += 1
                cows -= 1
        print(f"У вас коров: {cows} и быков: {bulls}.")
    print(" Вы выйграли!")

if __name__ ==  '__main__':
    bulls_cows()