import pymongo
myclient  = pymongo.MongoClient('mongodb+srv://icabiKirgiz:EQ6QuCbaxu1WFvOC@cluster0.qgni8.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

# print(myclient.list_database_names())
# print(mydb.list_collection_names())

# product = {'name':'Samsung S5', 'price': 2000}

# mycollection.insert_one() #Tek bir kayıt için
# mycollection.insert_many() #Çok kayıt eklicekseniz.
# result = mycollection.insert_one(product)
# print(result)
# print(type(result)) # Tipini gösterir
# print(result.inserted_id) # İd numarasını gösterir.


productList = [
    {'name':'Xiaomi mi8 Lite', 'price': 3000,'description':'iyi telefon'}, # Kendimiz de ID bilgisi verebiliriz.
    {'name':'Xiaomi mi8', 'price': 4000, 'categories': ['telefon','elektronik']}, # ID = identification(Kimlik)
]

result = mycollection.insert_many(productList)
# print(result.inserted_ids) # 's eki coğulluk ifade ediyor burada.
for i in result.inserted_ids:
    print(i)

