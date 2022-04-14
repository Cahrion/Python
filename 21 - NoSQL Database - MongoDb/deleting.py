import pymongo
from bson.objectid import ObjectId

myclient  = pymongo.MongoClient('mongodb+srv://icabiKirgiz:EQ6QuCbaxu1WFvOC@cluster0.qgni8.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

for i in mycollection.find():
    print(i)

print('*'*50)

# Delete_one
# Delete_many

# mycollection.delete_one({ # Tekli siler.
#     'name': 'IPhone 7'

# })

result = mycollection.delete_many({ # Çoklu Siler
    # 'name': 'IPhone 7'
    # 'name': {'$regex':'^S'}
    # Boş olursa hepsini siler.
})

print(f'{result.deleted_count} adet kayıt silindi.')


for i in mycollection.find():
    print(i)
