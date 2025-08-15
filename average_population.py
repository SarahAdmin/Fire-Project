import pandas as pd
df = pd.read_csv('Fire Population.csv',encoding='latin-1')


df['TOTAL_POPULATION'] = df['TOTAL_POPULATION'].astype(str).str.replace(',', '', regex=False)
df['TOTAL_POPULATION'] = pd.to_numeric(df['TOTAL_POPULATION'])

df1 = df.where(df['COUNTRY'] == 'England').dropna()
df2 = df.where(df['COUNTRY'] == 'Scotland').dropna()
df3 = df.where(df['COUNTRY'] == 'Wales').dropna()
df4 = df.where(df['COUNTRY'] == 'Great Britain').dropna() 

averageOne = df1['TOTAL_POPULATION'].mean()
averageTwo = df2['TOTAL_POPULATION'].mean()
averageThree = df3['TOTAL_POPULATION'].mean()
averageFour = df4['TOTAL_POPULATION'].mean() 
print(f'Average Population in England is {averageOne}.')
print(f'Average Population in Scotland is {averageTwo}.')
print(f'Average Population in Wales is {averageThree}.')
print(f'Average Population in Great Britian is {averageFour}.')
