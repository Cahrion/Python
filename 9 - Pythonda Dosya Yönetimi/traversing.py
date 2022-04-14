# file = open("newfile.txt","r", encoding="utf-8")

# tek tek aç kapa yerine yeni bir komut yani; "with"

with open("newfile.txt","r", encoding="utf-8") as file:
    content = file.read() # içteki yer kaça kadar "10'ise" 10'a kadar.
    print(content)
    file.seek(0) # Klösörün konumunu ayarlar ve degiştirir.
    print(file.tell()) # "tell" yanan klösörün konumunu verir.
    content2 = file.read()
    print(content2)

# file.close()