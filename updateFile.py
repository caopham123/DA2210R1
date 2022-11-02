#%%
import pandas as pd
import numpy as np

df = pd.read_csv('FoodPrice_in_Turkey.csv')
df.head(10)

    ##DOI TEN COLUMN
df.rename(columns={'Place':'Dia diem','Month':'Thang','Year':'Nam','Price':'Gia' },inplace=True)
print(df.head(10))

    ##THEM COLUMN
df['Giam gia'] = pd.Series('10%', index=df.index)

df.insert(3, 'Tinh trang', pd.Series('Con hang',index=df.index))

   ##THEM HANG
df = df.append({'Dia diem':'US','ProductId':'50','ProductName':'ac','Tinh trang':'Het hang',
           'UmId':10,'UmName':'Kg','Thang':'12','Nam':'2022','Gia':'10','Giam gia':'20%'},ignore_index=True)

# df.tail(15).to_csv('demo.csv')

    ##XOA COT
# df = df.pop('Giam gia')

df.drop(['ProductName', 'ProductId'], axis=1, inplace=True)

    ##XOA HANG
df.drop(5,axis=0, inplace=True)
df = df.head()
df.to_csv('demo.csv')
# %%
