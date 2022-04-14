from dbmanagers import DbManager
from datetime import datetime
from Student import Student
from Teacher import Teacher


class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = '*****\nn1- Ögrenci Listesi\nn2- Ögrenci Ekle\nn3- Ögrenci Güncelle\nn4- Ögrenci Sil\nn5- Ögretmen Ekle \nn6- Derslere göre sınıflar\n- Çıkış(E/Ç)'
        while True:
            print(msg)
            islem = input('Seçim: ')
            if islem == "1":
                self.displayStudents()
                break
            elif islem == '2':
                self.addStudents()
                break
            elif islem == '3':
                self.UpdatingStudents()
                break
            elif islem == '4':
                self.StudingDelete()
                break
            elif islem == '5':
                self.addTeachers()
                break
            elif islem == '6':
                self.WhoLesson()
                break
            elif islem == 'E' or islem == 'Ç':
                break
            else:
                print('*****\nYanlış Seçim')

    def StudingDelete(self):
        self.StudentList()
        informatin = int(input('Silmek istediginiz Ögrencinin ID:'))
        self.db.Deleting(informatin)


    def displayStudents(self):
        self.displayClasses()
        classid = int(input('hangi sınıf: '))
        print('')
        students = self.db.getStudentByClassId(classid)
        print('~ Ögrenci Listesi ~')
        print('')
        for i in students:
            print(f'{i.StudentNubmer} : {i.name} {i.surname}')
        for index,i in enumerate(students): # Burada ki enumerate Biri index numarası ekler ve bir index eklenerek o numara alınabilir.
            print(f'{index+1}~ {i.name} {i.surname}')
        
        print('')

    def addStudents(self):
        Many = int(input('Kaç adet ögrenci eklemek istesiniz: '))
        while Many > 0:

            OgrName = input('İsmi: ')
            OgrSurName = input('Soyismi: ')
            OgrStudentNubmer = int(input('Numarası: '))
            OgrBirthdate = input('Doğum Tarihi (10/10/2010): ')
            OgrBirthdates = OgrBirthdate.split('/')
            birthdate = datetime(int(OgrBirthdates[2]),int(OgrBirthdates[1]),int(OgrBirthdates[0]))
            OgrGender = input('Cinsiyeti: ')
            self.displayClasses()
            OgrClass = int(input('Sınıfı: '))
            Many -= 1
            student = Student(None,OgrStudentNubmer,OgrName,OgrSurName,birthdate,OgrGender,OgrClass)
            self.db.MixStudent(student)
            
    def displayClasses(self):
        classes = self.db.getClasses()
        for i in classes:
            print(f'{i.id}: {i.name}')


    def StudentList(self):
        print('')
        Student = self.db.getStudent()
        for Std in Student:
            print(f'ID: {Std.id} , {Std.name} {Std.surname}')
        print('')

    def UpdatingStudents(self):
        self.StudentList()

        information = input('Degiştirmek istenen ögrencinin ID: ')    
        StudentInfos = self.db.getProductsById(information)
        print('~~ Bilgiler ~~')
        for StudentInfo in StudentInfos:
            print(f' --------------------------------')
            print(f'|')
            print(f'| N1- ID: {StudentInfo.id}')
            print(f'| N2- Name: {StudentInfo.name} {StudentInfo.surname}')
            print(f'| N3- Birthdate: {StudentInfo.birthdate}')
            print(f'| N4- Gender: {StudentInfo.gender}')
            print(f'| N5- Class: {(self.db.getClassesbyID(int(StudentInfo.classid))[1])}')
            print(f"|")
            print(f' --------------------------------')
        while True:
            info = input('Neyi Degiştirmek isterdiniz (1,2,3,4,5)\nSeçim: ')
            if info == '1':
                StudentInfos[0].id = input('New ID: ')
                self.db.MixStudent(StudentInfos[0])
            elif info == '2':
                StudentInfos[0].name = input('New Name: ')
                StudentInfos[0].surname = input('New Surname: ')
                self.db.MixStudent(StudentInfos[0])
            elif info == '3':
                Birthdate = input('New Birthdate (10/10/2010)\nSeçim: ')
                Birthdates = Birthdate.split('/')
                StudentInfos[0].birthdate = datetime(Birthdates[2],Birthdates[1],Birthdates[0])
                self.db.MixStudent(StudentInfos[0])
            elif info == '4':
                StudentInfos[0].gender = input('New Gender: ')
                self.db.MixStudent(StudentInfos[0])          
            elif info == '5':
                self.displayClasses()
                print('Lütfen bir rakam giriniz.')
                StudentInfos[0].classid = int(input('New Class: '))
                self.db.MixStudent(StudentInfos[0])             
            Failed = input("Çıkmak için (X) yazınız.Devam etmek için (ENTER)'layın")
            if Failed == 'X':
                break
        
    def addTeachers(self):
        Many = int(input('Kaç adet Ögretmen eklemek istesiniz: '))
        while Many > 0:

            OgrtName = input('İsmi: ')
            OgrtSurName = input('Soyismi: ')
            OgrtBranch = input('Bölümü: ')
            OgrtBirthdate = input('Doğum Tarihi (10/10/2010): ')
            OgrtBirthdates = OgrtBirthdate.split('/')
            birthdate = datetime(int(OgrtBirthdates[2]),int(OgrtBirthdates[1]),int(OgrtBirthdates[0]))
            OgrtGender = input('Cinsiyeti: ')
            teacher = Teacher(None,OgrtBranch,OgrtName,OgrtSurName,birthdate,OgrtGender)
            Many -= 1
            self.db.MixTeacher(teacher)

    def WhoLesson(self):
        Lessons = self.db.getLesson()
        for i in Lessons:
            print(f'{i.id} - {i.name}')
        Who = input('Ögrenmek istediginiz derslik: ')
        print(f'Seçilen derste olan derslik: {self.db.getClassesbyID(self.db.getClass_LessonbyLessonID(Who)[0])[1]}')



        # (self.db.getClassesbyID(int(StudentInfo.classid))[1])



app = App()
app.initApp()