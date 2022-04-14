
sayi = int(input("Sayı: "))
asalmi = True
if sayi == 1:
    asalmi = False

for i in range(2, sayi):
    if sayi % i == 0:
        asalmi = False
        break

if asalmi:
    print(f"{sayi} Sayisi asal bir sayıdır.")
else:
    print(f"{sayi} Sayisi asal degildir.")