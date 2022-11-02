import pandas as pd

data = pd.read_csv('subset-covid-data.csv')
data.info()  #data.shape
data.date.value_count()

cleaned_data = data[data.date == '2020-04-12']
# Vẽ biểu đồ phân bố số lượng ca mắc mới ở các quốc gia
print ("trung bình số ca mắc mới: " + str(cleaned_data.cases.mean()))
print ("trung vị của số ca mắc mới: "+ str(cleaned_data.cases.median()))
import matplotlib.pyplot as plt
plt.hist(cleaned_data.cases, bins = 200)
plt.title("Phân bố số ca mắc mới")
plt.xlabel("số số ca mắc mới")
plt.ylabel("Số lượng quốc gia")
# trung bình số ca mắc mới: 376.8186274509804
# trung vị của số ca mắc mới: 11.5
# Text(0, 0.5, 'Số lượng quốc gia')

print ("5 quốc gia có số ca nhiễm mới cao nhất")
data = data.sort_values('cases',ascending = False)
data.head(5)

print ("5 quốc gia có số ca tử vong cao nhất")
data = data.sort_values('deaths',ascending = False)
data.head(5)

