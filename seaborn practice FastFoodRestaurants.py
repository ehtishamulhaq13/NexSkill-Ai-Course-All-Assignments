import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("FastFoodRestaurants.csv", delimiter=",")
print(df.dtypes)
dffilter=df.head(40)
dffilter100=df.head(100)

sns.set(style="whitegrid")

g=sns.displot(data=dffilter, x="postalCode", y="latitude", kind='hist')
g.figure.suptitle("sns.displot(data=dffilter, x=postalCode, y=latitude, kind='hist')")
g.figure.show()
read = input("Wait: ")



g=sns.kdeplot(data=dffilter, x="latitude")
g.figure.suptitle("sns.kdeplot(x=latitude,data=dffilter)")
g.figure.show()
read = input("Wait: ")


g=sns.histplot(data=dffilter, x="postalCode", y="latitude")
g.figure.suptitle("sns.histplot(data=dffiltor, x=postalCode, y=latitude)")
g.figure.show()
read = input("Wait: ")



g=sns.scatterplot(data=dffilter, x="longitude", y="latitude")
g.figure.suptitle("sns.scatterplot(data=dffilter, x=longitude, y=latitude)")
g.figure.show()
read = input("Wait: ")



g=sns.lineplot(data=dffilter, x="postalCode", y="latitude")
g.figure.suptitle("sns.lineplot(data=dffilter, x=postalCode, y=latitude)")
g.figure.show()
read = input("Wait: ")


g=sns.barplot(data=dffilter, x="postalCode", y="latitude")
g.figure.suptitle("sns.barplot(data=dffilter, x=postalCode, y=latitude)")
g.figure.show()
read = input("Wait: ")



g=sns.catplot(data=dffilter, x="postalCode", y="latitude")
g.figure.suptitle("sns.catplot(data=dffilter, x=postalCode, y=latitude)")
g.figure.show()
read = input("Wait: ")



g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue) - glue = dffilter.pivot(coloumns=postalCode, values=latitude)" )
g.figure.show()
read = input("Wait: ")
