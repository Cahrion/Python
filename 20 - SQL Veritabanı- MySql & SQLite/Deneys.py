import mysql.connector

def insertProducts(list):
    connection = mysql.connector.connect(host='localhost',user = 'root',password ='MySqlŞifrem4862', database='englishdatebase')
    cursor = connection.cursor()
        
    sql = 'INSERT INTO quiz(English,Turkish) VALUES (%s,%s)'
    values = ("singe","sarkı soylemek")

    cursor.executemany(sql,values)

    try:
        connection.commit()
    except mysql.connector.Error as err:
            print('hata: ', err)
    finally:
        connection.close()


list = []
while True:
    a = input('Yapmak istedikleriniz nelerdir?\n1- DataBase göster.\n2- Yeni bir eşya ekle \n3- Kapat\nSayı ile giriniz: ')
    if a == "1":
        Show()
    if a == "2":
        print('')
        print('----  ----')
        print('')
        english = input('Adı: ')
        turkish = input('Adı: ')
        list.append((english,turkish))
        insertProducts(list)
        
    if a == "3":
        break