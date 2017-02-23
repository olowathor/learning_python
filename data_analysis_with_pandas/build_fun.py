import quandl
import pandas as pd

api_key = str(open('quandlapikey.txt','r').read()).split("'")[1]

df = quandl.get('FMAC/HPI_AK',authtoken=api_key)

print(df.head())
