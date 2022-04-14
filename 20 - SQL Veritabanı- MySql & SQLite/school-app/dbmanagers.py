import mysql.connector
from datetime import datetime
from Student import Student
from Teacher import Teacher
from connection import connection
from Class import Class
from classlesson import ClassLesson
from Lesson import Lesson
class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    def getProductsById(self,id):
        sql = 'Select * From student Where idStudent=%s'
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error: ' + err )

    def getStudentByClassId(self,classid):
        sql = 'Select * From student Where ClassID=%s'
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error: ' + err )





    def addStudent(self, Student: Student):
        SQL = 'INSERT INTO student(StudentNubmer,Name,Surname,Birthdate,Gender,ClassID) VALUES(%s,%s,%s,%s,%s,%s)'
        values = (Student.StudentNubmer,Student.name, Student.surname,Student.birthdate,Student.gender,Student.classid)

        self.cursor.execute(SQL,values)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt eklendi.')
            print(f'ID: {self.cursor.lastrowid}')
        except mysql.connector.Error as err:
            print('hata: ' + err)


    def editStudent(self, Student: Student):
        sql = 'Update student Set Name=%s, Surname=%s, Birthdate=%s, Gender=%s, ClassID=%s where idStudent=%s'
        values = (Student.name,Student.surname,Student.birthdate,Student.gender,Student.classid,Student.id)

        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print('Hata: ' + err)

    def MixStudent(self, Student: Student):
        if (Student.id == 0):
            sql = 'INSERT INTO student(StudentNubmer,Name,Surname,Birthdate,Gender,ClassID) VALUES(%s,%s,%s,%s,%s,%s)'
            values = (Student.StudentNubmer,Student.name, Student.surname,Student.birthdate,Student.gender,Student.classid)
        else:
            sql = 'Update student Set Name=%s, Surname=%s, Birthdate=%s, Gender=%s, ClassID=%s where idStudent=%s'
            values = (Student.name,Student.surname,Student.birthdate,Student.gender,Student.classid,Student.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print('Hata: ' + err)
        finally:
            self.connection.close()
            print('+ Completed')
        
    def getClasses(self):
        sql = 'Select * From class'
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error: ' + err )
    
    def getClassesbyID(self,id):
        sql = 'Select * From class Where id=%s'
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return obj
        except mysql.connector.Error as err:
            print('Error: ' + err )

        
    def getStudent(self):
        sql = 'Select * From student'
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error: ' + err )
    def Deleting(self,id):
        sql = 'delete from student where idStudent=%s'
        values = (id,)
        self.cursor.execute(sql,values)

        try:
            self.cursor.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt silindi.')
        except mysql.connector.Error as err:
            print('hata: ' + err)
        finally:
            self.connection.close()
            print('+ Completed')




    def MixTeacher(self, Teacher: Teacher):
        if (Teacher.id == 0):
            sql = 'INSERT INTO Teacher(Branch,Name,Surname,Birthdate,Gender) VALUES(%s,%s,%s,%s,%s)'
            values = (Teacher.branch,Teacher.name, Teacher.surname,Teacher.birthdate,Teacher.gender)
        else:
            sql = 'Update Teacher Set Branch=%s,Name=%s, Surname=%s, Birthdate=%s, Gender=%s where id=%s'
            values = (Teacher.branch,Teacher.name,Teacher.surname,Teacher.birthdate,Teacher.gender,Teacher.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
        except mysql.connector.Error as err:
            print('Hata: ' + err)
        finally:
            self.connection.close()
            print('+ Completed')

    def getClass_LessonbyLessonID(self,id):
        sql = 'Select * From class_lesson Where LessonID=%s'
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return obj
        except mysql.connector.Error as err:
            print('Error: ' + err )
    def getLesson(self):
        sql = 'Select * From lesson'
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Lesson.CreateLesson(obj)
        except mysql.connector.Error as err:
            print('Error: ' + err )




db = DbManager()
# student = db.getProductsById(7)

# student[0].name = 'Zeliha'
# student[0].surname = 'Durmaz'
# student[0].StudentNubmer = '7894'
# student[0].id = '0'


# db.addStudent(student[0])
# db.editStudent(student[0])
# print(student[0].name)
# print(student[0].surname)
# db.MixStudent(student[0])






# students = db.getStudentByClassId(1)
# for i in students:
    # print(i.name + ' ' + i.surname + ' ' + i.StudentNubmer)