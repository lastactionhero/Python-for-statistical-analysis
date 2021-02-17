#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %%
# This is data of dice rolled. We want to test if this dice is fair or not.
dicedata = pd.read_csv("loaded_500.txt",header=None)
# %%
dicedata.describe()
# %%
sns.displot(data=dicedata)
# %%
dicedata.value_counts()
# %%
