##summa = 0
##for i in range(1,101):
##    summa+=i
##print (summa)
##fact = 0
##for i in range(1,21)
##fact *=1
##print(fact)

##books = ['серебряный глаз',"гарри потер и узник азкабана",'дневник номер 3']
##print(books[2])
##
##lenth = len(books)
##print(f'в списке {lenth} элемента')
##for i in range(lenth):
##      print(i+1)
##      print(books[i])

def robot_backward():
      print(f'робот идёт назад')
def robot_forword():
      print(f'робот идёт вперед')
def robot_take(item):
      print(f'робот берет {item}')
def robot_put(item,backpack):
      if item in backpack:
            print(f'робот кладёт {item}')
      else:
            print('ничего нет')
def robot_take(item):
      print(f'робот берет {item}')
      return item
      
backpack=[]
while True:
      key = input('Какая команда: ')
      if key == 'w':
            robot_forword()
      elif key == 's':
            robot_backward()
      elif key == 'e':
            thing = input('что брать?')
            robot_take(thing)
      elif key.startswich('бери'):
            words = key.split()
            thing = robot_take(words[1])
            backpack.appent(thing)
      elif key.startswich('клади'):
            words = key.split()
            robot_put(words[1],backpack)
