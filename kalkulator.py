num1 = input('введите первое число: ')
num1 = int(num1)
operator = input("ведите знак:")
num2 = input('введите второе число:')
num2 = int(num2)
def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b


if operator == '+':
    answer = plus(num1,num2)
elif operator == '-':
    answer = minus(num1,num2)
elif operator == '*':
    answer = multiply(num1,num2)
elif operator == '/':
    answer = divide(num1,num2)
print(f'ответ {answer}')
stop = input('закончить?')
if stop == 'да'
    break