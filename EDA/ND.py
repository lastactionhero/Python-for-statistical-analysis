#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %%
diabetes = pd.read_csv("Diabetes.csv")
#%%
diabetes.info()
#%%
# lets remove cols which we done need in analysis
cols = [c for c in diabetes.columns if c not in ['Outcome', 'Pregnancies']] 
ds = diabetes[cols]
#%%
# if there are 0s and we dont want them to be calculated for sum, avg etc. then replace it with NAN
ds[cols] = ds[cols].replace(to_replace=0, value=np.NaN)
#%%
ds.describe().transpose()
#%%
sns.pairplot(data=diabetes,hue='Outcome')
# %%
sns.heatmap(diabetes.corr())
# %%
hw = pd.read_csv("height_weight.csv")
# %%
hw.head()
# %%
hw.describe()
# %%
sns.jointplot(data=hw,x='height',y='weight',hue='sex')
# %%
sns.jointplot(data=hw,x='height',y='weight',hue='sex',kind='kde')

# %%
sns.jointplot(data=hw,x='height',y='weight',kind='hex')

# %%
