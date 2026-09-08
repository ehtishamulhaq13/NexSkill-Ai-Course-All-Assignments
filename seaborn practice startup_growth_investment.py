import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df =pd.read_csv("startup_growth_investment_data.csv", delimiter=",")
print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)

sns.set(style="whitegrid")

g=sns.displot(data=dffilter, x="Funding Rounds", y="Number of Investors", kind='kde')
g.figure.suptitle("sns.displot(data=dffilter, x=Funding Rounds, y=Number of Investors, kind='kde')")
g.figure.show()
read = input("Wait: ")



g=sns.kdeplot(data=dffilter, x="Year Founded",)
g.figure.suptitle("sns.kdeplot(data=dffilter, x=Year Founded)")
g.figure.show()
read = input("Wait: ")





g=sns.histplot(data=dffilter, x="Year Founded", y="Funding Rounds")
g.figure.suptitle("sns.histplot(data=dffilter, x=Year Founded, y=Funding Rounds)")
g.figure.show()
read = input("Wair: ") 






g=sns.scatterplot(data=dffilter, x="Number of Investors", y="Year Founded")
g.figure.suptitle("sns.scatterplot(data=dffilter, x=Number of Investors, y=Year Founded)")
g.figure.show()
read = input("Wait: ")




g=sns.lineplot(data=dffilter, x="Funding Rounds", y="Year Founded")
g.figure.suptitle("sns.lineplot(data=dffilter, x=Funding Rounds, y=Year Founded)")
g.figure.show()
read = input("Wait: ")





g=sns.barplot(data=dffilter, x="Year Founded", y="Number of Investors")
g.figure.suptitle("sns.barplot(data=dffilter, x=Year Founded, y=Number of Investors)")
g.figure.show()
read = input("Wait: ")




g=sns.catplot(data=dffilter, x="Number of Investors", y="Year Founded")
g.figure.suptitle("sns.scatterplot(data=dffilter, x=Number of Investors, y=Year Founded)")
g.figure.show()
read = input("Wait: ")


