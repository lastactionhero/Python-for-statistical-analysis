#%%
import pandas as pd
import numpy as np
import seaborn as sns
#%%
dsDiabetes = pd.read_csv('Diabetes.csv')
# %%
dsDiabetes.head()
# %%
dsDiabetes.info()
# if there are null values then use dsdiabetes.fillna(0)
# %%
dsDiabetes.describe().transpose()
# %%
sns.pairplot(dsDiabetes)
# %%
# Drop null value rows use ds.dropna() but in this case we can see value '0' is unacceptable or equivalent to 0
# Column which can have valid 0 value are 
# Pregnancies, DiabetesPedigreeFunction, Outcome, Glucose,SkinThickness
NotMin0Ds= dsDiabetes[['BloodPressure', 'BMI', 'Glucose']]

#%%
#If any value is 0, it means we can not trust that data
RowsWith0Data = (NotMin0Ds==0).any(axis=1)
# %%
# Remove data from dataset which has 0 for BMI, Blood pressure or Glucose
dsDiabetes = dsDiabetes.loc[~RowsWith0Data]
# %%
dsDiabetes.describe().transpose()
# %%
# Lets look into data based on outcome
dsDiabetes.groupby('Outcome').mean()
# %%
dsDiabetes.groupby('Outcome').agg({"Glucose":"mean", "BMI":"median", "Pregnancies":"sum", "SkinThickness":"min"})
# %%
dsDiabetes.groupby('Outcome').agg({"mean", "median"})
#%%
sns.heatmap(dsDiabetes.corr())
# %%
# create positive and negative datasets based on outcome
negative = dsDiabetes[dsDiabetes['Outcome']==0]
positive = dsDiabetes[dsDiabetes['Outcome']==1]
# %%
negative.describe()
# %%
positive.describe()
# %%
dsDiabetes.to_csv('clean_diabetes.csv', index=False)
# %%
