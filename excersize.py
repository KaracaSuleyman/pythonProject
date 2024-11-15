#1 Kullanıcının girdiği bir cümledeki her kelimeyi tersine çeviren bir döngü yazın . Örneğin, "Hello world"should be "olleH dlrow".
# text= "Hello Worlds".split()
# i=0
# reserveText=[]
#
# while i < len(text):
#     reserveText.append(text[i][::-1])
#     i+=1
# x=" ".join(reserveText)
# print(x)

#2 Kullanıcının girdiği 1'den 'e kadar olan forsayıların harmonik toplamını hesaplayıp yazdıran bir döngü kullanın .
#
# n=int(input("Enter a number: "))
# harmonic_mean=0.0
# for i in range(1,n+1):
#     harmonic_mean=harmonic_mean+1/i
# print(harmonic_mean)

#3 Bir listedeki her değer için yıldız işareti yazdırarak bir histogram oluşturmak için bir döngü yazın for. Örneğin, liste için [3, 5, 2]şunu yazdırın:

# list=[3,5,2]
#
# for i in list:
#     print("*" *i)

#4 50'den 1'e kadar tüm tek sayıları yazdıran bir döngü yazın .
# list=[]
# for i in range(50,0,-1):
#     if i % 2 != 0:
#         list.append(i)
#
# print(list)

#5 Kullanıcıdan tekrar tekrar bir sayı girmesini istemek için bir döngü kullanın . Kullanıcı negatif bir sayı girerse durun,
                                        # sonra girilen sayıların toplam sayısını yazdırın.
# toplam=0
# i=0
# while i>=0:
#     i=int(input("Enter a number:"))
#     if i<0:
#         break
#     toplam+=i
# print(toplam)

#6 1'den 7'ye kadar olan sayıların küplerinden oluşan bir liste oluşturan bir döngü kullanarak bir program yazın .

# list=[]
# for i in range(1,8):
#     list.append(i**i*i)
# print(list)

#7 Kullanıcıdan bir cümle alan ve forcümle içindeki toplam kelime sayısını saymak için bir döngü kullanan bir program oluşturun.

# text=input("Enter a sting")
# list=text.split(" ")
#
# count=0
# for i in range(len(list)+1):
#     if i>= len(list):
#         break
#     count=count+1
# print(count)

#8 Bir kelime listesi üzerinde yineleme yapan ve yalnızca "a" harfini içeren kelimeleri yazdıran bir döngü yazın .
                        # Liste:["apple", "berry", "orange", "grape", "peach"]

# list=["apple", "berry", "orange", "grape", "peach"]
# list2=[]
# for i in list:
#     if "a" in i:
#         list2.append(i)
# print(list2)

#9 Kullanıcının girdiği tüm çift sayıların toplamını hesaplayan bir döngü yazın . Kullanıcı "stop" yazdığında sonlanır.

# toplam=0
# while True:
#     num=(input("Enter a number: or enter stop"))
#
#     if num.lower()=="stop":
#         break
#
#     try:
#         num = int(num)
#         if num % 2 == 0:
#             toplam += num
#     except ValueError:
#         print("Invalid input, please enter a valid number or 'stop'.")
#
# print(toplam)


#10 whileKullanıcıdan bir dizi sayı alan ve girilen en büyük sayıyı bulan bir döngü yazın . Kullanıcı "exit" yazdığında durun.

#
# enBuyuk = None
#
# while True:
#     num = input("Enter a number or type 'exit' to stop: ")
#
#     if num.lower() == 'exit':
#         break
#
#     try:
#         num = int(num)
#         if enBuyuk is None or num > enBuyuk:
#             enBuyuk = num
#     except ValueError:
#         print("Invalid input, please enter a valid number or 'exit'.")
#
# if enBuyuk is not None:
#     print("Girilen en büyük sayı:", enBuyuk)
# else:
#     print("Hiçbir sayı girilmedi.")


#11 İlk 10 asal sayıyı bulmak ve yazdırmak için bir döngü kullanın

# list=[]
# i=2
# while len(list)< 10:
#     prime= True
#
#     for j  in range(2,int(i**0.5)+1):
#
#         if i%j ==0:
#             prime=False
#             break
#     if prime:
#         list.append(i)
#     i=i+1
#
# print(list)

