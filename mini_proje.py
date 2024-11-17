
with open('text.txt', 'r',) as f:
    with open('passed.xtx', 'w') as passsss:
        with open('failed.xtx', 'w') as fails:
            contents = f.readlines()
            m =0
            for line in contents:
                if m==0:
                    m+=1
                    continue
                line = line.replace('\n','')
                space_num=0
                space_index=[]
                index=0
                for char in line:
                    if char==' ':
                        space_num+=1
                        space_index.append(index)
                    index+=1

                name_Surname=line[:space_index[0]]
                surname= name_Surname.split('-')[-1]
                name=name_Surname[:name_Surname.index(surname)-1].replace('-',' ')
                point=line.split(' ')[-1]
                point=point.split('/')
                first_exam=int(point[0])
                second_exam=int(point[1])
                final_exam=int(point[2])
                ort = first_exam * 0.3 + second_exam * 0.3 + final_exam * 0.4
                branch= line[space_index[0]+1:space_index[len(space_index)-1]]

                if ort >= 70 and final_exam >= 70:
                    passsss.write(name)
                    passsss.write(' ' * (25-len(name)))
                    passsss.write(surname)
                    passsss.write(' ' * (25 - len(surname)))
                    passsss.write(branch)
                    passsss.write(' ' * (25 - len(branch)))
                    passsss.write(str(round(ort,1)))
                    passsss.write(' ' * 21 )
                    passsss.write('Passed')
                    passsss.write('\n')

                else:
                    fails.write(name)
                    fails.write(' ' * (25 - len(name)))
                    fails.write(surname)
                    fails.write(' ' * (25 - len(surname)))
                    fails.write(branch)
                    fails.write(' ' * (25 - len(branch)))
                    fails.write(str(round(ort, 1)))
                    fails.write(' ' * 21)
                    fails.write('failed')
                    fails.write('\n')







