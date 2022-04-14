numbers = [1,2,3,4,5]

for num in numbers:         # hepsini 'num'a atar ve yazdırır.
    print(num)


names = ["Çınar","Sadık","Sena"]


for name in names:
    print(f"My name is {name}")

name = "Sadık Turan" # Str'lar her biri bir string ifade gibi alınıp tek olarak yazılır.

for n in name:
    print(n)


tuple = [(1,2),(1,3),(3,5),(5,7)]
for a,b in tuple:
    print(a,b)

d = {"k1": 1, "k2":2, "k3":3}


for key,value in d.items(): # Mantık : "," eki getirildigininde iç listenin bölümünde hareket etme ve o seçimi yapma denilebiliri
    print(key,value)




# S1 = {}

# name = [(1,2),(4,3),(3,5),(5,7)]

# for ilk,son in name:
#     S1.update({ilk: {
#             "Birinci" : ilk,
#             "İkinci" : son

#     }})
# print(S1)


# a = int(input("Hangi sayının son halini görmek istersiniz: "))
# print(S1[a])