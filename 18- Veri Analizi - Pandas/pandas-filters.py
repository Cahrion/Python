import pandas as pd
import numpy as np

data = np .random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns= ['columns1','columns2','columns3','columns4','columns5'])


result = df
result = df.columns
result = df.head() #   5 adet kayıt gelri
result = df.head(10) # İçindeki sayı kadar verir.
result = df.tail() #Sondan 5 adet 
result = df.tail(10) # İçindeki sayıyı sondan verir.
result = df['columns1'].head()# İlk 5 kaydı alır. içindeki 'bburanın' sadece
result = df.columns1.head() #Aynı mantık ama üsteki daha yararlı.
result = df[['columns1','columns2']].head() #Çoklu kayıt
result = df[['columns1','columns2']].tail() #Sonda Çoklu kayıt
result = df[5:15][['columns1','columns2']].head() #Bölmeli kayıt.
result = df[5:15][['columns1','columns2']].tail() #Bölmeli kayıt.

result = df > 50 
result = df[result]
result = df[df % 2 == 0]
result = df['columns1'][df['columns1'] > 50]
result = df['columns1'][df['columns1'] > 50][df['columns1'] % 2 == 0] # Veya;
result = df[['columns1','columns2']][(df['columns1'] > 50) & (df['columns2'] % 2 == 0)]
result = df[['columns1','columns2']][ (df['columns1'] > 50) | (df['columns2'] % 2 == 0) | (df['columns2'] <= 70) ]
result = df.query('columns1 >= 50 & columns1 % 2 == 0')
result = df.query('columns1 >= 50 & columns1 % 2 == 0')[['columns1','columns2']]
result = df.query('columns1 >= 50 | columns1 % 2 == 0')[['columns1','columns2']]

# and = & , or = |

print(result)