
a = float(input("Bir sayı değeri giriniz: "))

print(f" 100 ile 0 arasında : {(0 < a) and (a < 100)}")

b = int(input("Bir sayı değeri giriniz: "))
print(f"Sayınız çift ve pozitif : {(b > 0) and (b % 2 == 0)}")

email = "doctor@gmail.com"
parola = "123456"

c = input("Email: ")
d = input("Parola: ")

print(f" Giriş bilgileriniz : {(c == email) and (d == parola)}")

e = input("[1]Bir sayı giriniz: ")
f = input("[2]Bir sayı daha giriniz: ")
g = input("[3]Bir sayı daha giriniz: ")

print(f"İlk sayı: {e} ikinci sayı: {f} üçüncü sayı: {g}")
print(f"İlk girilen sayı ikinciden büyüktür : {e > f}")
print(f"İlk girilen sayı üçüncüden büyüktür : {e > g}")
print(f"İkinci girilen sayı üçüncüden büyüktür : {f > g}")
print(f"Birbirine eşit var mı: {(e == f) or (e == g) or (f == g) }")
h = float(input("Vize 1. sınav notu: "))
ı = float(input("Vize 2. sınav notu: "))
j = float(input("Final sınav notu: "))

k = ((h + ı)/2 *60 + j*40)/100

print(f"Puanı: {k}" )
print(f"Geçme durumu: {(k >= 50 and j >= 50) or ((j) > 70) }")

sa = {}
ad = (input("Adı: "))
kilo = float(input("Kilosu: "))
boy = float(input("boyu: "))
index = (kilo) / (boy**2)

sa.update({
            ad : {
                "Kilo" : kilo,
                "Boy" : boy,
                "index" : int(index)
 


            }


})


print(f"index: {index}")
print(f"Zayıf mısın:{index <= 18.4 and index > 0}")
print(f"Normal misin: {index <= 24.9 and index > 18.4}")
print(f"Fazla kilolu musun: {index <= 29.9 and index > 24.9}")
print(f"Obez misin: {index <= 34.9 and index > 29.9}")

way = input("Kimin Kilo indexsini ögrenmek istersiniz ? ")

print(sa[way])






