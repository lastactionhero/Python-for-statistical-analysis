#%%
import matplotlib as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy.stats import pearsonr 
#%%
junkfooddf = pd.read_csv('junkfood.csv')
#%%
junkfooddf.head(10)
#%%
junkfooddf.isnull().sum()
# %%
junkfooddf.info()
# %%
junkfooddf.groupby(by='Food').sum()
# %%
sns.displot(data=junkfooddf, x='Acne', hue='Food',palette='inferno')
#%%
sns.displot(data=junkfooddf, x='Frequency', hue='Food',palette='inferno')
# %%
sns.jointplot(data=junkfooddf, x='Acne', y='Frequency', hue='Food', xlim=(-1,17),ylim=(-1,40) ,palette='magma')
# %%
sns.set_theme(palette='inferno')
grid = sns.FacetGrid(data=junkfooddf, row='Food')
grid.map(sns.scatterplot, 'Acne', 'Frequency')

#%%
junkfooddf.corr()
#%%
junkfooddf.groupby(by='Food').corr()
#%%
sns.heatmap(junkfooddf.groupby(by='Food').corr())

# %%
# Null Hypothesis: Frequency of junk food does not corelate with acne. 
corr, pvalue = pearsonr(junkfooddf['Acne'],junkfooddf['Frequency'])
print (f'pvalue - {pvalue} and correlation - {corr} ')
# result - Fail to reject null hypothesis
# %%
# lets see correlation for each food type
for food in junkfooddf['Food'].unique():
    df = junkfooddf[junkfooddf['Food']==food]
    corr, pvalue = pearsonr(df['Acne'], df['Frequency'])
    print(f'{food} ---> Correlation - {corr:0.2f} and pvalue - {pvalue:0.2f} ' )
# %%
# For cake - We reject null hypothesis