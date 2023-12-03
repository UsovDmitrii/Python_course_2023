"""
2.	Сделайте предсказание выживаемости пассажира,
на основе датасета “titanic.csv”, с использованием библиотеки sklearn.
Сделайте тестовый проход на 10 пассажирах.
"""
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

np.set_printoptions(precision=2, floatmode='fixed', suppress=True)
data = pd.read_csv('titanic.csv')
data = data.dropna()

X_train = np.array(data["Age"]).reshape(-1,1)
Y_train = np.array(data["Survived"]).reshape(-1,1)

X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train,test_size = 10, shuffle=True)

model = svm.SVC()
model.fit(X_train, Y_train)

predicted  = model.predict(X_test)
X_test = X_test.reshape(1,-1)
Y_test_out = Y_test.reshape(1,-1)
print(f'Вход\n{X_test}')
print(f'Данные\n{Y_test_out}')
print(f'Предсказания\n{predicted}')