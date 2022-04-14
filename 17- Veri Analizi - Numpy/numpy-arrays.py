import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10) # Sayıları alır son sayı hariç yazar.
# result = np.arange(10,100,3) # En sondaki kadar ilerler ve onları alır.
# result = np.zeros(10) # Sıfırlardan oluşan bir dizi yapar (sadece sıfır.)
# result = np.ones(10) # Birlerden oluşan bir dizi yapar (sadece bir.)
# result = np.linspace(0,100,5) # Bölme işlemini sondakine göre başlangıç ve sonu böler.
# result = np.linspace(0,5,10) # Float bir sayıda yapabilir.
# result = np.random.randint(0,10) # 10 dahil degil ve random bir sayi turu üretir.
# result = np.random.randint(10) # Bitiş deger verir ve sıfırdan başlar.
# result = np.random.randint(1,10,3) # Son gelen ek kaç adet random sayı istendigini belirtir ve ona göre sayı birimi getirir.
# result = np.random.rand(5) # 0-1 arasında üretir.
# result = np.random.randn(5) # -1 ile 1 arasında bir sayi üretir.
# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10) # Mantiken sayıları bir merkeze aldık.
# print(np_multi.sum(axis=1)) # Satırdakilerin toplamları gelir.
# print(np_multi.sum/axis=0) # Sütünların toplamını verir.


rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max() #En büyük sayı degerini verir.
result = rnd_numbers.min() #En küçük sayı degerini verir.
result = rnd_numbers.mean() # Ortalamayı verir.
result = rnd_numbers.argmax() # En büyügün indexsini verir.
result = rnd_numbers.argmin() # En küçügün indeksini verir.

print(result)
