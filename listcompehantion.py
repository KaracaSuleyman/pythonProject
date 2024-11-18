



list=[1,2,3,4,5,6,7,8,9]

list2=[]
for i in list:
    list2.append(i)
print(':  list2', list2 )


list3=[numbers for numbers in list]
print(':  list3', list3 )

# Verilen listedeki elemanlarin karesini listeleyen

list4=[number*number for  number in list]
print(':  list4', list4 )

#Verilen listedeki cift rakamlardan liste olustur

list5=[ numbers for numbers in list if numbers %2==0]
print(':  list5', list5 )

# Verilen listelerdeki cift rakamlarin karelerini yazdir

list6=[number*number for number in list if number%2==0]
print(':  list6', list6 )

#listedeki 4 den buyuk cift sayialrin karelerini olustur.

list7=[number*number for number in list if number%2==0  and number>4]
print(':  list7', list7 )

# [(a,1),(b,2),(c,3),(d,4)] olacak sekilde liste olustur
numbers=[1,2,3,4]
letters='abcd'

list8=[(letter,number) for letter in  letters  for number in numbers  ]
print(':  list8', list8 )


list_a=[1,2,3,4,5,6,7,8,9]
list_b=[1,2,3,5]
#birinci listede bulunup ikinci listede bulunmayan elemanlarin karesini olustur

list9=[i*i for i in list_a if not i in list_b]
print(':  list9', list9 )


#verilen liste icindeki listedeki elemanlari tek liste halinde list=[1,2,3,4,5,6,7,8,9,10,11,12,13] olarak yazdir
list_c=[[1,2,3,4,5],[6,7,8,9],[10,11,12,13]]

list10=[j for i in list_c for j  in i  ]
print(':  list10', list10 )

# Liste nin methodlarini yazdirma
list_Method=[method for method in dir(list) if not method.startswith('_')]
print(':  list_Method', list_Method )


