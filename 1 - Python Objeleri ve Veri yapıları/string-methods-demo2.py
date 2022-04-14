website = " DedeminSonyolcusu.net "
Burası = "Neresi burası begardaşım"
Suslan = "15462345231"

result = website.title()
result = website.count("e")
print(result)

result = Burası.split()
print(result)

result = Suslan.center(50, "!")
print(result)
result = Suslan.startswith("154")
print(result)
result = Burası.endswith("şım")
print(result)
result = website.isalpha()
print(result)
result = Suslan.isdigit()
print(result)
patates = "Neredesin Yar gözlüm {}".format("154")
print(patates)

deden = Burası.count("i")
print(deden)

deliyar = input("Ne yaptın ? ")
print("demek böyle yaptın :", deliyar)
pattos = input("bir sayı tut ")
pattos = int(pattos)*5
print("Bu sayıyı 5 ile çarpıyorum ve sonuç : ", pattos)
Salatalık = input("Yarın Boş musun ? ")
print(" O zaman dans :) ")