import quandl
import pandas as pd
import pickle
from time import sleep

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

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    #print(main_df.head())
    pickle_out = open('fiddy_states.pickle', 'wb')
    
    pickle.dump(main_df,pickle_out)
    pickle_out.close()

#grab_initial_state_data()
'''
pickle_in = open('fiddy_states.pickle', 'rb')
HPI_data = pickle.load(pickle_in)
#print(HPI_data)
'''

#pickle with pandas
HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')
print(HPI_data2)




