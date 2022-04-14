#class

class Person:
    # pass # pass geçiş demek boş bırakma 
    # class attributes
    # constructer(yapıcı metod)
    address = "no iformation"
    def __init__(self, name, year): # Self(farklı isimlerde olabilir sadece ilk olsun) ekleme ve eklileri gösterir.

        self.name = name
        self.year = year
        print("Metod Aktif!")

    # object attributes
    # methods

# object, instance


p1 = Person(name="Patates",year= 1990)
p2 = Person(name="Yağmur", year= 2000)

#updating
p1.name = "Ahmet"
p1.address = "Giresun"
# accessing object attributes
print(f"name: {p1.name} year: {p1.year} address: {p1.address}")
print(f"name: {p2.name} year: {p2.year} address: {p2.address}")



print(p1)
print(p2)
print(type(p1))
print(type(p2))