
# open()

# "w": (Write) yazma modu. 
#       ** Dosyayı konumda oluşturur.
#       ** Dosya içerigini siler ve yeniden ekleme yapar

# file = open("newfile.txt","w")
# file.close()

# file = open("C:/users/icabi/Desktop/newfile.txt", "w")
# print(file)

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("İcabi Kırgız.")
# file.close


# "a": (append) ekleme. Dosya konumda yoksa oluşturur.

# file = open("newfile.txt","a",encoding="utf-8")
# file.write(" İcabi Kırgız ".center(100,"*"))
# file.close()


# "x": (Create) oluşturma. Dosya zaten varsa hata verir.

file = open("newfile2.txt","x",encoding="utf-8")
file.close()




# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.

