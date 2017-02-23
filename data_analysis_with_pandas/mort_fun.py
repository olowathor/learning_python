import quandl
import pandas as pd
from time import sleep
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = open('quandlapikey.txt','r').readline()#.split("'")[1]

def repair_date(df):
    df.reset_index(level=0,inplace=True)
    new_date = []
    for record in df['Date']:
        new_date.append(record[:10])
    new_dates = {}
    new_dates['Date2'] = new_date
    df2 = pd.DataFrame(new_dates)
    joined = df.join(df2)
    joined.drop(labels='Date',axis=1,inplace=True)
    joined.rename(index=str, columns={'Date2':'Date'}, inplace=True)
    joined.set_index('Date',inplace=True)
    return joined

def sp500_data():
    sleep(1)
    try:
        df = quandl.get("YAHOO/INDEX_GSPC", trim_start="1990-01-01", authtoken=api_key)
    except Exception as e:
        print(str(e))
        return pd.DataFrame()

    #print(df.head())
    df.rename(index=str, columns={'Adjusted Close':'sp500'}, inplace=True)
    #print(df.head())
    
    df["sp500"] = (df["sp500"]-df["sp500"][0]) / df["sp500"][0] * 100.0

    df = repair_date(df)
    #print(df)
    #print(type(df))
    print(type(df.columns))
    df.index = pd.to_datetime(df.index, unit='d')
    df = df.resample('1D', how='mean', axis=0)
    df.fillna(method='ffill', limit=30, inplace=True)
    df = df.resample('M')    
    df = df['sp500']
    #print(df.head())
    return df

def gdp_data():
    sleep(1)
    try:
        df = quandl.get("BCB/4385", trim_start="1990-01-01", authtoken=api_key)
    except Exception as e:
        print(str(e))
        return pd.DataFrame()

    df.rename(index=str, columns={'Value':'GDP'}, inplace=True)

    df["GDP"] = (df["GDP"]-df["GDP"][0]) / df["GDP"][0] * 100.0
    df = repair_date(df)
    #print(df.head())
    #df = df.resample('M')#.mean()
    df = df['GDP']
    df = pd.DataFrame(df)
    #print(df)
    return df

def us_unemployment():
    sleep(1)
    try:
        df = quandl.get("ECPI/JOB_G", trim_start="1990-01-01", authtoken=api_key)
    except Exception as e:
        print(str(e))
        return pd.DataFrame()

    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    #print(df.head())
    df = df.resample('1D')
    df.fillna(method='ffill', limit=30, inplace=True)
    df = df.resample('M')
    #print(df.head())
    return df

def mortgage_30y():
    query = "FMAC/MORTG"
    sleep(1)
    try:
        df = quandl.get(query, trim_start="1990-01-01", api_key=api_key)#, trim_start='1975-01-01'
    except Exception as e:
        print(str(e))
        return pd.DataFrame()

    df.rename(index=str, columns={'Value':'m30'}, inplace=True)
    df["m30"] = (df["m30"] - df["m30"][0]) / df["m30"][0] * 100.0
    df = repair_date(df)
    df.index = pd.to_datetime(df.index, unit='d')
    df = df.resample('1D')
    df.fillna(method='ffill', limit=30, inplace=True)
    df = df.resample('M')
    #print(df.head())
    return df


#grab_initial_state_data()
#sp500 = sp500_data()
US_gdp = gdp_data()
US_gdp.to_pickle('GDP.pickle')
#unemployment = us_unemployment()
#m30 = mortgage_30y()

#m30.to_pickle('mortgage.pickle')
#HPI_data = pd.read_pickle('fiddy_states3.pickle')
#print(HPI_data.head(), m30.head(), unemployment.head(), US_gdp.head(), sp500.head())
#HPI = HPI_data.join([m30, unemployment, sp500], how='inner')
#print(HPI.dropna().head())
#HPI.dropna(inplace=True)
#HPI.to_pickle('HPI.pickle')

