names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

names.append("Cenk")

names.insert(0, "Sena")
# names.remove("Deniz")
vat = names.index("Deniz")
print(vat)

vat2 = "Ali" in names
print(vat2)

names.reverse()
years.reverse()

names.sort()
years.sort()

str = "Chevrolet,Dacia".split(",")
print(str)


print(min(years))
print(max(years))

print(years.count(1998))
years.clear()

print(names)
print(years)

van1 = input("En sevidigin marka: ")
van2 = input("En sevdigin 2. marka: ")
van3 = input("En sevdigin 3. marka: ")

list = [van1, van2, van3]

van5 = input("En sevdigin markaları ögrenmek istermisin? ")
van6 = van5.count("rusyanın fethi")

van6 = "evt"
print(f"okeyy cevabın {van6} ise;")

print(list)