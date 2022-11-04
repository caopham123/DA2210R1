#%%
import pandas as pd   

#DOC FILE
data = pd.read_csv('../Demo/OnlineRetail.csv',encoding='ISO-8859-1') 
# print(data.head(10))

print("Cot: {}   Hang: {}".format(data.shape[1], data.shape[0]))
# print("Thong tin Du lieu:\n",data.info())

##Cot CustomerID co gia tri khac Null tu 0-406829
##InvoiceNo, StockCode, Description, InvoiceDate, country: là thuộc tính định tính, có thang đo định danh

##  CONG TY BAN HANG CHO BAO NHIEU QG
Country = pd.unique(data['Country'])
print('DS quoc gia:\n',Country, end='\n')
total_Country = Country.size
print("Tong so QG: ", total_Country)

##  SO DON BAN RA VA TONG DOANH THU
data['Total'] = data['Quantity'] * data['UnitPrice']

total_invoices = data['Total'].sum()
print('So don ban ra: ', total_invoices.size)
print('Tong Doanh thu: ', total_invoices.sum())

# list_Product = pd.unique(data['StockCode'])
# total_Product = list_Product.size
# print(total_Product)

##  SO LUONG BAN RA LON NHAT
num_product = data.groupby(['StockCode', 'Description']) ['Quantity'].sum().sort_values(ascending=False)
print('Top 10 SP ban chay:\n', num_product.head(10), end='\n')
# %%
