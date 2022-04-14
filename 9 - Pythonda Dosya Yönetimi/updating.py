# with open("newfile.txt","r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())

# ***** Sayfa sonunda güncelleme *****

# with open("newfile.txt","a", encoding="utf-8") as file: # append ek bir yazı yazar.
#     file.write("\nEmel Turan")

# ***** Sayfa başında güncelleme *****

# with open("newfile.txt","r+", encoding="utf-8") as file: 
#     content = file.read()
#     content = "Efe Turan\n" + content 
#     file.seek(0)
#     file.write(content)

# with open("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())


# ***** Sayfa ortasında güncelleme *****

with open("newfile.txt","r+", encoding="utf-8") as file:
    list2 = file.readlines()
    list2.insert(1,"Yılmaz Korkmaz\n")
    file.seek(0)
    # for a in list2:
    #     file.write(a)
    file.writelines(list2)
    
with open("newfile.txt","r+", encoding="utf-8") as file:
    print(file.read())