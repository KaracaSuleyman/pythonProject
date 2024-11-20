#
# list1=[1,2,3,4,5,12,103,15,17,19,323,25,246,47,166]
#
# def isodd(x):
#     if x%2==0:
#         return True
#     return False
#
#
#
# evenlist=list(filter(isodd, list1))
#
# print(evenlist)
#
# even2list=list(filter(lambda x:x%2==0, list1))
# print(even2list)
#
#
#
# def tenss(x):
#     if x >= 10 and x <100:
#         return True
#     return False
# tenslist=list(filter(tenss, list1))
# print(tenslist)
#
# tens2list=list(filter(lambda x: 10 <= x < 100, list1))
# print(tens2list)




# kelimeler=['Mirror','Adam','Ananas','Banan','Shoes','Amarok','Ana','Ada','Kazak']
# kelimelerlower=list(map(lambda x: x.lower(), kelimeler))
# print(kelimelerlower)
# start_with_A=list(filter(lambda x:x.startswith('a') , kelimelerlower))
# print(start_with_A)
#
#
# inside_in_A=list(filter(lambda  x : 'a' in x, kelimelerlower))
# print(inside_in_A)
#
# palindoromList=list(filter(lambda x : x== x[::-1] , kelimelerlower))
# print(palindoromList)



# list1=[1,2,(1,2,3),True,'String','example',{1,2,4}]
#
# strlist=list(filter(lambda x : isinstance(x,str),list1))
# print(strlist)


list1=[{'Name:' :'Jhon' , 'Age:':23},{'Name:' :'Smith' , 'Age:':33},{'Name:' :'Ronaldo' , 'Age:':37},{'Name:' :'Arda' , 'Age:':19},{'Name:' :'Adam' , 'Age:':29},
       {'Name:' :'Arne' , 'Age:':69},{'Name:' :'Agot' , 'Age:':68}]


starts_With_a=list(filter(lambda x : x['Name:'].startswith('A')  , list1))
print(starts_With_a)

above_20=list(filter(lambda x : x['Age:']>20 , list1))
print(above_20)
under_20=list(filter(lambda x : x['Age:']<20 , list1))
print(under_20)