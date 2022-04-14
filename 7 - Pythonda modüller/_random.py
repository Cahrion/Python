import random

# result = dir(random)
# result = help(random)
# result = random.random()
# result = random.uniform(1,35)
# result = random.randint(1,100)

names = ["Ali","Yağmur","Deniz","Cenk"]

Talih = random.randint(0,len(names)-1)
Talih = random.choice(names) # direkt seçim yapar üstekinden kolayca


lister = list(range(10))
random.shuffle(lister) # karıştırıp atar:)
# print(lister)




liste = range(100)
result = random.sample(liste, 4) # sayıya göre rastgele sayılar gönderir.

print(result)

print(f"Kazanan kişi: {Talih}")