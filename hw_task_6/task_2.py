"""
2.	Поместите построенную модель в класс
a.	все гипер параметры принимаются при инициализации
b.	методы:
i.	подготовка данных
ii.	обучение
iii.	инференс (прямой проход сети по обученным весам)
"""

import numpy as np
from keras.models import Sequential
from keras.layers import Dense

class Keras_model:
    def __init__(self, layer_1, layer_2, layer_3, input, epochs, batch_size, verbose):
        self.X = None
        self.Y = None
        self.dataset = None
        self.model = Sequential()
        self.set_hyperparameters(layer_1, layer_2, layer_3, input, epochs, batch_size, verbose)
    def set_hyperparameters(self, layer_1, layer_2, layer_3, input, epochs, batch_size, verbose):
        self.epochs = epochs
        self.batch_size = batch_size
        self.verbose = verbose
        self.layer_1 = layer_1
        self.layer_2 = layer_2
        self.layer_3 = layer_3
        self.input = input

    def set_data(self,datapath):
        self.datapath = datapath

    def prepare_dataset(self):
        self.dataset = np.genfromtxt(self.datapath, delimiter=',', dtype=float)
        self.X = self.dataset[:, :8]
        self.Y = self.dataset[:, -1]

    def learn(self):
        self.model.add(Dense(self.layer_1, input_dim=self.input, activation='relu'))
        self.model.add(Dense(self.layer_2, activation='relu'))
        self.model.add(Dense(self.layer_3, activation='sigmoid'))
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.model.fit(self.X, self.Y, epochs=self.epochs, batch_size=self.batch_size, verbose=self.verbose)

    def predict(self, X):
        return self.model.predict(X)