import random
a = int(random.randrange(1,100))
b = 0
Puan =  100
Hak = int(input("Kaç hakkın olsun istersin: "))
Eksilen = Puan/Hak
Hamle = Hak
while Hak > 0 :
    b = int(input("Sizce sayı kaçtır: "))
    if b > a:
        print("Aşağıda kaldı.")
        Hak -=1
        Puan -=Eksilen

    elif a == b:
        print("Bravo başardın.")
        print(f"Sayı: {a}")
        Hak -=1
        Hamle2 = Hak
        Hak = -1
    else:
        print("Yukarıda")
        Hak -=1
        Puan -=Eksilen

if Hak == 0:
    print(f"Maalesef hakkın bitti. Sayı: {a}")
elif Hak == -1:
    print(f"Oyunu {Hamle - Hamle2} hamlede kazandınız. Puanınız: {Puan}")

