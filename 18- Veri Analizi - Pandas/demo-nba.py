import pandas as pd


df = pd.read_csv('datasets/nba.csv')

result = df
#1
result = df.head(10)
#2
result = len(df.index)
#3
result = int(df['Salary'].mean())
#4
result = df['Salary'].max()
#5
result = df.query("Salary == Salary.max()")[['Name','Salary','Team']]
#6
result = df.query('Age >= 20 & Age <= 25')[['Name','Team']]
#7
result = df.query('Name == "John Holland"')[['Team','Name']]
#8
result = df.groupby('Team').mean()
#9
result = len(df.groupby('Team'))
result = df['Team'].nunique()



# 10
result = df['Team'].value_counts()

# 11
# df = df.dropna()
df = df.fillna('~~')
# result = df[df['Name'].str.contains('and')]


def str_find(name):
    if 'and' in name.lower():
        return True
    return False

result = df[df['Name'].apply(str_find)]

print(result)