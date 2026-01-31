# from audioop import reverse
#
# #
# tuple= ("Turuncu", "Yesil","Sari","Lacivert","Beyaz")
# #
# # print(tuple)
# #
# #
# # for i in tuple:
# #     print(i)
#
#
# print(type(x))
# print(len(x))
# print(x[::2])
# # list=  ["Turuncu", "Yesil","Sari","Lacivert","Beyaz"]
# #
# # for i in list:
# #     print(i)
# #
# # list[2]= "Mor"
# # print(list)
# #
#
x= {"Turuncu", "Yesil","Sari","Lacivert","Beyaz"}
#
# print(x)
# (x.add("Mor"))
# print(x)
# x.discard("Gri")                  #sectigimiz yoksa ama hata almak istemiyorsak bu yontemi kullaniz

y = {"Turuncu", "Yesil","Sari","Mor", "Kirmizi"}

#print(x.intersection(y))          #kesisimi ayni olan elemanlari yazdirir

#print(x.union(y))                 #alayini birlestirir

#print(x.difference(y))             #x in y den farkli elemanlari
#print(y.intersection(x))           #y nin x den farkli elemanlari
#
# print("Sari" in x)
# print("Turuncu" in y.difference(x))


# emptylist= []
# emptylist2= list()
#
# print(type(emptylist), type(emptylist2))             #her ikisi de bos liste olusturacak
#
# emptytuple= ()
# emptytuple2= tuple()
#
# print(type(emptytuple), type(emptytuple2))           #her ikisi de bos tuple olusturacak
# emptyset= {}
# emptyset2= set()
#
# print(type(emptyset), type(emptyset2))               #burasi onemli ikisde set OLUSTURMUYOR !!! {} dict(sozluk) olusturuyor


# ilginc= set("ILGINC")
#
# print(ilginc)                                   #setin icine ne yazarsan yat bunu kumeye donusturur. ILGINC I L G I N C olacak
#                                                     # list tuple farketmez hepsi ayni sonuca gelecek
#




personal ={"Isim" : "Ali", "Yas": 20,"Cinsiyet": "Erkek", "Hobiler": ["Resim","Muzik", "Sinema"]}     #ilk yazilan key ikincisi value

print(personal)

personal["Isim"] = "Ahmet"
# print(personal)

personal.update({"Isim" : "Mehmet", "Yas" : 30})
# print(personal)

personal["ID"]= 1234567
# print(personal)
#
# del personal["Cinsiyet"]
# print(personal)
#
# for i in personal:
#      print(i)
# for i in personal:
#      print(personal[i])
# for i in personal:
#      print(i  , personal[i])
#
#
# print(personal.keys())
# print(personal.values())
# print(personal.items())
#
# print("Mehmet" in personal.values())
# #
# for k,v in personal.items()   :
#     print(k,v)
#
# print(personal["Evli Mi"])                      #Bu sekilde yazdigimizda yoksa sordugumuz hata aliriz...
#print(personal.get("Evli Mi"))                   #Bu sekilde sorarsak yoksa none degeri doner ve hata almayiz

#print(personal.get("Evli Mi", "Bulunamadi"))       #get fonksiyonuna virgulden sonraki ikinci degeri ilk deger bulunamazsa ekrana yazialcak olan cikar



