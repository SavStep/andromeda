# fruits = ['яблоко','драконий фрукт','груша']
# for item in fruits:
#     print(item)
# fruits = iter(fruits)
# print(next(fruits))
# print(next(fruits))
# print(next(fruits))
# print(next(fruits)+'- её нелзя скушать')
# name = 'итерация'
# name = iter(name)
# duz =('дуц')
# daz =('дац')
# duz =iter(duz)
# daz =iter(daz)
# def party():
#     print(next(duz))
#     print(next(daz))

#     for i in range(5):
#         party()
class Number:
    def __iter__(self):
        self.a = 1
        return self
def __next__(self):
    b = self.a
    self.a +=1
    return b
number = Number()
number = iter(number)
print(next(number))
print(next(number))
print(next(number))