#%%
import pandas as pd
import numpy as np

df = pd.read_csv('FoodPrice_in_Turkey.csv')
df2 = df.head()
print(df2)
df2.to_csv("demoFile.csv")

# %%
