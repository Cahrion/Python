x, y, z = 2, 5, 10

numbers = 1, 5, 7, 10, 6

w = input("Bir sayı giriniz: ")
w1 = input("Bir sayı daha giriniz: ")
w = int(w)
w1 = int(w1)
print((w * w1) - (x + y + z) )

print(y // x)

print((x + y + z) % 3) # Kalan gösterilir.

print(y**x)

x, *y, z = numbers
print(z**3)
print(y[0]+ y[1]+ y[2])