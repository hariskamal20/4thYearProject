import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import seaborn as sns
import warnings
warnings.filterwarnings("ignore",category=UserWarning)

#Time Series Analysis
plt.style.use('fivethirtyeight')
# Above is a special style template for matplotlib, highly useful for visualizing time series data
from pylab import rcParams
rcParams['figure.figsize'] = 20, 10
df = pd.read_csv('timeSeriesIrelandCon.csv')
df.columns=['Year', 'Electric power consumption']
df=df.dropna()
df['Year'] = pd.to_datetime(df['Year'])
df.set_index('Year', inplace=True) #set date as index
#df.head()
plt.xlabel("Year")
plt.ylabel("Electric power consumption")
plt.title("Consumption graph")
plt.plot(df)
df.plot(style='k.')
plt.savefig('static/ts.png')
