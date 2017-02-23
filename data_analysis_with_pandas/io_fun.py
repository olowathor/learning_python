import pandas as pd
'''
df = pd.read_csv('zavodnici_kb.csv')

#print(df.head())

df.set_index('cup', inplace=True)

df.to_csv('zkouska.csv')

df2 = pd.read_csv('zkouska.csv', index_col=0)
print(df2.head())

df2.columns = ['Jmeno','první','druhý','třetí','účast','disciplína']

print(df2.head())
df2.to_csv('zkouska2.csv')
df2.to_csv('zkouska3.csv', header=False)
'''

df3 = pd.read_csv('zkouska3.csv', names=['pohár','jmeno','první',
                                        'druhý','třetí','účast','disciplína'],
                                        index_col=0)

#print(df3.head())

df3.to_html('vysledky.html')

df3.rename(columns={'jmeno':'name'}, inplace=True)
#print(df3.head())



