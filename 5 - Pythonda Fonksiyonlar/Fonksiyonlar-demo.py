# a = (input("Bir kelime yazınız: "))
# b = int(input("Kaç kez olucağını yazınız: "))

# def yazdır(neyi,kaçadet):
#     print(neyi * kaçadet)

# yazdır(("{} \n").format(a),b)


# def sınır(*args):
#     liste = []
    
#     for arg in args:
#         liste.append(arg)
    
#     return liste

# result = sınır(10,20,70,"Merhaba",905)
# print(result)



# def parto(x,y):
#     for sayi in range(x, y+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# x = int(input("Bir sayi giriniz: "))
# y = int(input("Bir sayi giriniz: ")) 


# parto(x,y)
sa = []
def Parlox(a):
    if a > 0:
        for i in range(1,a+1):
            if a % i == 0:
                sa.append(i)

    elif a == 0:
        print("0'in böleni yoktur.")
    else:
        print("Lütfen pozitif bir sayi giriniz.")



a = int(input("Bir sayi giriniz: "))

Parlox(a)
print(sa)