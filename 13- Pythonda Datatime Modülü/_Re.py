import re

# result = dir(re)


# re module

str = "Python: Programlama Python saat"

# re.findall()

# result = re.findall("Python",str) #Verilen dizin içindeki kelimeleri bulur. ve liste içinde yazar.
# result = len(result)


# re.split()

# result = re.split(" ",str) #Splitin aynı.
# result = re.split("r", str) #neyden bölcegini içteki str'dan yapılır.

# re.sub()

# result = re.sub(" ","-",str) # Dönüştürme işini yapar (bkz.Join gibi)
# result = re.sub("\s","-",str) # Boşluk karakteri '\s' ile de gösterilebilir.

# re.search()

result = re.search("Python",str)

# result = result.span()
# result = result[1]
# result = result.start() # Baş
# result = result.end() # Son
# result = result.group() # Aranan kelimeyi yazar.
# result = result.string() # Aranılan bölgeyi yazar


# regular expression

result = re.findall("[abc]",str) #Parantez içindekileri arar.
result = re.findall("[a-e]",str) # a'dan e'ye kadar olanları arar.
result = re.findall("[0-395]",str) # 0-3 arasındakileri sayıları ve ek olarak 9 ve 5 i arar.
result = re.findall("[^abc]",str) # abc karakteri dışında mantıgında ('^')

result = re.findall("..",str) # (...) kaç hane varsa o kadar haneli olanları arar.
result = re.findall("P...on",str) # boş karakteride bulur yani.

#Başlıyor mu?
result = re.findall("^P",str) # Parantez içindekiyle başlıyor mu diye sorar varsa yazar.
#Bitiyor mu?
result = re.findall("n$",str) # Soru sorar doğruysa geri gönderir.
result = re.findall("Python$",str)


result = re.findall("sa*t",str) #Saçma bir şey
result = re.findall("sa+t",str) 
result = re.findall("sa?t",str) 
#Sayıya baglı olarak kaç adet olduguna bakar yanii;

result = re.findall("a{2,3}",str)
result = re.findall("[0-9]{2}",str)  # 2 basamaklı sayı dizimi arar.

# Alternatif bir dizin ekler 
# a | b = a yada b

# Gruplandırma için = (a|b|c) = > a,b,c karakterlerinin arkasına xz gelir ve denenir.

 #\$a dolar işaretini aramamıza yarar.

#\Athe => the sözcügü cümlenin başında mı ?
#the\Z => the sözcügü cümlenin sonunda mı ?


# result = re.findall("\APython",str)
# result = re.findall("saat\Z",str)
# """

# \Bthe = the kelimesi başında mı?
# the\B = the kelimesi sonunda mı?

# \Bthe = the kelimesinin başında degil mi ?
# the\B = the kelimesinin sonunda degil mi ?


# \d = Rakam ararken kullanılır
# \D = Rakam olmayanları arar.

# \w = Alfabetik karakterler
# \W = \w tam tersi


# """


print(result)