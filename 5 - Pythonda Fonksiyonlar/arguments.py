# def changeName(n):
#     n = "ada"

# name = "Yigit"
# changeName(name)
# print(name)

# def change(n):
#     n[0] = "istanbul" 

# sehirler = ["ankara","izmir"]
# n = sehirler[:] # slicing

# n[0] = " istanbul"
# print(sehirler)
# print(n)


# def add(*paramsss):
    # return sum((paramsss))  
# Params kısa yoldan matematik işlemleri için bir alt yapı oluşturur ve bu şekilde komutu kullanarak istek yönünde işlem cöplügünü temizler.
# veya
    # sum = 0
    # for n in params:
    #     sum += n

    # return sum


# print(add(10,20))
# print(add(10,20,30,50,70,80,90,40,60,120,150))

def User(**num):
    for key,value in num.items():
        print(f"{key}: {value}")

User(name= "Çınar", age = 2, city="istanbul")
User(name= "Ada", age = 12, city="kocaeli",phone = 123131321)
User(name= "Yigit", age = 14, city="Ankara",phone = 544564, email = "Email@gmail.com")

# tuple listesi için (*) tek yıldız.
# Dictinery listesi için (**) iki yıldız.

def myfunc(a, b, *args, **dic):
    print(a)
    print(b)
    print(args)
    print(dic)

myfunc(10, 20,10,20,30,40,50,Name= "ali",patato= "yes" )