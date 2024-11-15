import random
#
# for i in range(10):
#     #print(random.random())     # random rastgele 0 ile 1 araliginda  kac tane uret dediysen sayi uretiyor..
#     #print(random.uniform(3,6))      #uniform ise istedigin aralikta rastgele
#     #print(random.randint(1,5)) #randint alt ve ust sinir icinde olan tam sayialr uretir.!!! SADECE BUNDA ALT VE UST SINIR ALIR
#     print(random.randrange(0, 15,2)) #randrange de de iki deger arasinda ne kadar farkli arttirmak istiyoruz buluyoruz

# list=["sari", "Lacivert","Mor","Turuncu","Bordo","Koknar"]
#
# print(random.choice(list))              #Listenin icinden rastgele index okur
#
# random.shuffle(list)                    #adi uzerinde listeyi karistiriyor
# print(list)
#
# print(random.sample(list,2))        #Listeden rastgele kac tane eleman istersen onlari getiriyor

# Ornegin bir zari 100 kere attigimizda zarlarin gelme olasiligi nedir?
#zarlar={1:0,2:0,3:0,4:0,5:0,6:0}
#
# for i in range(100000000):
#     zar=random.randint(1,6)
#     zarlar[zar]+=1
#
# for zar in zarlar:
#     print(f"{zar} gelme olasiligi: {zarlar[zar] /100000000}")

# tavla da 6 6 gelme olasiligi nedir

# altialti=0
# deneme_Sayisi=0
# while True:
#     deneme_Sayisi+=1
#     zar1=random.randint(0,6)
#     zar2=random.randint(0,6)
#     if zar1==6 and zar2==6:
#         altialti+=1
#     if altialti ==10:
#         print(f"10 kere  6-6 gelemsi icin zarlar {deneme_Sayisi} kadar atilmasi gerekir")
#         break
#

