import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)


result = numbers1 + numbers2#Birbiriyle toplanır ve dizi sayısı eşit olması gerekir.
                            # Eşit sayıda dizi toplanmış halde oluşur. '-' de geçerlidir.
result = numbers1 + 10  # Belirtilen sayı her dizi'ye eklenir. '-' da geçerlidir.
result = numbers1 * numbers2 # Çarpılır bütün değerler karşılarındaykiyle.
result = numbers1 / numbers2 # Bölüm yapılır.
result = np.sin(numbers1)  # Sinisünü alır
result = np.sqrt(numbers1) #Karekökünü alır.
result = np.log(numbers1) # Logaritması alınır.

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

# print(mnumbers1)
# print(mnumbers2)

result = np.vstack((mnumbers1,mnumbers2)) # Dikey şekilde birleştirme yapar
result = np.hstack((mnumbers1,mnumbers2)) # Yatay şekilde birleştirme yapar

result = numbers1 >= 50 #Seçilenlerin kaç tanaesinin elliden büyük olup olmadıgını bulur burada 'TRUE' ve 'FALSE' değerleri verir.
result =  numbers1 % 2 == 0 # True veya false değerleri verir.
# for ap in result:
#     if ap:
#         print("Sayı bir çiftir.")
#     else:
#         print('Sayı bir tektir.')

print(numbers1[result]) #True değerleri alır ve onları gönderir.



print(result)
