from datetime import date
a='Pyhton'
print(str(a))
print(repr(a))



today=date.today()
print(today)
print(str(today))
print(repr(today))
print('='*100)
print('='*100)
print('='*100)
print()

class Company:
    name: object

    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age

    def __str__(self):
        return 'Name: {}, Surname: {}'.format(self.name, self.surname)

    def __repr__(self):
        return f'Futbolcu ({self.name},{self.surname},{self.age})'

worker1=Company('Tuncay','Sanli','23')

print(worker1)
print(repr(worker1))
print()
print('='*100)
print('='*100)
print('='*100)

