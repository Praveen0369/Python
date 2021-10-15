import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.pyplot as plt
df=pd.read_csv("/content/india-gdp-per-capita.csv")
df#display data set
reg = linear_model.LinearRegression()
reg.fit(df[['date']],df.gdp)
dt=0.01
Y=(df[['gdp']])
pr=reg.predict(Y)
%matplotlib inline
plt.subplot(111)
plt.plot(df.date,pr)
