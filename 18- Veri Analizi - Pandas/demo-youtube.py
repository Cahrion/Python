import pandas as pd

df = pd.read_csv('datasets/youtube-ing.csv')
#1
result = df.head(10)
#2
result = df[5:15].head()[['channel_title','tags']]
#3
result =f'{df.columns} + {len(df.columns)}'
#4
df = df.drop(['thumbnail_link','comments_disabled','ratings_disabled','video_error_or_removed','description','trending_date'], axis=1) # Colon
#5
result = df[['likes','dislikes']].mean()
#6
result = df[['likes','dislikes']].head(50)
#7
result = df['views'].max()
result = df.query("views == views.max()")[['title','views']]
#8
result = df['views'].min()
result = df.query("views == views.min()")[['title','views']]
#9
result = df.sort_values('views').head(10)
#10
result = df.groupby('category_id')['likes'].mean().sort_values()
#11
result = df.groupby('category_id')['comment_count'].sum().sort_values(ascending= False)
#12
result = df['category_id'].value_counts()
#13
df['Uzun'] = df['title'].apply(len)
result = df[['Uzun','title']]
#14 
df['Uzunluk'] = df['tags'].str.split('|').apply(len)
result = df[['Uzunluk','tags']]
#15
df['Oran'] = (df['likes'] / df['dislikes'])
# result = df[['Oran','likes','dislikes']]
# result = df[['Oran','likes','title']].sort_values(len('Oran')).head(10)
# result = df.sort_values('Oran')

###########Ek hocanın yorumu: 

def likedislikeoranhesapla(dataset):
    likesList = list(dataset['likes'])
    dislikesList = list(dataset['dislikes'])

    liste = list(zip(likesList,dislikesList))

    oranListesi = []

    for like,dislike in liste:
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))
    return oranListesi

df['Begeni_Oranı'] = likedislikeoranhesapla(df)

print(df.sort_values('Begeni_Oranı',ascending=False)[['title','likes','dislikes','Begeni_Oranı']])