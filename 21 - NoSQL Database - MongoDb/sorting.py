import pymongo
from bson.objectid import ObjectId

myclient  = pymongo.MongoClient('mongodb+srv://icabiKirgiz:EQ6QuCbaxu1WFvOC@cluster0.qgni8.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']

result = mycollection.find().sort('name', 1 ) #Sıralama 
result = mycollection.find().sort('name', -1 ) # Ters Sıralama 
result = mycollection.find().sort([('name'),('price, -1')])  # Sıralamayı ikinci bir tabana ayırır.

for i in result:
    print(i)


