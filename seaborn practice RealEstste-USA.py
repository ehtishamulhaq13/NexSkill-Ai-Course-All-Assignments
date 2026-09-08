import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


# Load data from a CSV file
df = pd.read_csv('RealEstate-USA.csv',delimiter=",")
print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)

sns.set(style="whitegrid")

#kind='hist'  
g=sns.displot(data=dffilter, x="price" , y="bed" , hue="zip_code",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=price , y=bed, hue=zip_code,  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()



g=sns.displot(data=dffilter, x="price" ,   kind='kde')
g.figure.suptitle("sns.displot(data=dffilter, x=price , y=date_added , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.kdeplot(data=dffilter, x="price")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)" )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g = sns.histplot(data=dffilter, x='price', y='bed', hue='price', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='price', y='bed', hue='price', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g=sns.lineplot(data=dffilter, x="price" , y="bed"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=price , y=bed  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.barplot(data=dffilter, x="price", y="bed", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=price, y=bed, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g=sns.catplot(data=dffilter, x="price", y="bed")
g.figure.suptitle("sns.catplot(data=df, x=price, y=bed)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()

#.pivot(index="Model", columns="agency", values="price")
glue = dffilter.pivot(columns="price", values="bed")


g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=price, values=bed)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()