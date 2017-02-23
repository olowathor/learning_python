import pandas as pd
import pickle
import matplotlib.pyplot as plt

from matplotlib import style
style.use('fivethirtyeight')

bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}

df = pd. DataFrame(bridge_height)
df['std'] = pd.rolling_std(df['meters'], 2)

df_std = df.describe()['meters']['std']

df = df[(df['std'] < df_std)]

df[['meters','std']].plot()# = HPI_data['TX'] * 2
plt.show()


