import numpy as np
# # 1 
# number = np.array([10,15,30,45,60])
# # 2
# number = np.arange(5,15)
# # 3
# number = np.arange(50,100,5)
# # 4 
# number = np.zeros(10)
# # 5
# number = np.ones(10)
# # 6 
# number = np.linspace(0,100,5)
# # 7
# number = np.random.randint(10,30,5)
# # 8
# number = np.random.randn(10)
# # 9
# numberz = np.random.randint(10,50,15) 
# number = numberz.reshape(3,5)
# print(number)
# # 10
# numbers = (number.sum(axis=1)) 
# numbers = (number.sum(axis=0))
# # 11
# Enbüyük = numbers.max()
# minnak= numbers.min()
# ort = numbers.mean()
# numbers = f'{Enbüyük}, {minnak}, {ort}'
# # 12
# numbers = np.argmax(number) +1
# # 13
# number = np.arange(10,20)
# numbers = number[0:3]
# # 14
# numbers = number[::-1]
# # 15
# numbers = number[0]
# # 16
# numbers = number[1,2]
# # 17
# numbers = number[:,0]
# # 18 
# numbers = number ** 2
# # 19
number = np.random.randint(-50,50,15)
number = number.reshape(3,5)
print(number)
numberZ = number[(number > 0)]
numberS = numberZ[numberZ % 2 == 0]


print(numberS)