






list=[('Smith',23),('Jhon',45),('Eliam',35)]
list.sort(key=lambda x : x[1])


list2=[{'Name':'Jhon','Surname':'Doe','Age': 23},{'Name':'Jhon','Surname':'Doe','Age': 23},
                            {'Name':'Carlos','Surname':'Donny','Age': 33},{'Name':'Jhon','Surname':'Snow','Age': 23}]
list2.sort(key=lambda x : x['Surname'])
print(list2)

