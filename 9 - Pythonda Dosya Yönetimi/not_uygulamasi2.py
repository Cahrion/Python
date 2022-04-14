def not_gir():
    ad = input("Ögrencinin adı: ")
    Soy = input("Ögrencinin soyadı: ")
    not1 = input("1.Notu: ")
    not2 = input("2.Notu: ")
    not3 = input("3.Notu: ")
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(f"{ad} {Soy}:{not1},{not2},{not3}\n")

def ortalamalari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))


def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1]
    notlar = notlar.split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ort = (not1+not2+not3)/3

    if 100 >= ort and 90 <= ort:
        Belge = "AA"
    elif 90 > ort and 85 <= ort:
        Belge = "BA"
    elif 85 > ort and 80 <= ort:
        Belge = "BB"
    elif 80 > ort and 75 <= ort:
        Belge = "CB"
    elif 75 > ort and 70 <= ort:
        Belge = "CC"
    elif 70 > ort and 65 <= ort:
        Belge = "DC"
    elif 65 > ort and 60 <= ort:
        Belge = "DD"
    elif 59 > ort and 50 <= ort:
        Belge = "FD"
    elif 50 > ort and 0 < ort:
        Belge = "FF"
    else:
        print("Lütfen düzgün bir sayı ortalaması giriniz.")

    return (f"{ogrenciAdi}: {Belge} \n")


def notlari_kayitet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))
        
        with open ("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


b = True
while b:
    a = int(input("1- Notları Oku:\n2- Not Gir:\n3- Notları Kayıt Et\n4- Çıkış\n"))

    if a == 1:
        ortalamalari_oku()
    elif a == 2:
        not_gir()
    elif a == 3:
        notlari_kayitet()
    elif a == 4:
        print("Çıkış yapıldı.")
        break
    else:
        print("Lütfen Belirtilen Sayılardan birini seçiniz.")


