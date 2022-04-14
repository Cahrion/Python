liste = ["1","2","5a","10b","abc","10","50"]

# def check(psw):
#     import re
#     if not re.search("[a-z]",psw):
#         print(psw)


# for a in liste:
#     check(a)


# a = True
# def checking(psw):
#     import re
#     if re.search("[0-9]", psw):
#         print("Okey")
#     else:
#         print("Hatalı mesaj girdiniz.")
# while a:
#     w = input("Sayı giriniz.")      
#     if not w == "q":
#         try:
#             checking(w)
#         except Exception as ex:
#             print(ex)
#     else:
#         print("Okey")
#         break

# def  parola(parol):
#     import re
#     if re.search("[Ğğıİüçşö]",parol):
#         raise Exception("Türkçe karakter kullanmayınız.")
#     else: 
#         print("Kayıt başarılı.")
# a = input("Parolanızı giriniz: ")

# try:
#     parola(a)
# except Exception as ex:
#     print(ex)

a = input("Sayı giriniz: ")

def fact(factor):
    b = 1
    if factor < 0:
        raise ValueError("Negatif değer")
    elif not factor < 0:
        while not factor == 0:
            b = b * factor
            factor -=1

    else:
        print(b)
try:
    result = int(a)
    fact(result)
except:
    print("Lütfen rakamlardan oluşan bir sayi kümesi yazınız.")


 





