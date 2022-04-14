import pandas as pd



Data = [['Ahmet',50,'Koç'],['Ali',60,'Yay'],['Yağmur',70,'Yengeç'],['Çınar',80,'Akrep']]
dict = {'İsim': ["Ahmet","Ali","Yağmur","Çınar"],'Puan':[50,60,70,80],'Burç':["Koç","Yay","Yengeç","Akrep"]}
dict_list = [       
    
                        {'İsim':'Ahmet','Puan':50,'Burç':'Koç'},
                        {'İsim':'Ali','Puan':60,'Burç':'Yay'},
                        {'İsim':'Yağmur','Puan':70,'Burç':'Yengeç'},
                        {'İsim':'Çınar','Puan':80,'Burç':'Akrep'}


]



# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# df = pd.DataFrame([['Ahmet',50,'Koç'],['Ali',60,'Yay'],['Yağmur',70,'Yengeç'],['Çınar',80,'Yengeç']])
# df = pd.DataFrame(Data, columns = ['isim','Puan','burç'], index = [1,2,3,4], dtype = float)# Dtype int yani tam sayıları tam sayı olmayanlara çeviri.
# df = pd.DataFrame(dict)
# df = pd.DataFrame(dict, index = ['252','178','215','227'])
# df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list, index =['252','178','215','227'])



print(df)












# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1,oranges = s2)

# df = pd.DataFrame(data)
# print(df)