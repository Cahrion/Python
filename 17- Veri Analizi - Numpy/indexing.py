import numpy as np


numbers = np.array([0,5,10,15,20,25,50,75])


result = numbers[5]
result = numbers[-1]
result = numbers[0:3]
result = numbers[:3]
result = numbers[3:]
result = numbers[::]
result = numbers[::-1]

print(result)


numberss = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numberss[:,2] # :' işareti bütün satırları ele alır. ve her periyodun 'Kaçınçı ise onu alır.
result = numberss[:,0:2] # İkinci yere ve üçünçü yere yazılan yerlerin arasındakileri alır ve yazar.
result = numberss[-1,:] # Sondaki tarafı alır.
result = numberss[:2,:2]

arr1 = np.arange(0,10)
# arr2 = arr1 # referans

arr2 = arr1.copy()

#Adress birliginden dolayı degişenn birşey herkesde degişir.

arr2[0] = 20

print(arr1)
print(arr2)



# print(numberss[0][2]) == print(numberss[0,2])
print(numberss[0,2])
print(result)