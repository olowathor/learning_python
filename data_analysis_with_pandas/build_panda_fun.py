#import quandl

import pandas as pd

#api_key = open('quandlapikey.txt','r').readline()#.split("'")[1]

'''
###############################################
#Does not work
#print(api_key)
#df = quandl.get("FMAC/HPI_AK", authtoken=api_key)

#print(df.head())
#Does not work
###############################################
'''

'''
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

for abbv in fiddy_states[0][0][1:]:
    print("FMAC/HPI_" + str(abbv))
'''

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
'''
concat = pd.concat([df1,df2,df3])

print(concat)

df4 = df1.append(df2)
print(df4)
'''

s = pd.Series([80,2,50], index = ['HPI','Int_rate','US_GDP_Thousands'])
df5 = df1.append(s, ignore_index=True)

print(df5)

