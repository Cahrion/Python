def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1, f2, f3, f4, islem_adi,a,b):
    if islem_adi == "toplama":
        print(f1(a,b))
    elif islem_adi == "cikarma":
        print(f2(a,b))
    elif islem_adi == "carpma":
        print(f3(a,b))
    elif islem_adi == "bolme":
        print(f4(a,b))
    else:
         print("Geçersiz işlem...")

x = input("Ne yapmak istersiniz: ")
a = int(input("Kaç ile: "))
b = int(input("Kaçı: "))

islem(toplama, cikarma, carpma, bolme, x,a,b)   
# iç parametre kullanma olayı eğer değerlik aktarıldıysa olabilen bir komuttur.

