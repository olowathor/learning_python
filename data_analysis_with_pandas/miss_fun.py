import pandas as pd
import pickle
import matplotlib.pyplot as plt

from matplotlib import style
style.use('fivethirtyeight')


fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

#pickle with pandas
HPI_data = pd.read_pickle('fiddy_states3.pickle') #'pickle.pickle'

HPI_data['TX1yr'] = HPI_data['TX'].resample('A', how='mean')
#print(HPI_data[['TX','TX1yr']].head())
#HPI_data.dropna(inplace=True)#(how='all')
HPI_data.fillna(method='ffill',inplace=True)#(method='bfill')

#print(HPI_data[['TX','TX1yr']].head())

HPI_data[['TX','TX1yr']].plot(ax=ax1, label='Yearly TX HPI')# = HPI_data['TX'] * 2

plt.legend(loc=4)
plt.show()


