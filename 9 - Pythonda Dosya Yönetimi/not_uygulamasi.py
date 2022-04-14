def Notları_Oku():
    with open("Notlar.txt","r+", encoding="utf-8") as file:
        print(file.read())


b = True
while b:
    a = int(input("1- Notları Oku:\n2- Not Gir:\n3- Notları Kayıt Et\n4- Çıkış\n"))

    if a == 1:
        Notları_Oku()
        break
        
    elif a == 2:
        with open("Notlar.txt","a", encoding="utf-8") as file:
            isim = input("İsim: ")
            belge = "0"
            Not1 = float(input("1.Notu: "))
            Not2 = float(input("2.Notu: "))
            Not3 = float(input("3.Notu: "))
            ort = (Not1 + Not2 + Not3)/3
            if (ort >= 0 ) and (ort <= 100):
                if (ort < 85) and (ort > 0):
                    if ort < 70:
                        if ort < 50:
                            belge = "Belge alamadı."
                        else:
                            belge = "Ucundan geçti belgesi."
                    else:
                        belge = "Teşekkür belgesi"    
                elif (ort >= 85) and (ort <= 100):
                    belge = "Taktir belgesi"
                # file.write(f"\n\n{isim}\nBirinci notu: {Not1}\nİkinci notu: {Not2}\nÜçüncü notu: {Not3}\nOrtalaması: {ort}\nAlacağı belge: {belge}")
                file.write(f"{isim} : {Not1} , {Not2} , {Not3} \nOrtalaması ve belgesi: {ort},{belge}\n")
                print("Kayıt başarılı.")
            else:
                print(f"Lütfen düzgün sayılar giriniz ortalama: {ort} olamaz.")


    elif a == 3:
        pass
    elif a == 4:
        print("Çıkış yapıldı.")
        break
    else:
        print("Lütfen Belirtilen Sayılardan birini seçiniz.")


