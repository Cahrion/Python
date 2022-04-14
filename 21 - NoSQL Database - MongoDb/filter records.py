import pymongo
from bson.objectid import ObjectId

myclient  = pymongo.MongoClient('mongodb+srv://icabiKirgiz:EQ6QuCbaxu1WFvOC@cluster0.qgni8.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']


# result = mycollection.find_one({'name': 'Samsung S5'})
# result = mycollection.find_one({'_id':'5f80450439199a11a14cf1fe'}) #Str oldugundan dolayı bir hata verir bu yüzden object Id yazılır
result = mycollection.find_one({'_id':ObjectId('5f80450439199a11a14cf1fe')}) 



# result = mycollection.find({
#     'name':{
#         '$in' : ['Samsung S5','Samsung S6'] 
#        # $in isim eşitligine göre alır ve onları getirir

        # in = Str Eşitligi.


#     }
# })

# result = mycollection.find({
#     'name':{
#         '$nin' : ['Samsung S5','Samsung S6'] 
#        # $nin isim eşitliginde olmayanları alır
#             # Not = Olmayan
#             # in = içerisinde
#     }
# })



# result = mycollection.find({
#     'price':{
#         # '$gt': 2000 # $gt = Büyük olan kayıtları alır bir filtreleme şekli
#         '$gte': 2000 # $gte = Büyük ve eşit olanlar

        # Greater = Büyük
        # Than = Daha
        # Equed = Eşit


#     }
# })

# result = mycollection.find({
#     'price':{
#         '$eq': 2000 # Sadece o fiyata eşit olanları alır.
#     } # Tabii bunu ek bir operator kullanmadan da sadece eşitlik verilerek de yazılabilir 
#     # 'price':2000 # Gibi

        # Equed = Eşit

# })

# result = mycollection.find({
#     'price': {
#         # '$lt': 3000   # Less Than yani 3000' den küçükler
#         '$lte': 3000   # Less Than equed yani 3000' den küçükler ve eşitler 

#         # Less = Az
#         # Than = Daha
#         # Equed = Eşit
#     }
# })

# result = mycollection.find({
#     'price': {
#         '$ne': 3000   # Not Equed Eşit olmayanları alır, o haricinde.
#         # '$ne': 2000  #İkinci bir bilgi ek olarak konulamıyor.
            
#             # Not = Olmayan
#             # Equed = Eşit
#     }
# })


result = mycollection.find({

    'name':{
        '$regex':'^S' # name alanı S ile başlayan kayıtları getirir.
            # Regular = Düzenli
            # Expression =  İfade
    
    }


})







for i in result:
    print(i)
