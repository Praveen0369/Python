import pandas as pd



df=pd.read_csv("/content/clean_data.csv")

df.head()

df.info()

#Trying To Clear Out Nulls Or Finding Nulls

df.isna().sum().sum()

df[df.columns[df.isna().any()]].isna().sum()

df.isna().sum().plot(kind='hist')

threshold = 800
print(f"Columns with greater than {threshold} NaNs, {round((threshold/df.shape[0]) * 100)}% of it's values are NaNs.")

outliers=df.isna().sum()[df.isna().sum()>threshold]

outliers

del df['delete colum which is highly empty']

df.pop('delete colum which is highly empty')

df.isna().sum().plot(kind='hist')

#checking for duplicates

df.duplicated().sum()

#output

df.describe()
