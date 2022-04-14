website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"
lenght = len(course)
lenght2 = len(website)
print(lenght)
print(lenght2)
print(website[7:10])
print(website[22:25])
print(course[:15])
print(course[-15:])
print(course[::-1]) 

name, surname, age, job = "Bora" , "Yılmaz" , 32, "mühendis"

print("Benim adım {} {}, Yaşım {} ve mesleğim {}".format(name, surname, age , job )  )

s = "Hello world"
s = s[0:6] + "W" + s[-4:]
      # s.replace("w","W")
print(s)


print("{0}{0}{0}".format("abc"))