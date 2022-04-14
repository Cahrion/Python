import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ['A',"B","C"], columns= ['Column1','Column2','Column3'])


result = df
result = df['Column1'] #Seçim yapılabilir Colonlardan.
result = type(result)
result = df[["Column1","Column2"]]

# loc["loc","column"] = > loc[":","column"]
# Loc formülü her ikisinide veren bir mantık ve ilk yere bir index verirsek sadece index
# Eğer ':' yazıp diğer yere bir index verirsek ise colon bilgilerini verir.
# Bilakis  "15"'de oldugu gibi
 
result = df.loc["A"] #Yan index Bölümünü veriri.
result = type(result)
result = df.iloc[2] # Öne gelen ,' mantıgı sayısal anlamda ele alır ve 2.'gibi alır.

# result = df.loc[:,"Column2"] # 15
# result = df.loc[:,["Column1","Column2"]]
# result = df.loc[:,'Column1':'Column3'] #İsimler arasındakilerde dahil olarak bir alma işlemi yapar.
# result = df.loc[:,:"Column3"] # Başlangıç'tan başlar oraya kadar.
# result = df.loc['A':'C',:"Column2"] # Aynı mantık yan taraftan olan indexlerlede geçerlidir.
# result = df.loc[:'C',:"Column2"] # Aynı
result = df.loc["A","Column1"] # Tekli İşlem yapar.
result = df.loc[["A","B"],["Column1","Column2"]]

df["Column4"] = pd.Series(randn(3), ["A","B","C"])
df['Column5'] = df["Column1"] + df['Column3']

result = (df.drop('Column5', axis = 1)) # Silme işlemi yapar. #Ekstra olarak axis = metodunu kullanarak yukardan mı aşagıdan mı bir aygıt oldugunu söylememiz gerekiyor.
# Burda result çalışır ve silinmiş hali ama orjinal aynı kalır.
print(result)

result = (df.drop('Column5', axis = 1, inplace = True)) # Eğer burası True olursa global olarak her türlü adres degişir ve hepsine etki eder.
# print(result) # Ama bu parametre işlevsiz olarak sadece silme işlemi yapmış bir parametre olur.
# Veyahut resul parametresine atamak yerine normalde yazılabilir.
df.drop('Column5', axis = 1, inplace = True)

print(df)


