# %%
import pandas as pd
import numpy as np

df = pd.read_csv('../Day01/FoodPrice_in_Turkey.csv')

    #Xac dinh kich thuoc df
df.shape
print("So hang: ", df.shape[0])
print("So cot: ",df.shape[1])
df.head()

url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_North_America'
df3 = pd.read_html(url)
df3[0].head()
# %%
import pandas as pd
import numpy as np
df2 = pd.read_excel('../Day01/Loan.xlsx')

df2.shape
df2.head()
# %%
