

language = "Python"

if language == "Python":
    print(" Language is Python")

elif language == "Java":
    print(" Language is Java")

else:
    print(" Language is other")

user= 'Admin'
logged_in= False


"""c="Admin"
d= "Ad"+'min'


print(id(c))
print(id(user))
print(d)
print(id(d))"""



if logged_in and user == "Admin":
    print("Logged in as Admin")
elif user == "Admin" and not logged_in:
    print("Hey admin! you dont loggin in")
elif logged_in and not user == "Admin":
    print("Loggin in is anybody")
else:
    print("Hey you! You are not Admin and not logged in")


