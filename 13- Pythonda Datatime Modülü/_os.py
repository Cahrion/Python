import os
import datetime

# result = os.name

#Dizin degiştirme.
# os.chdir("C:\\") # Dizinini istedigin yere göre degiştirir.
# os.chdir("..") #C' dizininin bir üstüne geçiş yapar.
# result = os.getcwd() # Dizinini gösterir.

# Klasör oluşturma
# os.mkdir("NewDirector") # Aynı yerde dosya yapar.
# os.makedirs("New/yeniklosör") # Daha çoklu üretim yapabiliyor.
# os.rename("newdirector","YeniKlor")
# os.rmdir("YeniKlor") # İçinde bir şey yoksa siler
# os.removedirs("new/yeniklosör") # içindekiyle beraber siler.


# Listeleme

# result = os.listdir() #Klösör içindeki dosyaları listeler.
# for dosya in os.listdir():
#     if dosya.endswith(".py"):
#         print(dosya)


# result = os.stat("Dat.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # oluşturulma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) # Son degiştirme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime)   # Degiştirilme tarihi
# os.system("notepade.exe")


# path

result = os.path.abspath("_os.py") #Bütün dizini gösterir. (Kendisi dahil)
result = os.path.dirname("C:/Users/icabi/Desktop/python_temelleri/13- Pythonda Datatime Modülü/_os.py")
result = os.path.dirname(os.path.abspath("_os.py")) # Yol dizini gösterir.
result = os.path.exists("_os.py") # Konumda var mı yok mu olayını bahseder
result = os.path.isdir("_os.py") # Klösör mü başka bir şey mi diye sorar
result = os.path.isfile("_os.py") # Farklı bir klösör mü yoksa dosya mı diye sorar Farklı ise True verir.
result = os.path.join("C:\\","deneme","deneme1") #Kendiliginden anlamsız bir dizin yazar.
result = os.path.split("C:\\deneme") # Listeye çevirir.
result = os.path.splitext("_os.py") # İsmiyle dizinini ayırır.
result = result[0]
result = result[1]


print(result)