#11 Kullanıcıdan bir sayı isteyen ve daha sonra o sayının tüm çarpanlarını bir fordöngü kullanarak yazdıran bir program yazın.

# x=int(input("Enter a number: "))
# list=[]
#
# for i in range(1,x+1):
#     if x % i==0:
#         list.append(i)
#
# print(list)

#12 forYüksekliği 5 olan karakterlerden oluşan ters üçgen desenini oluşturmak ve yazdırmak için iç içe döngüleri kullanın *.

# high=5
# for i in range(high,0,-1):
#  print("*"*i)

#13 while 1 ile 10 arasında rastgele sayılar üreten ve sonunda 5 üreten bir döngü yazın . Üretilen her sayıyı yazdırın.

# set1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1=[]
#
# while True:
#
#     randomNumber=random.choice(set1)
#     print(randomNumber)
#     if randomNumber == 5:
#          break
#     else   :
#         list1.append(randomNumber)
#
# print(list1)


#14 Bir döngü kullanarak for, kullanıcı tarafından girilen bir dizgeden tüm yinelenen karakterleri kaldırın ve sonucu yazdırın.

# list1=list(input("Enter numbers: "))
# list2=[]
#
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#
# print(list2)


#15 for Verilen bir sayıdaki tüm basamakların çarpımını hesaplayan bir döngü yazın . Örneğin, için 123, şöyle olurdu 1 * 2 * 3 = 6.
#
# num = int(input("Enter a number: "))
# carpim = 1
# for i in str(num):
#     carpim *= int(i)
# print("Basamakların çarpımı:", carpim)


#16 Kullanıcı tarafından girilen dizeleri sürekli olarak tersine çevirmek için bir döngü kullanın while. Kullanıcı "done" girdiğinde durun.

# giris=""
# list1=[]
# list2=[]
#
# while  giris.lower()!="done":
#     giris = input("Enter something")
#     if giris.lower()!="done":
#         list1.append(giris)
#         list2=list1[::-1]
#
#     print(list2)

#17 forKullanıcının girdiği pozitif sayılardan oluşan bir listenin geometrik ortalamasını hesaplayan bir döngü oluşturun

# import math
# user_inputs = []
# for i in range(100):
#     user_input = input("Bir pozitif sayı girin (çıkmak için 'done' yazın): ")
#     if user_input.lower() == "done":
#         break
#     number = float(user_input)
#     if number > 0:
#         user_inputs.append(number)
#     else:
#         print("Lütfen pozitif bir sayı girin.")
# if len(user_inputs) > 0:
#     product = 1
#     for num in user_inputs:
#         product *= num
#     geometric_mean = math.pow(product, 1/len(user_inputs))
#     print("Geometrik Ortalama:", geometric_mean)
# else:
#     print("Geometrik ortalama hesaplamak için pozitif sayılar girilmedi.")


#18 Kullanıcıdan bir başlangıc numarası alan, 0'a kadar geri sayan ve bittiğinde "Zaman doldu!" yazan bir geri sayım sayacı yazın .

# basla = int(input("Enter a starting number:   "))
# while basla>=0:
#     print(basla)
#     basla-=1
# print("Time is up!!")


#19 forKullanıcı tarafından girilen bir dizgedeki karakter sayılarının dikey bir histogramını oluşturmak için bir döngü kullanın .
                # Her benzersiz karakter için, sayısını bir yıldız işareti satırı olarak yazdırın.

# inputStr=(input("Enter a number: "))
# char_count={}
# for i in inputStr:
#     if i in char_count:
#         char_count[i]+=1
#     else:
#         char_count[i]=1
# for i, count  in char_count.items():
#     print(i,  count)

#20 Kullanicinin girdigi bir sayinin faktoriyelini hesapla

# sayi=int(input("Faktoriyel hesaplanmasi icin bir sayi giriniz:   "))
# faktoriyel=1
# for i in range(1,sayi+1):
#     faktoriyel*=i
#
#
# print(" Girdiginiz",sayi,"sayisinin faktoriyeli=", faktoriyel)

# sayi=int(input("Enter a number: "))
#
# prime=True
#
# for i in range(2,int(sayi/2)+1):
#
#     if sayi %i ==0:
#         prime=False
#         break
#
# if prime:
#     print("The number is prime")
#
# else:
#     print("The number is not prime")

