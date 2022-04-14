
van = ["Bmw", "Mercedes", "Opel", "Mazda"]
lenght= len(van)
van2 = ["Audi", "Nissan"]
# print(van)
# print(lenght)

# print(van[0])
# print(van[3])

# van[3] = "Toyota"
# print(van)

# result = "Mercedes" in van
# print(result)

# print(van[-2])

# print(van.index())

# print(van[:3])

# van[2] = "Toyota"
# van[3] = "Renault"
# print(van)

# del van[3]
# print(van)

print(van[::-1])



# van3 = van + van2
# print(van3)

studentA = ["Yigit", "Bilgi" , 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan" , 1998, [80,70,90] ]

print("İsimleri: {} {} {}".format(studentA[0], studentB[0], studentC[0]))
print("Soyadları: {} {} {}".format(studentA[1], studentB[1], studentC[1]))
print("Doğum Tarihleri: {} {} {}".format(studentA[2], studentB[2], studentC[2]))
print("Aldığı Notlar: {} {} {}".format(studentA[3], studentB[3], studentC[3]))

print("Yaşları: {} {} {} ".format(2020-studentA[2], 2020-studentB[2], 2020-studentC[2]))
print(f"Not ortalamaları: {int((studentA[3][0]+studentA[3][1]+studentA[3][2])/3)} {int((studentB[3][0]+studentB[3][1]+studentB[3][2])/3)} {int((studentC[3][0]+studentC[3][1]+studentC[3][2])/3)}" )