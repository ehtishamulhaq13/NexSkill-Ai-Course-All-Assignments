import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

df= pd.read_csv('insurance.csv', delimiter=',')


print(df)
print("data type of cvs", df.dtypes)
print()
print("info of csv", df.info())
print()
print("shape of the dataset", df.shape)
print()

print("last three rows:")
print(df.tail(3))


print("first three rows:")
print(df.head(3))
print()

df.plot.scatter(x='age',y='charges', title='graph of age and charges');
plt.show()

y = df['age'].values.reshape(-1, 1)
x = df['charges'].values.reshape(-1, 1)

print("y :   " , y)
print("X :   " , x)

SEED = 225

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = SEED)


print(X_train)
print(y_train)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()


regressor.fit(X_train, y_train)
    
print(regressor.intercept_)
print(regressor.coef_)

def ehti(slope, intercept, age):
    return slope*intercept

score = ehti(regressor.coef_, regressor.intercept_, 285)
print(score)

score = regressor.predict([[40]]) 
print(score)

y_pred= regressor.predict(X_test)

df_preds = pd. DataFrame({'Actual' :y_test.squeeze(),'Predicted': y_pred.squeeze()})
print(df_preds)













