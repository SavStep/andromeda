class Phone:
    model = 'Samsung'
    oper_system = 'Android'
    batary = 12000
    def __init__(self,model):
        self.model = model 
phone1 = Phone()
print(phone1.batary)
phone2 = Phone
print(phone2.batary)

class Person:
    def __init__(self,first_name,last_name,gender):
        self.first_name = first_name#характер(атрибут)
        self.last__name = last_name
        self.gender = gender 
    def hobby(self):
        if self.first_name == 'morty':
            print('likes go to Rick')
        if self.first_name == 'ogurchik':
            print('likes kill the cockroachers')
        if self.first_name == 'gomer':
            print(' he likes drinking beer ')
morty = Person(first_name='morty' ,last_name='mortu')
gomer = Person(first_name='gomer' ,last_name='simpson')
ogurchik = Person(first_name='ogurchik' ,last_name='rick')
class Student(Person):
    def hobby(self):
        Person.hobby(self)
        print('любит играть на фа - но' )
    def learn(self):
        print(f'{self.first_name} учится')
