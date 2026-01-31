
class Footbolplayer:


    def __init__(self, name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age



    def __eq__(self, other):
        if self.name == other.name and self.surname == other.surname:
            return True

        return False


    def __add__(self, other):
        isim=self.name[0]+other.name[0]
        surname=self.surname[0]+other.surname[0]
        age=self.age+other.age
        return Footbolplayer(isim,surname,age)

    def __lt__(self, other):
        if self.age < other.age:
            return True
        return False


    def __gt__(self, other):
        if self.age > other.age:
            return True
        return False



footbalplayer1=Footbolplayer("Serhat","Akin",18)
footbalplayer2=Footbolplayer("Serhat","Sakin",18)
footbalplayer3=footbalplayer2+footbalplayer1

print(footbalplayer1==footbalplayer2)
print(footbalplayer3.age)
print(footbalplayer1 >(footbalplayer2))


