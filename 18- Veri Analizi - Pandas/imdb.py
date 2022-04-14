import pandas as pd

dt = pd.read_csv('IMDB.csv')
#1
result = dt.head()
#2
result = dt.head(10)
#3
result = dt.tail()
#4
result = dt.tail(10)
#5
result = dt['Movie_Title']
#6
result = dt['Movie_Title'].head()
#7
result = dt[['Movie_Title','Rating']].head()
#8
result = dt[['Movie_Title','Rating']].tail(7)
#9
result = dt[5:15][['Movie_Title','Rating']].head()
# 10
result = dt.query('Rating > 8.0')[['Movie_Title','Rating']].head(50)
# 11
result = dt.query('YR_Released >= 2014 & YR_Released <= 2015')[['Movie_Title','YR_Released']]
# 12
result = dt.query('(Num_Reviews > 100000) | (Rating >= 8 & Rating <= 9)')[['Movie_Title','YR_Released','Rating','Num_Reviews']]




print(result)







