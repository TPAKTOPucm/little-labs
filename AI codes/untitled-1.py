import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Work 1

data = pd.read_csv("real_estate.csv")
#print(data)
#print(data.isnull().sum())

#Work 2

columns = ['Transact Date','Age','Distance To Transport','Shops','Latitude','Longitude','Price']

for col in columns:
   data[col].head(100).plot()
   plt.show()
   sns.lineplot(data=data[col].head(100))
   plt.show()

#Work 3

for col in columns:
    data[col].plot(kind="hist")
    plt.show()
    diag = sns.histplot(x=data[col])
    plt.show()