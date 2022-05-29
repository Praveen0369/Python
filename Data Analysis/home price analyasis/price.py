import numpy as np


import pandas as pd

import matplotlib.pyplot as plt

%matplotlib inline

plt.rcParams['figure.figsize']=(10.0,8.0)

from scipy import stats
from scipy.stats import norm

from sklearn import linear_model

df=pd.read_csv("/content/clean_data.csv")
df.head()

df.info()
df.columns[df.isnull().any()]

miss = df.isnull().sum()/len(df)

miss = miss[miss > 0]
miss.sort_values(inplace=True)
miss

miss = miss.to_frame()
miss.columns = ['count']
miss.index.names = ['Name']
miss['Name'] = miss.index

pip install seaborn

sns.set(style="whitegrid", color_codes=True)
sns.barplot(x = 'Name', y = 'count', data=miss)
plt.xticks(rotation = 90)
sns.plt.show()

sns.distplot(df['price'])
