

def first_function(greeting, name= "Guest"):
  return  f' {greeting} {name}'

#print(first_function('Hello'))


"""def student_info(*courses, **student):
  print(courses)
  print(student)

student_info('Math', 'Geo','CompSci', name='Jhon', surname ='Due', age=20)
      """


month_days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leapYears(year):
  return  year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    


def day_in_month(year, month):
  if not 1 <= month <= 12:
    return 'Invalid month'

  if month == 2 and is_leapYears(year):
    return 29

  return month_days[month-1]



print(is_leapYears(2026))
print(day_in_month(2028, 2))
