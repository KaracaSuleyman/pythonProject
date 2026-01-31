from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class personal:
    personal_count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        personal.personal_count += 1


    @classmethod
    def created_by_Str(cls,str_):
        name, age_str = str_.split('-')
        age = int(age_str)  # Yaşı sayıya çevir
        return personal(name, age)

    @classmethod
    def created_by_birth_day(cls,name,birth_date):
        return cls(name,date.today().year-birth_date)

    @staticmethod
    def calculate_to_birth_year(personal):
        return date.today().year -personal.age




person1 = personal("John", 25)
person2 = personal("Arne", 45)
person3 = personal.created_by_Str("Arne-36")
person4 = personal.created_by_birth_day('Elif', 1968)
print(person4.age)
print(personal.calculate_to_birth_year(person3))