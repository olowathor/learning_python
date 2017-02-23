import pandas as pd
import pickle
import matplotlib.pyplot as plt

from matplotlib import style
style.use('fivethirtyeight')


fig = plt.figure()
ax1 = plt.subplot2grid((2,1),(0,0))
ax2 = plt.subplot2grid((2,1),(1,0),sharex=ax1)

#pickle with pandas
HPI_data = pd.read_pickle('fiddy_states3.pickle') #'pickle.pickle'

HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12)
#HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12)
TX_AK_12corr = pd.rolling_corr(HPI_data['TX'],HPI_data['AK'], 12)

#print(HPI_data[['TX','TX12MA']].head())

#HPI_data[['TX','TX12MA']].plot(ax=ax1)# = HPI_data['TX'] * 2
HPI_data[['TX','AK']].plot(ax=ax1)# = HPI_data['TX'] * 2
#HPI_data['TX12STD'].plot(ax=ax2)# = HPI_data['TX'] * 2
TX_AK_12corr.plot(ax=ax2,label='correlation TX vs. AK')# = HPI_data['TX'] * 2

plt.legend(loc=0)
plt.show()


