import mysql.connector

def Kontrol(Number,Name,Surname,Birty,Gen):
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='node-app')
    cursor = connection.cursor()

    SQL = 'INSERT INTO student(StudentNubmer,Name,Surname,Birtdate,Gender) VALUES(%s,%s,%s,%s,%s)'
    values = ((Number,Name,Surname,Birty,Gen))

    cursor.execute(SQL,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'ID: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata: ' + err)
    finally:
        print('İşlemler Başarıyla Tamamlandı.')
# Tekildir.
def Kontrols(list):
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='node-app')
    cursor = connection.cursor()

    SQL = 'INSERT INTO student(StudentNubmer,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)'
    

    cursor.executemany(SQL,list)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
    except mysql.connector.Error as Err:
        print('Hata: ' + Err)
    finally:
        connection.close()
        print('İşlemler Başarıyla Tamamlandı.')
#Çoguldur.
def getProducts():
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='node-app')
    cursor = connection.cursor()


    cursor.execute('Select * From Products Order By name, price') # İkinci aynı isimlere karşılık fiyat sıralaması yapar.
    # ASC düz şekil
    # DESC şekili ters şekil

    try:
        result = cursor.fetchall()
        for product in result:
            print(f'id: {product[0]} name: {product[1]} price: {product[2]}')
    except mysql.connector.Error as Err:
        print('Hata: ' + Err)
    finally:
        connection.close()
        print('İşlemler Başarıyla Tamamlandı.')

def getProductsById(id): 
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='node-app')
    cursor = connection.cursor()

    sql = 'Select * From Products Where idProducts=%s'
    value = (id,)

    
    cursor.execute(sql,value)

    result = cursor.fetchone()

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

def getProductsInfo(): 
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='node-app')
    cursor = connection.cursor()

    sql = 'Select COUNT(*) From Products where price > 2000'
    # COUNT ' metodu sayı alma olayını yapar.
    sql = 'Select AVG(Price) From Products'
    # AVG ' metodu sayıların ortalamasını alır.
    sql = 'Select SUM(Price) From Products'
    # SUM ' metodu sayıların toplamını alır.
    sql = 'Select MIN(Price) From Products'
    # MIN ' metodu sayılarda ki en küçügünü alır.
    sql = 'Select MAX(Price) From Products'
    # MAX ' metodu sayılarda ki en büyügünü alır.
    sql = 'Select Name,Price From Products Where Price = (Select MAX(Price) From Products)'
    # MAX ' metodu sayılarda ki en büyügünü aldıktan sonra ismini alır.







    cursor.execute(sql)

    result = cursor.fetchone()

    print(f'name: {result[0]}, price: {result[1]}')

getProductsInfo()