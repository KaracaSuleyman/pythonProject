

courses = ["History", "Math", "Physics", "CompSci"]


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



courses_str = ", ".join(courses)
print(courses_str)
new_list = courses_str.split(", ")
print(new_list)


# Tuples

