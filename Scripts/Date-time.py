# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:01:59 2016

@author: swamy
@Topic: Data Analysis with Pandas
"""
import pandas as pd
import datetime
import pandas.io.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
sns.set(style="ticks")
style.available
#style.use('twentytwo')

start = datetime.datetime(1991, 3, 17)
end= datetime.datetime.today()
#print()
df = web.DataReader("XOM","yahoo",start,end)
print(df.head())
print(df.tail())
df['High'].plot()
plt.legend()
plt.show()
grid = sns.FacetGrid(df['High'], hue="walk", col_wrap=5, size=1.5)

