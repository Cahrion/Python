message = "Hello There. My name is Can Kahraman"

# message = message.upper()      #HEPSİ BÜYÜK
# message = message.lower()      #hepsi küçük
# message = message.title()      #Sadece Baş Harfleri Büyük.
# message = message.capitalize() #Sadece baş harf büyük

# message = message.strip()   #İlk ve son karakterlerdeki boşlukları siler.
# message = message.split()   #Her kelimeyi boşluklarına göre ayrı ayrı ayırır
# message = message.split(".")
# message = " ".join (message) #Splitle ayrılan yerlere "buranın" içinmdeki şeyi ekler.

# index = message.find("Can") #Kaçıncı sayı diziliminde başladıgını söyler.

# isFound = message.startswith("H") # H harfi ile başlayıp başlamadıgını soruyor.

# isFound = message.endswith("D") # D harfi ile sonlanıp sonlanmadıgını soruyor.



# message = message.replace("Can", "İcabi") #İlk taraftakini [""] yazanı sondaki [""]'ne dönüştürür.

message = message.center(100, "*") #Kaç karakter varsa oranın tam ortasına koyar. [,"burası"] ise o ek gelenlerin ne olucagını belirler 



print(message)