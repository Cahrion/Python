# Identity Operator: is

# x = y = [1, 2, 3]
# z = [1, 2, 3]


# print(x==y)
# print(x==z) # Değer karşılaştırmasını yapar
# print(x is y)
# print(x is z) # objelerin karşılaşmasını yapar.

x = [1, 2, 3]
y = [2, 4]

del x[2]
y[1] = 1
y.reverse()


print(x==y)
print(x is y) #Eğer x = y gibi bir değer atansaydı eşit olurdu.
print(x is not y)

# Membership Operator: in

x = ["Apple", "Banana"]
print("Banana" in x)

name = "Çınar"
print("a" in name)
print("a" not in name)


