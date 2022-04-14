import pandas as pd

# customers = {
#     'CustomerId': [1,2,3,4],
#     'FirstName': ['Ahmet','Ali','Hasan','Canan'],
#     'LastName': ['Yılmaz','Korkmaz','Çelik','Toprak']
# }


# orders = {
#     'OrderId': [10,11,12,13],
#     'CustomerId': [1,2,5,7],
#     'OrderDate': ['2010-07-04','2010-08-04','2010-09-04','2010-10-04',]
# }

# df_customers = pd.DataFrame(customers, columns = ['CustomerId','FirstName','LastName'])
# df_orders = pd.DataFrame(orders, columns = ['OrderId','CustomerId','OrderDate'])


# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders) #Birleştirme metodu olarak görülür ve bu kullanılır.
# result = pd.merge(df_customers,df_orders,how='inner') #inner = > Birleşmiş ortak olan bilgiyi alır ve sadece eş değeri olanları alır ve onları kullanır.
# result = pd.merge(df_customers,df_orders,how='left') # left = > Bütün müşteriler gelsin ama siparişi olmayan müşterilerde geldsin
# result = pd.merge(df_customers,df_orders,how='right') # left = > Bütün sipariş bilgileri gelir ama isimler yok sa oralara belli metodlar yazılır.
# result = pd.merge(df_customers,df_orders,how='outer') # outer = > Her türlü bilgi gelir ve bulunmayanlara belirtilen simge veya isimlendirmeler yapılır.
# result = result.fillna(value = '∼∼')



customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ['Ahmet','Ali','Hasan','Canan'],
    'LastName': ['Yılmaz','Korkmaz','Çelik','Toprak']
}
customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ['Yağmur','Çınar','Cengiz','Can'],
    'LastName': ['Bilge','Turan','Yılmaz','Turan']
}
df_customersA = pd.DataFrame(customersA, columns = ['CustomerId','FirstName','LastName'])
df_customersB = pd.DataFrame(customersB, columns = ['CustomerId','FirstName','LastName'])


result = pd.concat([df_customersA,df_customersB]) # İndex Birleştirme işlemi yapar.
result = pd.concat([df_customersA,df_customersB],axis=1) # Kolon Birleştirme işlemi yapar.

print(result)