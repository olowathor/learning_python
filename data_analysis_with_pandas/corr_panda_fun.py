import quandl
import pandas as pd
from time import sleep
import pickle
import matplotlib.pyplot as plt

from matplotlib import style
style.use('fivethirtyeight')

api_key = open('quandlapikey.txt','r').readline()#.split("'")[1]
#print(type(api_key))

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]


def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        sleep(2)
        try:
            df = quandl.get(query,api_key=api_key)
        except Exception as e:
            print(str(e))
            continue
        df.rename(columns={'Value':str(abbv)}, inplace=True)
        #df = df.pct_change() #for fiddy_states_pct_change.pickle
        df[abbv] = (df[abbv] - df[abbv][0])/ df[abbv][0] * 100.0

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    #print(main_df.head())
    #pickle_out = open('fiddy_states.pickle', 'wb')
    pickle_out = open('fiddy_states3.pickle', 'wb')
    
    pickle.dump(main_df,pickle_out)
    pickle_out.close()

#grab_initial_state_data()

def HPI_Benchmark():
    try:
        df = quandl.get("FMAC/HPI_USA",api_key=api_key)
        #df.rename(columns={'Value':str(abbv)}, inplace=True)
        #df = df.pct_change() #for fiddy_states_pct_change.pickle
        us = 'United States'
        df[us] = (df[us] - df[us][0])/ df[us][0] * 100.0
    except Exception as e:
        print(str(e))
    return df
'''    
fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
'''
#pickle with pandas
HPI_data = pd.read_pickle('fiddy_states3.pickle') #'pickle.pickle'
HPI_State_Correlation = HPI_data.corr()
#print(HPI_State_Correlation)

print(HPI_State_Correlation.describe())

'''
benchmark = HPI_Benchmark()

#HPI_data['TX2'] = HPI_data['TX'] * 2

#print(HPI_data[['TX','TX2']]) 

HPI_data.plot(ax=ax1)
benchmark.plot(ax=ax1, color='k', linewidth=10)
plt.legend().remove()
plt.show()
'''





