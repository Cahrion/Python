
# a = float(input("Bir sayi giriniz: "))
# if (100 > a) and (a > 0):
#     print("İfadeniz 100 ile 0 arasındadır.")
# else:
#     print("İfadeniz 100 ile 0 arasında değildir.")



# b = int(input("Bir sayi giriniz: "))

# if b > 0:
#     if b % 2 == 0:
#         print("Pozitif bir çift sayıdır.")
#     else:
#         print("Pozitif bir tek sayıdır.")
# else:
#     if b % 2 == 0:
#         print("Negatif bir çift sayıdır.")
#     else: 
#         print("Negatif bir tek sayıdır.")

# email = "Cahrion@gmail.com"
# parola = "123456789"

# a = input("Email adresinizi giriniz: ")
# b = input("Şifrenizi giriniz: ")

# if a == "Cahrion@gmail.com" :
#     if b == parola:
#         print("Giriş başarılı.")
#     else:
#         print("Şifreniz hatalı")
# else:
#     if b == parola:
#         print("Email adresiniz hatalı.")
#     else:
#         print("Giriş bilgileriniz hatalı.")            


# print("3 Adet sayı giriniz: ")

# S1 = int(input("[A]Birinci sayı: "))
# S2 = int(input("[B]İkinci sayı: "))
# S3 = int(input("[C]Üçüncü sayı: "))

# if S1 > S2:
#     if S1 > S3:
#         if S3 > S2:
#             print("[A] sayısı en büyüktür.")
#             print("[C] sayısı ortanca.")
#             print("[B] sayısı en küçüktür.") 
#         else:
#             print("[A] sayısı en büyüktür.")
#             print("[B] sayısı ortanca.")
#             print("[C] sayısı en küçüktür.")   
#     else:
#         print("[C] sayısı en büyüktür.")
#         print("[A] sayısı ortanca.")
#         print("[B] sayısı en küçüktür.")      
# else:
#     if S2 > S3:
#         if S3 > S1:
#             print("[B] sayısı en büyüktür.")
#             print("[C] sayısı ortanca.")
#             print("[A] sayısı en küçüktür.") 
#         else:
#             print("[B] sayısı en büyüktür.")
#             print("[A] sayısı ortanca.")
#             print("[C] sayısı en küçüktür.")   
#     else:
#         print("[C] sayısı en büyüktür.")
#         print("[B] sayısı ortanca.")
#         print("[A] sayısı en küçüktür.")          


# Viz1 = int(input("1.Vize sonucun: "))
# Viz2 = int(input("2.Vize sonucun: "))
# Final = int(input("Final:  "))
# Toplam = ((Viz1 + Viz2)*30 + Final*40)/100

# if (Toplam >= 50):
#     if (Final >= 50):
#         print(f"Puanı: {Toplam}, Ortalamandan dolayı geçtin.")
#     else: 
#         print(f"Puanı: {Toplam}, Final notundan dolayı kaldın.")
# else:
#     if Final >= 70:
#         print(f"Puanın: {Toplam}, Final puanından dolayı geçtin.")
#     else:       
#         print(f"Puanı: {Toplam}, Ortalamandan dolayı kaldın.")



# a = input("Adın: ")
# b = float(input("Kilon: "))
# c = float(input("Boyun: "))

# index = b/(c**2)
# Kilom = {}
# Kilom.update({a : {
#         "Adın" : a,
#         "Kilon" : b,
#         "Boyun" : c,
#         "index" : index

# }}) 
# if index > 0:
#     if index >= 18.5:
#         if index >= 25.0:
#             if (index >= 30.0):
#                 if (index >= 35):
#                     print(f"Şişman+(Obez2), Kilo indeksi: {index}")
#                 else:
#                     print(f"Şişman(Obez), Kilo indeksi: {index}")
#             else:
#                 print(f"Fazla Kilolu, Kilo indeksi: {index}")
#         else:
#             print(f"Normal, Kilo indeksi: {index}")
#     else:
#         print(f"Zayıf, Kilo indeksi: {index}")       
# else:
#     print("Lütfen doğru sayılar giriniz.")

# Kilom2 = input("Kimin kilosunu ögrenmek istersiniz: ")
# print(Kilom[Kilom2])

print("Burada 'if','elif','else' komutlarıyla önceki uygulamaları yeniden yaptık:")
print("Sayının 0-100 arasında olması; ")
print("Sayının Çift yada pozitif olması; ")
print("Giriş plartformu; ")
print("Büyüklük küçüklük sıralaması; ")
print("Puan hesaplama; ")
print("Kilo index'si;")

