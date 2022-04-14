import mysql.connector
from datetime import datetime
from connection import connection


def Kontrol(Number,Name,Surname,Birty,Gen):
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
def Kontrols(list):
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
def Whiles():

    while True:
        Won = input('Ne yapmak istediniz.\n1- Ögrenci Ekleme\n2- Kapat\nLütfen numarasını kodlayınız: ')
        if Won == "1":
            list = []
            ask = int(input('Kaç adet Yüklemek istersiniz: '))
            while ask > 0:
                numbers = input('Numarası: ')
                names = input('İsim: ')
                surnames = input('Soyisim: ')
                dates = input('Doğum Tarihi(Gün/Ay/Yıl): ')
                dates = dates.split('/')
                genders = input('Cinsiyet: ')
                list.append((numbers, names, surnames,datetime(int(dates[2]),int(dates[1]),int(dates[0])),genders))
                ask -= 1
            Kontrols(list)
        if Won == "2":
            break


def Looking():
    cursor = connection.cursor()

    # sql = 'Select * from student'
    # sql = 'Select StudentNubmer,Name,Surname from student'
    # sql = 'Select Name,Surname from student where Gender = "K"'
    # sql = 'Select Name,Surname from student where YEAR(birthdate) = 2003'
    # sql = 'Select Name,Surname,idStudent from student where name = "Ali" and YEAR(birthdate) = 2005'
    # sql = 'Select Name,Surname from student where Name LIKE "%an%" or Surname LIKE "%an%"'
    # sql = 'Select COUNT(Gender) from student where Gender = "E"'
    # sql = 'Select Name from student where Gender = "K" Order By name'
    sql = 'select * from student LIMIT 3' # Limit düzeltme yapılır ve limite göre alım yapar.

    cursor.execute(sql)



    try:
        result = cursor.fetchall()
        for Res in result:
            # print(Res)
            # print(f'Name: {Res[0]} {Res[1]} ')
            # print(f'ID: {Res[2]} |-| Names: {Res[0]} ')
            print(f'Name: {Res[0]}')
    except mysql.connector.Error as err:
        print(f'Hata: {err}')
    finally:
        connection.close()



Looking()
