import requests
import json

#Matematiksel ve tek veri kullanım olarak benim yaptıgım fikir:

# result = requests.get("https://api.exchangeratesapi.io/latest")
# result = result.text
# result = json.loads(result)
# result = result["rates"]

# def Hesapla(a,b):
#     son = float(result[b]/result[a])
#     son2 = son*c
#     return f"1 {a} değeri: {son}{b} \n{c} {a} değeri: {son2}{b}"
# a = input("Bozulan döviz türü: ")
# b = input("Alınan döviz türü: ")
# c = float(input(f"Ne kadar {a} bozdurmak istersiniz: "))

# print(Hesapla(a,b))

# Hocanın hileli url yaparak her url'yi açtıgımız fikir: :)

api_url = ("https://api.exchangeratesapi.io/latest?base=")
a = input("Bozulan döviz türü: ")
b = input("Alınan döviz türü: ")
c = float(input(f"Ne kadar {a} bozdurmak istersiniz: "))

result = requests.get(api_url+a)
result = result.text
result = json.loads(result)
result = result["rates"]

print(f"1 {a} değeri: {result[b]} {b} \n{c} {a} değeri: {result[b]*c} {b}")