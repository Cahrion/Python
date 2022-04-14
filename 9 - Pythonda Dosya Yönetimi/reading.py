# try:
#     file = open("newfile.txt","r") #hiç bir şey konmazsa "r" parametresi kullanılır.
#     print(file)
# except Exception:
#     print("Dosya okuma hatası.")
# finally:
#     print("işlem tamamlandı.")
#     file.close()

file = open("newfile.txt","r", encoding = "utf-8")

# for döngüsü
# for a in file:
#     print(a, end="")

#*************** read() fonksiyonu

# print("İçerik 1")
# print(file.read())

# file = open("newfile.txt","r", encoding = "utf-8")
# print("İçerik 2")
# print(file.read())

# content = file.read(5) #1byte = 1 Karakter.
# print(content)

# file.close()


# ******** readline() fonksiyonu
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline()) # end'siz kullanımları eğer okunacak bir şey yoksa okumaya boşluk ekler.
# print(file.readline())

# ******** readlines() fonksiyonu

print(file.readlines()) # bilgiler bir liste içinde gelir ve her "ENTER" içerigi "\n" gibi gösterir.
# Eğer [1,2 veya 3] kullanırsa o listedekini gösterir .

file.close()