import pandas as pd
import pickle
import matplotlib.pyplot as plt

from matplotlib import style
style.use('fivethirtyeight')


fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))

#pickle with pandas
HPI_data = pd.read_pickle('fiddy_states3.pickle') #'pickle.pickle'

TX1yr = HPI_data['TX'].resample('A', how='mean')
#print(TX1yr.head())

HPI_data['TX'].plot(ax=ax1, label='Monthly TX HPI')# = HPI_data['TX'] * 2
TX1yr.plot(ax=ax1, label='Yearly TX HPI')# = HPI_data['TX'] * 2

plt.legend(loc=4)
plt.show()


