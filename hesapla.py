

print("hesapla")
koli=(60*100*45)+((65*45*35)*3)+(50*35*30)+(45*60*25)
cuval=(6 * (100* 120 * 40))
print(koli)
print(cuval)
toplam=koli+cuval
print(toplam)


# cm³ to m³ conversion function
def cm3_to_m3(cm3):
    return cm3 / 1_000_000

print(cm3_to_m3(toplam))

x=(cm3_to_m3(toplam))

print(f'{x*200: .2f}')

# Result
