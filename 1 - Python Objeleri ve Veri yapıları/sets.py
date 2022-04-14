fruits = { "orange","apple", "banane" }

# print(fruits[0]) indekslenemez


# for x in fruits:
#     print(x)          #Daha erken 

fruits.add("cherry")
fruits.update(["mango","grape","apple" ])  # bir elemandan bir tane olur.

print(fruits)

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList)) # Tekrarlı listeyi siliyor.

fruits.remove("mango")
fruits.pop()
fruits.discard("apple")

fruits.clear()

print(fruits)