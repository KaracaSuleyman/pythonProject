

class Person:
    def __init__(self, name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        self.nameSurname1= name + ' ' + surname

    @property
    def email(self):
        return f"{self.name}.{self.surname}@company.com"

    @property
    def nameSurname(self):
        return f'{self.name} {self.surname}'

    @nameSurname.setter
    def nameSurname(self, name):
         name, surname = name.split(' ')
         self.name = name
         self.surname = surname

    @nameSurname.deleter
    def nameSurname(self):
        print(f'isim silindi')
        self.name = None
        self.surname = None



person1 = Person("John","Smith",18)

person1.name='Solheim'

person1.nameSurname='Smith Doe'

del person1.nameSurname

print(person1.email)

print(person1.nameSurname)

print(person1.name)


