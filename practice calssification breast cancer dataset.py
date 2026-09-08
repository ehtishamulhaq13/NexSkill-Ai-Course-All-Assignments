import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

df = pd.read_csv('data.csv')
print(df)
print("data type of cvs", df.dtypes)
print()
print("info of csv", df.info())
print()
print("shape of the dataset", df.shape)
print()

df.plot.scatter(x='radius_mean', y='diagnosis', title='Scatter Plot of radius_mean and diagnosis');
plt.show()

df.plot.scatter(x='area_mean', y='diagnosis', title='Scatter Plot of area_mean and diagnosis');
plt.show()

df.plot.scatter(x='symmetry_mean', y='diagnosis', title='Scatter Plot of symmetry_mean and diagnosis');
plt.show()

df.plot.scatter(x='perimeter_se', y='diagnosis', title='Scatter Plot of perimeter_se and diagnosis');
plt.show()



y = df['diagnosis']
x = df[['radius_mean','area_mean','symmetry_mean','perimeter_se']]

print("y :   " , y)
print("X :   " , x)

SEED = 115

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = SEED)

print(X_train)
print(y_train)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()

classifier.fit(X_train, y_train)

print(classifier.n_estimators)
print(classifier.max_depth)


y_pred = classifier.predict(X_test)
score = classifier.score(X_test, y_test)
print("Accuracy:", score)


score = (classifier.max_depth, classifier.n_estimators, 225)
print(score)

score = (classifier.max_depth, classifier.n_estimators, 155)
print(score)

score = (classifier.max_depth, classifier.n_estimators, 413)
print(score)

score = (classifier.max_depth, classifier.n_estimators, 365)
print(score)

score = classifier.predict([[90,50,100,150]])
print(score) 


y_pred= classifier.predict(X_test)

df_preds = pd. DataFrame({'Actual' :y_test.squeeze(),'Predicted': y_pred.squeeze()})
print(df_preds)