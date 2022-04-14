# Inheritance (Kalıtım): Miras alma 
# yeniden yazma ugraşından kurtaran bir opsiyon

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print(f"Person aktif: {fname} {lname}")

    def who_am_i(self):
        print("I'm a person")
    
    def Hunger(self):
        print("I'm a hungery")


class Student(Person):
    def __init__(self, fname, lname, numbers):
        Person.__init__(self, fname, lname)
        self.number = numbers
        print(f"Student Aktif: {fname} {lname}")

    # override
    def who_am_i(self):
        print("I'am a student")    
    
    def pato(self):
        print("Patatesleri sever. ")

    def sayHello(self):
        print("Hello I'm a student")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")


p1 = Person("Ahmet", "Aydın")
s1 = Student("mehmet", "aydın", 123456)
t1 = Teacher("Serkan", "Yılmaz", "Math")

t1.who_am_i()
p1.who_am_i()
s1.who_am_i()
p1.Hunger()
s1.Hunger()
# p1.pato() #Biri birine baglı diğeri diğerine baglı olmadıgından dolayı olmuyor.
s1.pato()


print(f"Personel: {p1.firstName} {p1.lastName} adlı personel")
print(f"Ögrenci: {s1.firstName} {s1.lastName} adlı {s1.number} numaralı ögrenci.")
s1.sayHello()