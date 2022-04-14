# x = "global x"

# def function():
#     x = "local x"
#     print(x)
# function() # Mantık İlk koyulan global ve geçerli olur lakin bizim def ile gömdügümüz yazılım local olur ve çalışmaz.

# print(x)




# name = "Çınar"

# def changeName(new_name):
#     name = new_name
#     print(name)

# a = input("Eski isminizi girin: ")
# b = input("Birdaha eski isminizi girin: ")
# c = input("Yeni isim girin: ")

# if (a==b) and not (a==c) and (name == a):
#     changeName(c) 
# elif not (a == b):
#     print("Girdiginiz isimler uyuşmuyor.")
# elif (name == c):
#     print("Eski şifrenizi tekrar yazamazsınız.")
# elif not (name==a) or not (name==b):
#     print("Eski isminizi lütfen doğru giriniz.")



# name = "global string"

# def greeting():
#     # name= "Çınar"
    
#     def hello():
#         # name = "Ada"
#         print("Hello" + name)

#     hello()
# greeting()
# Gömülü fonksiyonlar dış global degişkeni etkilemez.



x = 50
def test():
    global x #bu sayede dış ortamıda etkiler.
    print(f"x: {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)

