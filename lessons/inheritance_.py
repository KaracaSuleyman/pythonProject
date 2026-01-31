class Person:
    solary_range=1.1
    def __init__(self, name, surname, solary):
        self.name = name
        self.surname = surname
        self.solary = solary
        self.email= name+surname+"@company.com"

    def show_details(self):
        return f'Ad: {self.name}, SurName: {self.surname}, Solary: {self.solary}, Email: {self.email}'


personal1=Person("John", "Doe", 45000)
personal2=Person("Arne", "Solheim", 65000)


class Developer(Person):
    def __init__(self, name, surname, solary, knowlege_Langue):
        super().__init__(name, surname, solary)             #super() fonksiyonu dededen gelen bilgileri alir ekstra yazmaya gerek kalmaz
        self.knowlege_Langue = knowlege_Langue
    solary_range=1.2
    def show_details(self):
        return f'Ad: {self.name}, SurName: {self.surname}, Solary: {self.solary}, Email: {self.email}, Knowlege Langue: {self.knowlege_Langue}'

    def tell_me_your_langue(self):
        return f'Bilidigi dil: {self.knowlege_Langue}'


developer1=Developer("Suleyman", "Karaca", 66000, 'Python')
developer2=Developer("James", "Smith", 75000,'Java')

class Administor(Person):
    def __init__(self, name, surname, solary, workers=None):
        super().__init__(name,surname,solary)
        if workers== None:
            self.workers =[]
        else:
            self.workers = workers

    def worker_add(self, worker):
        if worker not in self.workers:
            self.workers.append(worker)

    def delete_worker(self, worker):
        if worker in self.workers:
            self.workers.remove(worker)

    def show_worker(self):
        for worker in self.workers:
            print(worker.show_details())


administor1=Administor("Erlend", "Thomas", 125000, )

administor1.worker_add(personal1)
administor1.worker_add(developer1)

print(administor1.show_details())
administor1.show_worker()
print('-'*100)
administor1.delete_worker(personal1)
administor1.show_worker()

print('-'*100)
administor2=Administor("Alex", "De Souza", 135000,[personal1,personal2,developer1,developer2])
print(administor2.show_details())
administor2.show_worker()

print('-'*100)
print(isinstance(administor1, Developer))

print(issubclass(Developer, Person))