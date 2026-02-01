

courses = ["History", "Math", "Physics", "CompSci"]

"""
print(len(courses))


courses.insert(0, "Art")

print(courses)

courses.append("Education")
print(courses)

courses.extend(["Biology", "Chemistry"])
courses_2 = ["Geo", "Statistics"]
courses.extend(courses_2)
print(courses)


courses.sort()
print(courses)  

for index, course in enumerate(courses):
    print(index, course)    

 """



courses_str = " - ".join(courses)
print(courses_str)

new_courseslist= courses_str.split(" - ")
print(new_courseslist)


# Tuples
"""
tuple_1= ("History", "Math", "Physics", "CompSci")
tuple_2= tuple_1

tuple_1[0]= "Education"
print(tuple_1)


# tuple not working like list. You dont change tuple inside. but you can also playing with list

"""
#Sets

        # set likes  unorderer list

"""
set1= {"History", "Math", "Physics", "CompSci"}
print(set1)
set1[0]= "Education"
print(set1)
"""