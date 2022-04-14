# eh1 = input("isim: ")
# eh2 = int(input("yaş: "))
# eh3 = input("egitim seviyesi: ")
# eh3 = eh3.title()

# if eh2 >= 18:
#     if (eh3 == "Lise") or (eh3 == "Üniversite"):
#         print("Ehliyet Alabilirsiniz.")
#     elif (eh3 == "Ilkokul") or (eh3 == "Ortaokul"):
#         print("Egitim seviyeniz en az lise olması gerekmektedir.")
#     else:
#         print("Lütfen geçerli bir egitim durumu giriniz.")
# else:
#     print("En az 18 yaşında olmalısınız.")

# ehdurumu = {}
# ehdurumu.update({
#             eh1 : {
#                 "yaşı": eh2,
#                 "Egitim seviyesi": eh3
#             }

# })
# ehsor = input("Kimin durumunu ögrenmek istersin: ")
# print(ehdurumu[ehsor])


# yaz1 = float(input("1.Yazılı notun: "))
# yaz2 = float(input("2.Yazılı notun: "))
# yaz3 = float(input("Sözlü notun: "))

# hesap = (yaz1 + yaz2 + yaz3)/3

# if (hesap >= 85) and (hesap <= 100):
#     print("Puanınız: 5")
# elif (hesap >= 70) and (hesap < 85):
#     print("Puanınız: 4")
# elif (hesap >= 55) and (hesap < 70):
#     print("Puanınız: 3")
# elif (hesap >= 45) and (hesap < 55):
#     if (hesap >= 50):
#         print("Puanınız: 2")
#     else:
#         print("Puanınız: 2")
#         print("Kaldın.")
# elif (hesap >= 25) and (hesap < 45):
#     print("Puanınız: 1")
#     print("Kaldın.")
# elif (hesap >= 0) and (hesap < 25):
#     print("Puanınız: 0")
#     print("Kaldın.")
# else:
#     print("Lütfen 0 ile 100 arasında not değerligi giriniz.")



import datetime
a = datetime.datetime.today()
print("Trafiğe çıkış tarihinizi lütfen alttaki gibi kodlayınız.")
Traf = input("(Gün/Ay/yıl) şeklinde yazınız: ")
Traf = Traf.split("/")
Yg = ((a.year - int(Traf[2]))*365.25)
Ag = ((a.month - int(Traf[1]))*30)
Gg = (a.day - int(Traf[0]))
b = Yg + Ag + Gg
Year = 365.25
print(f"Toplam geçen gün: {b} ")

if (b > 0) and (365.25 >= b):
    print("1. Bakım yılında")
elif (b > 365.25) and ((Year*2) >= b):
    print("2. Bakım yılında")
elif (b > (Year*2)) and ((Year*3) >= b):
    print("3. Bakım yılında")
elif (b > (Year*3)) and ((Year*4) >= b):
    print("4. Bakım yılında")
elif (b > (Year*4)) and ((Year*5) >= b):
    print("5. Bakım yılında")
elif (b > (Year*4)) and ((Year*30000) >= b):
    print("5++. Bakım yılında")
else:
    print("Lütfen geçmiş bir yıl yazınız.")





# t3 = datetime.datetime(int(Traf[2]),int(Traf[1]),int(Traf[0])) 
# islem = a - t3
# print(islem.days)


