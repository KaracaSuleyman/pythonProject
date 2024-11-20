from functools import reduce
import math


list1=[2,4,6,8,9,18,12,24,36,45]

# ekok(a,b)* ebob(a,b)= a*b    ====>>>>>> ekok(a.b)= a*b / ebob(a,b)



def lcm_(a,b):
    return int(a*b//math.gcd(a,b))


lcmList=reduce(lcm_,list1)
print(lcmList)


########################### TAS KAGIT MAKAS #################

def stone_scrission(x,y):
    set1={x,y}
    if x ==y:
        return x
    if set1=={'stone','scrison'}:
        return 'stone'
    if set1=={'stone','paper'}:
        return 'paper'
    if set1=={'paper','scrison'}:
        return 'scrison'

list2=['stone','paper','paper','scrison','paper','stone','paper','paper','stone','paper']

result=reduce(stone_scrission,list2)
print(result)

