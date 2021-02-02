#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %%
ds1 = pd.read_csv("example_1.txt",names=['value'])
ds2 = pd.read_csv("example_2.txt",names=['value'])
#%%
ds1['type']="A"
ds2['type']="B"
#%%
ds1.info()
#%%
ds1.head()
#%%
ds2.head()

# %%
ds= ds1.append(ds2)
#%%
ds.head()
# %%
sns.displot(data=ds, x= 'value', hue='type')
# %%
sns.swarmplot(data=ds,x='value', y='type')
# %%
sns.boxplot(data=ds,x='value', y='type')

# %%
sns.violinplot(data=ds,x='value', y='type', inner='quartile')

