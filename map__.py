#
#
#
#
# list1=[1,3,4,7,8]
# list2=[3,5,9,0,1]
# list3=[11,12,13]
#
# def summ(a,b,c):
#     return a+b+c
#
# result=list(map(summ,list1,list2,list3))
#
#
# print(result)
#
# result2=list(map(lambda  x,y,z : x+y+z,list1,list2,list3))
# print(result2)
#
# products=[['Shoes: ', 150],['Pants: ',120],['Jakke',100],['T-shirt', 200]]
#
# def discount(x):
#     product,price=x[0],x[1]
#     price=price* (9/10)
#     return [product,price]
#
# result=list(map(discount,products))
# print(result)

names=['AhMeT','aYsE','oNur','HUSeyiN']

names2=list(map(lambda x : x.lower(),names))
print(names2)

names3=list(map(lambda x : x.upper(),names))
print(names3)

names4=list(map(lambda x : x.capitalize(),names))
print(names4)