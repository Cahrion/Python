import pandas as pd
import numpy as np


# data = {
#     'Column1': [1,2,3,4,5],
#     'Column2': [20,20,13,45,25],
#     'Column3': ['abc','bcaa',11,'cb','dea']
# }

# df = pd.DataFrame(data)

# def kareal(x):
#     return x * x

# kareal2 = lambda x: x*x


# result = df 
# result = df['Column2'].unique() #Birbirinden farklı olan elemanları alır.
# result = df['Column2'].nunique() #Birbirinden farklı olan elemanların sayısını alır.
# result = df['Column2'].value_counts() # Tekrarlanma olaylarını alır.
# result = df['Column1'] * 2 # Çarpar hepsini .
# result = df['Column2'].apply(kareal) # İçindeki fonksiyonu alır.
# result = df['Column2'].apply(kareal2) # İçindeki fonksiyonu alır.
# df['Column4'] = df['Column3'].apply(len) #Aynı mantık.
# result = df
# result = df.columns
# result = len(df.columns)
# result = df.index
# result = len(df.index)
# result = df.info

# result = df.sort_values('Column2') # Sıralar.
# result = df.sort_values('Column3')
# result = df.sort_values('Column3',ascending= False) #Ters sıralar. 'Ascending etkisi.


datas = {
    'Ay': ['Mayıs','Haziran','Nisan','Mayıs','Haziran','Nisan','Mayıs','Haziran','Nisan'],
    'Kategori': ['Elektronik','Elektronik','Elektronik','Kitap','Kitap','Kitap','Giyim','Giyim','Giyim'],
    'Gelir': [20,30,15,14,32,42,12,36,52]


}

dfs = pd.DataFrame(datas)
print(dfs.pivot_table(index= 'Ay',columns= 'Kategori',values='Gelir'))







# print(result)