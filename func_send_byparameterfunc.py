

# #list=[1,2,3,4,5,6,7,8,9]
# func= x*x
# result=[1,4,9,16,25,36,49,64,81]


list1=[1,2,3,4,5]
list2=[1,3,3,4,5,8,9,11]

def power(x):
    return x*x
def cube(x):
    return x*x*x

def map_func(func,list):
    result=[]
    for item in list:
        result.append(func(item))

    return result


print(map_func(cube,list1))
print(map_func(power,list2))