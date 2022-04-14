# 1 - 100 e kadar sayılar;

# x = 0
# while x <= 100:
#     if x % 2==1:
#         print(f"Sayı tek sayıdır: {x}")
#     else:
#         print(f"Sayı çift sayıdır: {x}")
#     x += 1

name = "" #false

while not name.strip():
    name = input("İsminizi giriniz: ")


print(f"Merhaba, {name}")