# #class

# class Person:
#     # pass # pass geçiş demek boş bırakma 
#     # class attributes
#     # constructer(yapıcı metod)
#     address = "no iformation"
#     def __init__(self, name, year): # Self(farklı isimlerde olabilir sadece ilk olsun) ekleme ve eklileri gösterir.

#         self.name = name
#         self.year = year
#         print("Metod Aktif!")


#     # methods
#     def intro(self):
#         print("Hello There I am " + self.name)

#     def calculateAge(self):
#         return 2019 - self.year


# # object, instance


# p1 = Person(name="Patates",year= 1990)
# p2 = Person(name="Yağmur", year= 2000)

# #updating
# p1.name = "Ahmet"
# p1.address = "Giresun"
# # accessing object attributes
# print(f"name: {p1.name} year: {p1.year} address: {p1.address}")
# print(f"name: {p2.name} year: {p2.year} address: {p2.address}")
# p1.intro()

# print(f"adım: {p1.name} ve yaşım: {p1.calculateAge()}")
# print(f"adım: {p2.name} ve yaşım: {p2.calculateAge()}")

yaricap = int(input("Yariçap: "))
class Circle:

    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    #methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
p1 = Circle(yaricap)
print(f"Alan: {p1.alan_hesapla()}")
print(f"Cevre: {p1.cevre_hesapla()}")