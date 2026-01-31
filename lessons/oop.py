


class Personal:             #Class olusturduk
    personal_count=0
    def __init__(self, name, surname,age,mail,id,salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.name = name
        self.surname = surname
        self.age = age
        self.mail = mail
        self.id = id
        self.salary = salary
        Personal.personal_count+=1
    def personal_Info(self):
        print(f'Ad= {self.name} Soyad= {self.surname} Yas= {self.age} Mail= {self.mail} ID= {self.id} Maas= {self.salary}')



personal1 = Personal("John", "Smith",12,"jhon@smith.com",1,23000)
personal2 = Personal('Jhon','Doe',15,"jhon@sdoe.com",2, 39000)


print(personal2.__dict__)
print(Personal.personal_count)

