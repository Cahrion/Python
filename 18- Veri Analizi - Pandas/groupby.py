import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','Bilgi İşlem'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]

}


df = pd.DataFrame(personeller)
result = df
# result = df.query('Departman == "İnsan Kaynakları"')
# result = df['Maaş'].sum() # Sum ' Metodu toplama işlemini yapar.
# result = df.groupby('Departman').groups
# result = df.groupby(['Departman','Semt']).groups

# semtler = df.groupby('Semtler')

# semtler = df.groupby(['Semt'])

# for name, group in semtler:
#     print(name)
#     print(group)


# for name, group in df.groupby(['Departman']):
#     print(name)
#     print(group)



# result = df.groupby('Semt').get_group('Kadıköy')
# result = df.groupby('Departman').get_group('Muhasebe')
# result = df.groupby('Semt').get_group('Kadıköy')['Maaş'].sum()
result = df.groupby('Departman').sum()
result = df.groupby('Departman').mean()
result = df.groupby('Semt').mean()
result = df.groupby('Departman')['Yaş'].max()
result = df.groupby('Departman')['Maaş'].max()['Muhasebe']
result = df.groupby('Departman').agg(np.mean)
result = df.groupby('Departman')['Maaş'].agg([np.sum,np.mean,np.max,np.min]).loc['Muhasebe']










print(result)




