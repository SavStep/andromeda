
##    while counter <=100:
##        print(counter)
##        counter +=1
##    while counter <=0:
##        print(counter)
##        counter -=1
##rain =  True
##
##while rain ==   True:
##    print('пью чай')
##    stop = input ("дождь закончился!")
##    if stop == 'да':
##        print('может пойдём на улицу')
##        break
##game = True
##while game:
##    print('игра началась')
##    stop = input ("хотите выйти из игры?")
##    if stop == 'да':
##        print('игра окончена')
##        break
##number = 1
##while number < 20:
   ##print(number)
    ##number += 1
#for number in range(20):
   # print(number)
##for i in range (5):
##    start = input ('с какого числа вывести диапазон')
##    n = input ('до какого числа вывести диапазон')
##    n = int (n)
##    start = int (start)
##    print(list(range(start,n)))
##our_group = []
##for number in range(3):
##    name = input('как тебя зовут')
##    print(f'привет,{name}')
##    our_group.append(name)
##    print(our_group)
print('агазин игр steam')
flag =  True
wish_list = []
while flag:
    print('добоо пожаловать')
    print('выбери действие:')
    print('1 - добавить игру в список желаемого')
    print('2 - удалить игру из списка желаемого')
    print('3 - купить игру')
    print('4 - поиграть в игру')
    print('5 - вывести все игры')
    print('6 - выйти из програмы')
    action = input('->')#ввод от пользователя(какое действие)
    #action = int (action)
    if action == '1':
        game = input('какую игру ты бы хотел?')
        if game not in wish_list:
            wish_list.append(game)
            print(f'{game} добавлена')
        else:
            print('ошибка,такая игра уже есть')
    elif action == '5':
        if len(wish_list) ==0:
            print('у вас нет игр')
        else:
            print(wish_list)
    #elif action = 
