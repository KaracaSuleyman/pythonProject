list_methods = []
for method in dir(list):
    if method.startswith('__'):
        continue
    list_methods.append(method)


set_methods = []
for method in dir(set):
    if method.startswith('__'):
        continue
    set_methods.append(method)


string_methods = []
for method in dir(str):
    if method.startswith('__'):
        continue
    string_methods.append(method)


tuple_methods = []
for method in dir(tuple):
    if method.startswith('__'):
        continue
    tuple_methods.append(method)


dict_methods = []
for method in dir(dict):
    if method.startswith('__'):
        continue
    dict_methods.append(method)



titles=['List Methods','Set Methods','String Methods','Tuple Methods','Dict Methods']
classes=[list_methods, set_methods, string_methods, tuple_methods, dict_methods]

max_len=0

for class_name in classes:
    if len(class_name)>max_len:
        max_len = len(class_name)

with open("methods.txt","w") as f:
    for title in titles:
        # print(title, end='')
        # print(" " * (30 - len(title)), end='')
        # f.write(title)
        # print(' ' * (30 - len(title)))
        print(title.ljust(30), end='')  # Ekrana yazdırma
        f.write(title.ljust(30))  # Dosyaya yazma
   

    for i in range(max_len):
            print()
            f.write('\n')
            for class_name in classes:
                if i >= len(class_name):
                    print('-' *  7, end='')
                    print(' ' * 23,end='')
                    f.write('-'* 7)
                    f.write(' ' * 23)

                else:
                    print(class_name[i], end='')
                    print(' ' * (30 - len(class_name[i])), end='')
                    f.write(class_name[i])
                    f.write(' ' * (30 - len(class_name[i])))





