# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("Fonksiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("hello", name)

# def sayGreeting():
#     print("Greeting")

# sayHello = my_decorator(sayHello)
# sayGreeting = my_decorator(sayGreeting)
# sayHello("ali")
# sayGreeting()

import time
import math

def zaman(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        stop = time.time()
        print(f"fonksiyon {str(stop - start)} saniye'de yapıldı.")
    return inner

@zaman
def usalma(b,c):
    print(math.pow(b,c))
@zaman
def faktoriyel(num):
    print(math.factorial(num))
@zaman
def toplama(a,b):
    print(a+b)

a = input("(usalma,faktoriyel,toplama) Ne yapmak isterdiniz: ")
if a == "usalma":
    b = int(input("Kaç ile: "))
    c = int(input("Kaç: "))
    usalma(b,c)
elif a == "faktoriyel":
    d = int(input("Kaçın: "))
    faktoriyel(d)
elif a == "toplama":
    b = int(input("Kaç ile: "))
    c = int(input("Kaç: "))
    toplama(b,c)
else:
    print("Belirtilen uygulamalardan birini seçiniz.")
