

student= { "name" : "Jhon", "age" : 25, "city" : "New York", "courses" : ["Math", "Compsci"] }



student["phone"]= "555-555-5555"
print(student)

print(student.get("name", "not found!"))

student["name"]="Jane"
print(student)

del student["name"]
print(student)
city = student.pop("city")
print(city)

print(student)

student["name"]="Jhon"
print(student)



list = [1,2,3,4,5]
set1 = set(list)
print(set1)