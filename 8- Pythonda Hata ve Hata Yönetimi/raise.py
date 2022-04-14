# x = 10

# if x > 5:
#     raise Exception("x'5 den büyük değer alamaz.")

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("Parola en az 8 karakter olmalıdır.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("Parola küçük harf içermelidir.")
#     elif not re.search("[A-Z]", psw):
#         raise Exception("Parola büyük harf içermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("Parola rakam içermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("Parola alpha numeric karakter içermelidir.")
#     elif re.search(" ", psw):
#         raise Exception("Parola boşluk içermemelidir.")
#     else:
#         print("Giriş başarılı.")
# a = input("Bir parola giriniz: ")

# try:
#     check_password(a)
# except Exception as ex:
#     print(ex)
# else:
#     print("Giriş başarılı.")
# finally:
#     print("İşleminiz tamamlandı.")


class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("İsminiz fazla karakter içeriyor.. Max:10")
        else:
            self.name = name
            print(name)

try:
    p = Person("Aliiiiiiiiiiii",1998)
except Exception as ex:
    print(ex)