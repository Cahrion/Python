# def usalma(number):


#     def inner(power):
#         return number ** power

#     return inner

# a = int(input("Hangi sayının üstünü almak istersiniz: "))
# b = int(input("Kaç 'üssü: "))

# two = usalma(a)(b)
# print(two)
# three = usalma(3)


# def yetki_sorgula(page):
#     def inner(role):
#         if role == "Admin":
#             return f"{role} rolünün {page} sayfasına ulaşabilme hakkı vardır."
#         else:
#             return f"{role} rolünün {page} sayfasına ulaşabilme hakkı yoktur."
#     return inner

# admin_user = yetki_sorgula("Admin Page")
# print(admin_user("User"))

def islem(islem_adi):
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *=i
        return carpim
    if islem_adi == "toplama":
        return toplama
    elif islem_adi == "carpma":
        return carpma


print(islem("toplama")(1,2))
print(islem("carpma")(1,9,5,7))




