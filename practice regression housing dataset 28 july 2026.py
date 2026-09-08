import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv




df= pd.read_csv('housing.csv', delimiter=',')

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

df.plot.scatter(x='total_rooms',y='population', title='Scatter Plot of total_rooms and population');
plt.show()

y = df['population'].values.reshape(-1, 1)
x = df['total_rooms'].values.reshape(-1, 1)

print("y :   " , y)
print("X :   " , x)

SEED = 115

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = SEED)

print(X_train)
print(y_train)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()


regressor.fit(X_train, y_train)
    
print(regressor.intercept_)
print(regressor.coef_)

def ehti(slope, intercept, total_rooms):
    return slope*intercept

score = ehti(regressor.coef_, regressor.intercept_, 919)
print(score)

score = regressor.predict([[30]]) 
print(score)     


y_pred= regressor.predict(X_test)

df_preds = pd. DataFrame({'Actual' :y_test.squeeze(),'Predicted': y_pred.squeeze()})
print(df_preds)











from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse= mean_squared_error(y_test, y_pred)
rmse= np.sqrt(mse)

r2 = r2_score(y_test, y_pred)


print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')








