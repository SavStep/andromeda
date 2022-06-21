import  random
from tokenize import Number

programmers = ['Степан','Савелий','Ярослав','Артемий','Тамерлан','Роман']

print(f'победил{programmers[random.randint(0,5)]}')
win_counter = [0] * len(programmers)
print(win_counter)
for i in range(1000):
    win_counter[random.randint(0,5)]+=1

print(win_counter)
m = max(win_counter)
i = win_counter.index(m)
print(f'победил{programmers[i]}он набрал{win_counter[i]}')

cars_counter = 0
summa = 0
number_counter = 0
interations = 0
for i in range(10**6):
    car_number = random.randint(0,999)#номер машины
    cars_counter += 1
    number_counter+= car_number#сумма номеров машин
    if number_counter>=1000:
        summa +=cars_counter
        number_counter = 0
        cars_counter = 0
        interations+= 1
print(summa/interations)