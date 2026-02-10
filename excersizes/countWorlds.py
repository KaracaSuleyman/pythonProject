from collections import Counter
import random

text= """Süleyman, şimdi çok kritik bir aşamadasın ve doğru hazırlık seni bir anda tester’den developer’a geçiş yapan adam konumuna sokabilir.
Zivid seni zaten potansiyel görüyor, ama bu mülakatta Python + teknik düşünme + problem çözme tarafını görmek isteyecekler. Ben sana burada gerçekçi, Norveç şirket kültürüne uygun, tester geçmişine göre uyarlanmış ve Python ağırlıklı bir soru seti çıkarıyorum.
Bu listeyi çalışırsan mülakatta hiçbir şey seni şaşırtmaz."""


print(len(text.split())-2)



str='Bismillahirrahmanirrahim'
char_counter=Counter(str)
print(char_counter)
for i, char in char_counter.items():
    if char> 1:
        print(f'{i} : {char}' ' times' )



#delete dublicate in the list

my_list=[1,2,3,4,5,1,2,3]

same_list = set()
different_list = set()
for i in my_list:
    if i in same_list:
        different_list.add(i)
    else:         same_list.add(i)

print(same_list)
no_repeat=same_list-different_list
print(no_repeat)

#Bir string’i ters çeviren fonksiyon yaz.

str1='Hello World'
def reverse_string(reverse):
    return reverse[::-1]
print(reverse_string(str1))




