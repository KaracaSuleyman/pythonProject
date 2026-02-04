import calendar
import datetime
import os
import random
import  math



from myModule import *

courses=['Math','History','CompSci', 'Physics']


index= find_index(courses,'CompSci')
#print(index)

#print(test)

#print(sys.path)

random_courses= random.choice(courses)
#print(random_courses)

sum= math.radians(90)
#print(math.sin(sum))

today =datetime.date.today()
#print(today)

call = calendar.isleap(2024)
#print(call)


print(os.getcwd())




