import pymongo
from bson.objectid import ObjectId

myclient  = pymongo.MongoClient('mongodb+srv://icabiKirgiz:EQ6QuCbaxu1WFvOC@cluster0.qgni8.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']


# Update_one # Bir kayıt günceller.
# Update_many  # Birden fazla kayıt günceller.

for i in mycollection.find():
    print(i)


# mycollection.update_one( #Burdugu ilk kayıt üzerinde bu güncellemeyi yapar.
#     {'name': 'IPhone 6'},
#         {'$set': {
#             'name': 'Samsung S7',
#             'price': 4200
#         }}
# )

result = mycollection.update_many( #Burdugu bütün kayıtlar üzerine yapar.
    {'name': 'Samsung S8'},
        {'$set': {
            'name': 'IPhone 7',
            'price': 6200

        }}
)

print(f'{result.modified_count} adet kayıt güncellendi.') #Kaç adet güncelleme işlemi oldugundan bahseder.
# Count = Miktarı, Sayısı
# Modified = Değiştirilmiş








print(f'-- Dur --'.center(50,'-'))
for i in mycollection.find():
    print(i)