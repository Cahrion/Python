# a = input("İsminizi giriniz: ")
# def sayHello(name = "user"):
#     return (f"Hello {name}")

# msg = sayHello(a)

# print(msg)


def total(num1,num2):
    return num1 + num2
result = total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2020 - dogumYili

ageCinar = yasHesapla(2017)
ageSena = yasHesapla(2010)
ageAda= yasHesapla(2011)

print(ageCinar)
print(ageSena)


def Emekliligekacyilkaldi(dogumYili, isim):
    """
    DOCSTRING: Doğum yiliniza göre emekliliğinize kac yil kaldi.
    INPUT: Doğum yili
    OUTPUT: Hesaplanan yil bilgisi
    """
    yas = yasHesapla(dogumYili)
    Emeklilik = 65 - yas

    if Emeklilik > 0:
        print(f"emekliliğinize {Emeklilik} yıl kaldı.")
    else:
        print(f"Zaten emeklisiniz. Emekliliginizden {yas - 65}'yıl geçmiş")

Emekliligekacyilkaldi(1950, "icabi")


