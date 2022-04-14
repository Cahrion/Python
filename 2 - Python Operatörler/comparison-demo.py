a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz: "))

c = (a > b)

print("Birinci sayı büyükse true yazacaktır." )
print(c)

print("")
print("Vize Uygulaması")
print("")

vize = float(input("1.Vize notu: "))
vize2 = float(input("2.Vize notu: "))
final = float(input("Final notu: "))

ort = (((vize + vize2)*30 + final*40)/100)
ort2 = (50 <= ort)

print(f" Bölümü geçti : {ort2}, Puanı: {ort}")

print("")
print("Tek mi çift mi uygulaması")
print("")


tc = int(input("Bir sayı giriniz: "))
tc2 =  ((tc % 2) == 0)
print(f"Verdiginiz sayı çift: {tc2}")

print("")
print("Negatif mi Pozitif mi ?")
print("")

np = int(input("Bir reel sayı giriniz: "))
print(f"Yazdıgınız sayı pozitiftir: {np > 0}")


print("")
print("Giriş !")
print("")


email = "email@sadikturan.com"
parola = "abc123"

e = (input("Email adresiniz: "))
p = (input("Parolanız: "))
e1 = int((e == email))
p2 = int((p == parola))

print(f"Hesabınız Doğru: {(e1+p2) >= 2}")




