SadikTuran456= {
    "ad" : "Sadık Turan",
    "HesapNo": "123456",
    "Bakiye": 3000,
    "ekHesap": 2000


}


AliTuran123= {
    "ad" : "Ali Turan",
    "HesapNo": "12345678123",
    "Bakiye": 2000,
    "ekHesap": 1000


}

İcoYan= {
    "ad" : "İcabi Kırgız",
    "HesapNo": "159445678123",
    "Bakiye": 1000,
    "ekHesap": 537


}

def paraCek(hesap,miktar):
    What = input("Ne yapmak istersiniz? (Para,Bakiye,Yatır) ")
    if "Para" == What:
        miktar = int(input("Kaç para çekmek istersiniz: "))
        a = int(hesap["Bakiye"])
        b = int(hesap["ekHesap"])
        if miktar > a:
            f = input("Bakiyeniz yetersiz. Ek hesap'da kullanılsın mı? ")
            if ("evet" == f) or ("kullan" == f) or ("e" == f):
                if miktar > a+b:
                    print("Paranız yetersiz.")
                    paraCek(Xlarc,0)
                elif a+b >= miktar:
                    print("İşleminiz başarıyla sonuçlandı.") 
                    Newmany = (a+b) - miktar
                    hesap["Bakiye"] = 0
                    hesap["ekHesap"] = Newmany
                    


                    print("Son bilgileriniz.")
                    for w in hesap.items():
                        print(w)

            elif ("hayır" == f) or ("kullanma" == f) or ("h" == f):
                paraCek(Xlarc,0)
            else:
                print("Hata!")
                print("Eğer kullanmak istiyorsanız: 'evet, kullan veya e' yazınız. ")
                print("Eğer kullanmak istemiyorsanız: 'hayır, kullanma veya h' yazınız. ")
                paraCek(Xlarc,0)
        elif a >= miktar:
            NewsMany = a - miktar
            print("İşleminiz başarıyla sonuçlandı.") 
            hesap["Bakiye"] = NewsMany
            
            print("Son bilgileriniz.")
            for s in hesap.items():
                print(s)
    elif What == "Bakiye":
        for Pak in hesap.items():
            print(Pak)
    elif What == "Yatır":
        Yat = int(input("Kaç para yatırmak istersiniz: "))
        if 2000 > hesap["ekHesap"]: # Ek hesap limiti 2000Tl'dir.
            SonYat = 2000 - hesap["ekHesap"]
            if SonYat > Yat:
                hesap["ekHesap"] +=Yat
                print("Hesabınıza para yatmıştır.")
                print("Son bilgileriniz.")
                for w in hesap.items():
                    print(w)
            elif Yat > SonYat:
                EkYat = Yat - SonYat
                hesap["ekHesap"] +=SonYat
                hesap["Bakiye"] +=EkYat
                print("Hesabınıza para yatmıştır.")
                print("Son bilgileriniz.")
                for w in hesap.items():
                    print(w)
        else:
            hesap["Bakiye"] +=Yat
            print("Hesabınıza para yatmıştır.")
            print("Son bilgileriniz.")
            for w in hesap.items():
                print(w)



Xlarc = eval(input("Hesap no: "))


paraCek(Xlarc,0)



# Global yazmaya gerek yok :)