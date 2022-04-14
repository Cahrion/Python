from datetime import datetime
from datetime import timedelta

simdi = datetime.now()
# result1 = simdi.year
# result2 = simdi.month
# result3 = simdi.day
# result4 = simdi.hour
# result5 = simdi.minute
# result6 = simdi.second
# result7 = datetime.ctime(simdi)

# sa = [result1,result2,result3,result4,result5,result6]

# for a in sa:
#     print(a)
# print(result7)

# result = datetime.strftime(simdi,"%Y")
# result = datetime.strftime(simdi,"%X")
# result = datetime.strftime(simdi,"%d")
# result = datetime.strftime(simdi,"%d")
# result = datetime.strftime(simdi,"%A")
# result = datetime.strftime(simdi,"%B")
# result = datetime.strftime(simdi,"%Y %B %A")

# t = "20 Nisan 2020"
# gun, ay, yıl = t.split()
# print(gun)
# print(ay)
# print(yıl)


# t = "15 April 2019 hour 10:12:30"

# dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
# print(dt)


# birtday = datetime(2002,3,28,12,17,00)

# result = datetime.timestamp(birtday) #Saniye cinsinden belirtilir.
# print(result)
# result = datetime.fromtimestamp(result) # Saniye bilgisini yeniden tarih bilgisi yapar.
# print(result)
# result = datetime.fromtimestamp(0) # Hangi tarihten itibaaren ele aldıgını gösterir.
# print(result)


# result = simdi - birtday # timedelta gün olarak parçalar.
# result = result.days #Gün olarak parçalar.

# result = result.second
# result = result.microseconds
print(simdi)
result = simdi + timedelta(days=10) # belli günleri çıkar veya toplama işlemi
result = simdi - timedelta(days=10) # yapma olayını sağlayan parametre.


print(result)