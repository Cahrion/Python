import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='node-app')
    cursor = connection.cursor()
        
    sql = 'INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)'
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'ID: {cursor.lastrowid}')
    except mysql.connector.Error as err:
            print('hata: ', err)
    finally:
        connection.close()
        print('DataBase baglantısı kapandı.')
def Show():
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='node-app')

    mycursor = connection.cursor()
    mycursor.execute('SHOW DATABASES')
    print('')
    print('---- DataBase ----')
    print('')
    for x in mycursor:
        print(x)
    print('')
    print('---- DataBase ----')
    print('')
def insertProducts(list):
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='node-app')
    cursor = connection.cursor()
        
    sql = 'INSERT INTO Products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)'
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt eklendi.')
        print(f'ID: {cursor.lastrowid}')
    except mysql.connector.Error as err:
            print('hata: ', err)
    finally:
        connection.close()
        print('DataBase baglantısı kapandı.')


list = []
while True:
    a = input('Yapmak istedikleriniz nelerdir?\n1- DataBase göster.\n2- Yeni bir eşya ekle \n3- Kapat\nSayı ile giriniz: ')
    if a == "1":
        Show()
    if a == "2":
        Piece = int(input('Kaç adet bilgi yükliceksiniz: '))
        while Piece > 0:
            print('')
            print('----  ----')
            print('')
            names = input('Adı: ')
            prices = float(input('Fiyatı: '))
            imageurls = input("Fotograf Url'si: ")
            descriptions = input("Değerlendirmesi: ")
            list.append((names,prices, imageurls, descriptions))
            print('')
            print('----  ----')
            print('')
            Piece = Piece - 1
        insertProducts(list)
        
    if a == "3":
        break