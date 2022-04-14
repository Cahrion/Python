import pandas as pd 
import numpy as np


data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index= ['a','c','e','f','h'], columns= ['column1','column2','column3'])


df = df.reindex(['a','b','c','d','e','f','g','h'])

newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df['column4'] = newColumn


result = df
result = df['column1'].drop('a', axis = 0)

result = df.isnull() # Değersizler True olarak gösterir.
result = df.notnull() # Değerliler True olarak gösterir.
result = df.isnull().sum()
result = df['column1'].isnull().sum()
result = df[df['column1'].isnull()]
result = df[df['column1'].isnull()]["column1"]
result = df[df['column1'].notnull()]["column1"]

result = df.dropna() # axis = 0 normal olarak = > satır
result = df.dropna(axis = 1) # = > Sütün
result = df.dropna(how = 'any') # Bir tane bile varsa siler.
result = df.dropna(how = 'all') # Tüm satır öyleyse siler.
result = df.dropna(subset = ['column1','column2'], how ='all') #Hangilerinde arıyacagını seçebilirsin.
result = df.dropna(subset = ['column1','column2'], how ='any') #Hangilerinde arıyacagını seçebilirsin.
result = df.dropna(thresh = 2) # Kaç adet yeterli derecede varsa say bizden biri o diyor gibi
result = df.dropna(thresh = 4) # Kaç adet yeterli derecede varsa say bizden biri o diyor gibi
result = df.fillna(value = 1) # Nan yazan yerleri 'Burdakilerle' bunlarla degiştirebiliriz.

result = df.sum() # Toplam
result = df.sum().sum()# Hepten toplam.
result = df.size # Toplam
result = df.isnull().sum().sum() #Nullar Hepten toplam



def ortalama(df):
    Toplam = (df.sum().sum()) - (df.isnull().sum().sum())
    Sayı = (df.size) - (df.isnull().sum().sum())
    return Toplam/Sayı

result = df.fillna(value = int(ortalama(df)))

print(result)





