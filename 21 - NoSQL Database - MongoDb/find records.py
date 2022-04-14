import pymongo

myclient  = pymongo.MongoClient('mongodb+srv://icabiKirgiz:EQ6QuCbaxu1WFvOC@cluster0.qgni8.mongodb.net/node-app?retryWrites=true&w=majority')

mydb = myclient['node-app']
mycollection = mydb['products']
# Tekli kayıt almak.
# result = mycollection.find_one()
# Çoklu kayıt almak.
result = mycollection.find({},{'_id':0,'name':1}) #İD numarasını '0' degilse her türlü gözükür.
for i in result:
    print(i)
