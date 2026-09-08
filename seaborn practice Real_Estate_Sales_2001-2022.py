import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df =pd.read_csv("Real_Estate_Sales_2001-2022_GL-Short.csv", delimiter=",")
print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)

sns.set(style="whitegrid")

g=sns.displot(data=dffilter, x="Serial Number", y="List Year", kind='hist')
g.figure.suptitle("sns.displot(data=dffilter, x=Serial Number, y=List Year, kind='hist')")
g.figure.show()
read = input("Wait: ")



g=sns.kdeplot(data=dffilter, x="List Year")
g.figure.suptitle("sns.kdeplot(x=List Year, data=dffilter)")
g.figure.show()
read = input("Wait: ")


g=sns.histplot(data=dffilter, x="Serial Number", y="List Year")
g.figure.suptitle("sns.histplot(data=dffiltor, x=Serial Number, y=List Year)")
g.figure.show()
read = input("Wait: ")



g=sns.scatterplot(data=dffilter, x="List Year", y="Serial Number")
g.figure.suptitle("sns.scatterplot(data=dffilter, x=List Year, y=Serial Number)")
g.figure.show()
read = input("Wait: ")



g=sns.lineplot(data=dffilter, x="Serial Number", y="List Year")
g.figure.suptitle("sns.lineplot(data=dffilter, x=Serial Number, y=List Yeare)")
g.figure.show()
read = input("Wait: ")


g=sns.barplot(data=dffilter, x="List Year", y="Serial Number")
g.figure.suptitle("sns.barplot(data=dffilter, x=List Year, y=Serial Number)")
g.figure.show()
read = input("Wait: ")



g=sns.catplot(data=dffilter, x="Serial Number", y="List Year")
g.figure.suptitle("sns.catplot(data=dffilter, x=Serial Number, y=List Year)")
g.figure.show()
read = input("Wait: ")



