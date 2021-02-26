#%%
import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm,skewnorm, lognorm
#%matplotlib inline
# %%
# This is data of dice rolled. We want to test if this dice is fair or not.
dicedata = pd.read_csv("loaded_500.txt",header=None)
# %%
dicedata.describe()

# %%
sns.displot(data=dicedata)
# %%
dicedata.value_counts()/dicedata.size
# %%
materdata= pd.read_csv("Meteorite_Landings.csv")
# %%
materdata.head()
# %%
materdata.describe().transpose()
# %%
materdata.info()
#%%
materdata.isnull().sum()
# %%
sns.countplot(data=materdata, x='nametype')
# %%
sns.countplot(data=materdata, x='recclass')
# %%
materdata['fall'].unique()
# %%
sns.countplot(data=materdata, x='fall')
# %%
sns.countplot(data=materdata, x='year')
# %%
materdata['year'].unique()
#%%
materdata['year'].value_counts()
#%%
# %%
limiteddata = materdata[(materdata['year']>1900)& (materdata['year']<2020)]
sns.displot(data=limiteddata, x='year')

# %%
# null values for year and mass will make prediction very difficult
df = materdata.dropna(subset=['mass', 'year'])
# remove entries with 0 mass
df=df[df['mass']>0]
df.info()
# %%

sns.countplot(data=df[(df['year']>1970)], x='year')
# %%
df['logmass']=np.log(df['mass'])
# %%
sns.displot(data=df['logmass'])
# %%
# mean and std of logmass
mn , std= df['logmass'].mean(), df['logmass'].std()
pdf_np = np.random.normal(loc=mn, scale=std, size=45292)
# %%
# Overlay of multiple histograms - check how actual vs ideal distribution
sns.displot([pdf_np,df['logmass']])
# %%
fig=plt.figure()
axes = fig.add_axes([0.8,0.8,0.8,0.8])
asteroid = np.log(10000000)
axes.hist(df['logmass'], bins=100)
axes.hist(pdf_np, bins=100)
axes.axvline(asteroid)
# %%