#21 Kullanicinin girdigi sayinin pozitif kac tane boleni oldugunu hesapla

# number=int(input("Enter a number: "))
# count=0
# list1=[]
#
# for i in range(1,number+1):
#     if number%i==0:
#         count=count+1
#         list1.append(i)
#
# print(f"{number} is divisible by {count} ans divisible by {(list1)}")


#22 Kullanicinin girdigi sayinin rakamlari toplamini bulan program

# number=int(input("Enter a number: "))
# sum=0
# strNumber=str(number)
# tempNumber=number
# for i in strNumber:
#     sum+=int(i)

        #2- Yol

# while tempNumber!=0:
#      x=tempNumber%10
#      sum=sum+x
#      tempNumber=tempNumber//10
#
# print(f"{number} is sum:  {sum}")

#23 girilen sayilardan en buyuk ve en kucugunu bulma
# maxNumber=0
# minNumber =1212312312312312313
# count=0
# while count<5:
#
#     number = int(input("Enter a number: "))
#     if number < minNumber:
#         minNumber=number
#         count+=1
#     if number > maxNumber:
#         maxNumber=number
#         count+=1
#
# print(f"Min Number: {minNumber}, Max Number: {maxNumber}")
#
            # 2. Yol
#
# list=[]
# for i in range(5):
#     number = int(input("Enter a number: "))
#     list.append(number)
# print(f" biggest number:: {max(list)} -> minimum number :: {min(list)}")


#24 Kullanicinin girdigi sayinin herhangibir sayinin karesi olup olmadigini kontorl edin

# sayi =int(input("Enter a number: "))
# karekok  = sayi ** 0.5
#
# if karekok == int(karekok):
#         print(f"{sayi} is squart to {karekok}")
#
# else:
#         print("degil")


#25 Kullanicin girdigi metinde kac hangi rakam kac tane geciyor bul

# metin=input("Lutfen bir metin giriniz")
# dict=dict()
#
# for char in metin:
#         if char in dict:
#                 dict[char] += 1
#
#         else:
#                 dict[char] = 1
# for char,count in dict.items():
#         print(char,count)

#26 Kullanicin girdigi metinde bulunan a harflerini A harfine cevir
# text=input("Enter a string: ")
# text2=""
# for i in text:
#         if i == "a":
#          text2+="A"
#
#         else:
#                 text2+=i
# print(text2)

#27 Ilk 10000 asal sayinin kactanesi 3 ile baslar 7 ile biter
#
# prime_list=[]
# prime_list2=[]
# prime_list.append(2)
# number=3
# while True:
#         prime=True
#
#         for i in range(2,int(number ** 0.5)+1):
#                 if number % i == 0:
#                         prime=False
#                         break
#
#         if prime:
#                 prime_list.append(number)
#                 if len(prime_list)==10000:
#                         break
#         number+=1
# for prime in prime_list:
#         strPrime=str(prime)
#         if strPrime.startswith("3") and strPrime.endswith("7"):
#                 prime_list2.append(prime)
#
# print(prime_list2)
# print(len(prime_list2))


#28 uc basamakli sayilarin kac tanesinin rakamlarinin kupunun toplami kendisine esittir?


# list=[]
# for num in range(100,1001):
#         sum = 0
#         step = 0
#         tempNum = num
#         while tempNum !=0:
#          step= tempNum   % 10
#          sum += step **3
#          tempNum = tempNum // 10
#         if sum == num:
#                 list.append(num)
# print(list)


#29 ilk 100 fibonacci sayisini ekrana yazdir

# fibonacci_list=[]
# fibonacci_list.append(0)
# fibonacci_list.append(1)
# index=2
#
# while True:
#         fibonacci_list.append(fibonacci_list[index-2]+fibonacci_list[index-1])
#         index+=1
#
#         if len(fibonacci_list)==100:
#                 break
#
# print(fibonacci_list)


#30 100 basamakli fibonacci sayisini bul


# fibonacci_list=[]
# fibonacci_list.append(0)
# fibonacci_list.append(1)
#
# for i in range(2,10001):
#
#         fibonacci_list.append(fibonacci_list[i-2]+fibonacci_list[i-1])
#
#         if len(str((fibonacci_list[i])))==1000:
#                 print(f"100 basamakli fibonacci sayisi= {fibonacci_list[i]}")
#                 print(i)
#                 break






