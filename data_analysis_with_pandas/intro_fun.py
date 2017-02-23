import pandas as pd
#import datetime
#import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

'''
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 1, 1)

df = web.DataReader("XOM","yahoo", start, end)
print(df.head())

df['Adj Close'].plot()
plt.show()
'''

web_stats = {'Day': [1,2,3,4,5,6], 'Visitors':[43,53,34,45,64,34], 'Bounce rate':[65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)# making data frame

'''
print(df)

print(df.head())
print(df.tail())
print(df.tail(2))

print(df.set_index('Day'))
print(df.head())
df2 = df.set_index('Day')
print(df2.head())
df.set_index('Day', inplace=True)
print(df.head())

print(df['Visitors'])
print(df.Visitors)
'''

print(np.array(df[['Bounce rate','Visitors']]))

print(df.Visitors.tolist())

df2 = pd.DataFrame(np.array(df[['Bounce rate','Visitors']]))

print(df2)

