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

    sql = 'Select * From products'
    sql = 'Select * From Categories'
    sql = 'Select * From products inner join Categories on Categories.id=Products.Categoryid'
    sql = 'Select Products.name,Products.price, Categories.name From products inner join Categories on Categories.id=Products.Categoryid'
    sql = 'Select Products.name,Products.price, Categories.name From products inner join Categories on Categories.id=Products.Categoryid where Categories.name="Telefon"'
    sql = 'Select P.name,P.price, C.name From products as P right join Categories as C on C.id=P.Categoryid '



    cursor.execute(sql)




    try:
        result = cursor.fetchall()
        for product in result:
            print(product)
    except mysql.connector.Error as Err:
        print('Hata: ' + Err)
    finally:
        connection.close()
        print('İşlemler Başarıyla Tamamlandı.')




getProducts()