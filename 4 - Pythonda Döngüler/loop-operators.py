# range

# for item in range(10,100,2): #kendi bir liste kurar ve onu ayarlar (nerden başlıyacagı,Nerde bitecegi,kaçar kaçar)
#     print(item)

# print(list(range(5,100,10)))


# enumerate

# text = "Hello there"

# for index,letter in enumerate(text):
#     print(f"index: {index}, letter: {letter}")

# enumerate = İndex numaralarını ek olarak kendisi bulan ve bunları ek olarak yazabilme olanagı sağlayan komut

# zip

list1 = [1,2,3,4,5]

list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

w = zip(list1, list2, list3)

# for item in w:
#     print(item)


for a,b,c in w:
    print(f"Sayi: {a}, Harf: {b}, Yüzdelik: {c}")

