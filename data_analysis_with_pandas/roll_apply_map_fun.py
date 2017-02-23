import quandl
import pandas as pd
import numpy as np
from statistics import mean
from sklearn import svm, preprocessing, cross_validation

import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = open('quandlapikey.txt','r').readline()#.split("'")[1]

'''
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

def HPI_Benchmark():
    try:
        df = quandl.get("FMAC/HPI_USA", trim_start="1990-01-01", api_key=api_key)
    except Exception as e:
        print(str(e))

    df.rename(index=str, columns={'Value':'US'}, inplace=True)
    df['US'] = (df['US'] - df['US'][0])/ df['US'][0] * 100.0
    df = repair_date(df)
    df.index = pd.to_datetime(df.index, unit='d')
    pd.DataFrame(df)
    #print(df.head())
    return df

HPI_bench = HPI_Benchmark()
HPI_bench.to_pickle('HPI_bench.pickle')
'''
#HPI_bench = pd.read_pickle('HPI_bench.pickle')
#print(pd.read_pickle('GDP.pickle').head())
#print(pd.read_pickle('HPI_bench.pickle').head())

def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0

def moving_average(values):
    return mean(values)

housing_data = pd.read_pickle('HPI.pickle')
housing_data = housing_data.join(pd.read_pickle('GDP.pickle'), how='inner')
housing_data = housing_data.join(pd.read_pickle('HPI_bench.pickle'), how='inner')

housing_data = housing_data.pct_change()

housing_data.replace([np.inf,-np.inf], np.nan, inplace=True)
housing_data.dropna(inplace=True)

housing_data['US_HPI_future'] = housing_data['US'].shift(-1)
housing_data.dropna(inplace=True)

housing_data['Label'] = list(map(create_labels, housing_data['US'], housing_data['US_HPI_future']))
#print(housing_data[['US','US_HPI_future','Label']].head())
'''
housing_data['ma_apply_example'] = pd.rolling_apply(housing_data['m30'], 10, moving_average)
print(housing_data.tail())
'''
housing_data.dropna(inplace=True)
house = housing_data.drop(['US_HPI_future','Label'], axis=1)
#print(housing_data.head())

X = np.array(house)
X = preprocessing.scale(X)
y = np.array(housing_data['Label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))

