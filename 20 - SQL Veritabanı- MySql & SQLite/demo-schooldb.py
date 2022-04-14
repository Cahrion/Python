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
# Tekildir.
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
# Çoguldur.
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
# Kontrols()
Whiles()

"""


Hoca Kafasında Komutlar Haritasi:


"""
"""
class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentNumber,name,surname,birthdate,gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate= birthdate
        self.gender = gender
    def SaveStudent(self):
        SQL = 'INSERT INTO student(StudentNubmer,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)'
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(SQL,value)
        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as Err:
            print('Hata: ', Err)
        finally:
            Student.connection.close()
            print('İşlemler Başarıyla Tamamlandı.')

# ahmet = Student('202','ahmet','yılmaz',datetime(2005, 5, 17), 'E')
# ahmet.SaveStudent()

    @staticmethod
    def SaveStudents(students):
        SQL = 'INSERT INTO student(StudentNubmer,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)'
        value = (students)
        Student.mycursor.executemany(SQL,value)
        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as Err:
            print('Hata: ', Err)
        finally:
            Student.connection.close()
            print('İşlemler Başarıyla Tamamlandı.')

ogrenciler = [
    ('301','Ahmet','Yılmaz',datetime(2005, 5,17),'E'),
    ('302','Ali','Can',datetime(2006, 6,17),'E'),
    ('303','Canan,','Tan',datetime(2005, 7,7),'K'),
    ('304','Ayşe','Taner',datetime(2005, 9,23),'K'),
    ('305','Bahadır','Toksöz',datetime(2004 ,7,27),'E'),
    ('306','Ali','Cenk',datetime(2003, 8,25),'E')
]
Student.SaveStudents(ogrenciler)

"""