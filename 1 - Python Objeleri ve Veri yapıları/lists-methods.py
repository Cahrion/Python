numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]


val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers.append(49)    #en sona ekler
numbers.insert(3, 78) #ilk seçili yere onu ekler

# numbers.pop() #  en sonu siler
# numbers.pop(0) # sıralamya göre olan yeri siler

# numbers.remove(49) # Sıralı degilde seçiliyi siler

numbers.sort()  # Numaraları sayılarına göre sıralar
letters.sort()  # Kelimeleri Alfabetik sıraya göre sıralar.

numbers.reverse() #Ters Çevirir. :)
letters.reverse() #Ters.

print(len(letters))
print(len(numbers))

print(numbers.count(10))
print(letters.count("a"))

numbers.clear() # Hepsini siler.


print(numbers)
print(letters)

