import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv


df = pd.read_csv('bank.csv')
print(df)
print("data type of cvs", df.dtypes)
print()
print("info of csv", df.info())
print()
print("shape of the dataset", df.shape)
print()





y = df['loan'].map({'yes': 1, 'no': 0})
x = df[['age','balance','housing','duration','day','contact','education','month']]

x['housing'] = x['housing'].map({'yes': 1, 'no': 0})
x = pd.get_dummies(x, columns=['contact', 'education', 'month'], drop_first=True)


print("y :   " , y)
print("X :   " , x)

SEED = 115

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = SEED)




from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


print(X_train)
print(y_train)

from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier(random_state=SEED, max_iter=500)

classifier.fit(X_train_scaled, y_train)

print(classifier.hidden_layer_sizes)
print(classifier.alpha)



y_pred = classifier.predict(X_test_scaled)
score = classifier.score(X_test_scaled, y_test)
print("Accuracy:", score)






y_pred= classifier.predict(X_test_scaled)

df_preds = pd. DataFrame({'Actual' :y_test.squeeze(),'Predicted': y_pred.squeeze()})
print(df_preds)