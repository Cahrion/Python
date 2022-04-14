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

    # cursor.execute('Select * From Products')
    # cursor.execute('Select name,price From Products')

    # cursor.execute('Select * From Products Where name="Samsung S7" or price=3000')
    cursor.execute('Select * From Products Where name LIKE "%Samsung%" or price=3000') #Yüzdelerin anlamı önündekileri ve arkasındakileri ayarlayan şeyler.

    # result = cursor.fetchone() # Liste olmaksızın birinciyi kutucuklar içinde bize getirir.


    result = cursor.fetchall() # Listeleyerek hepsini bir arada getirir.
    for repting in result:
        print(repting)

    # for product in result:
    #     print(f'id: {product[0]} name: {product[1]} price: {product[2]}')

def getProductsById(id):
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='node-app')
    cursor = connection.cursor()

    sql = 'Select * From Products Where idProducts=%s'
    value = (id,)

    # cursor.execute('Select * From Products')
    # cursor.execute('Select name,price From Products')

    # cursor.execute('Select * From Products Where name="Samsung S7" or price=3000')
    # cursor.execute('Select * From Products Where name LIKE "%Samsung%" or price=3000') #Yüzdelerin anlamı önündekileri ve arkasındakileri ayarlayan şeyler.
    cursor.execute(sql,value)
    # result = cursor.fetcone() # Liste olmaksızın birinciyi kutucuklar içinde bize getirir.


    result = cursor.fetchone() # Listeleyerek hepsini bir arada getirir.

    print(f'id: {result[0]} name: {result[1]} price: {result[2]}')

    # for product in result:
    #     print(f'id: {product[0]} name: {product[1]} price: {product[2]}')

def updateProduct(id, name, price):
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='node-app')
    cursor = connection.cursor()

    sql = 'UPDATE products Set name=%s, price=%s where idProducts=%s'
    value = (name,price,id)
    cursor.execute(sql,value)

    try:
        connection.commit()
    except mysql.connector.Error as err:
        print('hata: ' + err)
    finally:
        print('+ Completed')
def UpdatePower():
    while True:
        ids = int(input('Which change ID: '))
        Names = input('New name: ')
        Prices = int(input('New Price: '))
        updateProduct(ids,Names,Prices)
        DorS = input('Stop? (Y,N)\n')
        if DorS == 'N':
            break
            
UpdatePower()
