
#  """
#     ogrenciler = {
#         "120": {
#             "ad": "Ali",
#             "soyad": "Yılmaz",
#             "telefon": "532 000 00 01"
#         },
#         "125":{
#             "ad": "Can",
#             "soyad": "Korkmaz",
#             "telefon": "532 000 00 02"
#         },
#         "128":{
#             "ad": "Volkan",
#             "soyad": "Yükselen",
#             "telefon": "532 000 00 03"
#         },

#                 }
# """

# a1 = input("Ögrencinin Numarası : ")
# a2 = input("Ögrencinin Adı : ")
# a3 = input("Ögrencinin Soyadı : ")
# a4 = input("Ögrencinin Telefonu : ")
# a5 = input("Ögrencinin Numarası : ")
# a6 = input("Ögrencinin Adı : ")
# a7 = input("Ögrencinin Soyadı : ")
# a8 = input("Ögrencinin Telefonu : ")
# a9 = input("Ögrencinin Numarası : ")
# a10 = input("Ögrencinin Adı : ")
# a11 = input("Ögrencinin Soyadı : ")
# a12 = input("Ögrencinin Telefonu : ")

# user = { a1 : {
#         "ad": a2,
#         "soyad": a3,
#         "telefon": a4  
# },
#                 a5 : {
#         "ad": a6,
#         "soyad": a7,
#         "telefon": a8  
# },
#                 a9 : {
#         "ad": a10,
#         "soyad": a11,
#         "telefon": a12  
# }
# }
user = {}
a1 = input("Ögrencinin Numarası : ")
a2 = input("Ögrencinin Adı : ")
a3 = input("Ögrencinin Soyadı : ")
a4 = input("Ögrencinin Telefonu : ")

user.update({
    a1: {
        "adı" : a2,
        "Soyadı" : a3,
        "Telefonu" : a4   
        }
}
)

a1 = input("Ögrencinin Numarası : ")
a2 = input("Ögrencinin Adı : ")
a3 = input("Ögrencinin Soyadı : ")
a4 = input("Ögrencinin Telefonu : ")

user.update({
    a1: {
        "adı" : a2,
        "Soyadı" : a3,
        "Telefonu" : a4   
        }
}
)

a1 = input("Ögrencinin Numarası : ")
a2 = input("Ögrencinin Adı : ")
a3 = input("Ögrencinin Soyadı : ")
a4 = input("Ögrencinin Telefonu : ")

user.update({
    a1: {
        "adı" : a2,
        "Soyadı" : a3,
        "Telefonu" : a4   
        }
}
)


print("")
print("-----")
print("Bilgiler Kaydedildi.")
print("-----")
print("")
B1 = input("Bilgi almak istediğiniz ögrenciyi numarasını giriniz : ")
ogrenci = user[B1]


print("Aradığınız {} nolu ögrencinin adı: {} soyadı: {} telefonu: {} ".format(B1,ogrenci["adı"],ogrenci["Soyadı"],ogrenci["Telefonu"] ))


