import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import matplotlib.pyplot as plt
df=pd.read_csv("/content/readme.csv")
df#prints data
%matplotlib inline
plt.scatter(df.area,df.price,color='red',marker='^')
reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
#----Main-----#
%matplotlib inline
plt.scatter(df.area,df.price,color='red',marker='^')
plt.plot(df.area,reg.predict(df[['area']]),color='blue')
