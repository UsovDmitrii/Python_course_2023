"""
3.	* постройте цикличный подбор гипер параметров
a.	параметры:
i.	кол-во нейронов на первом слое от 5 до 15 с шагом 1
ii.	кол-во нейронов на втором слое от 4 до 10 с шагом 1
iii.	кол-во эпох от 10 до 50 с шагом 5
iv.	размер батча от 10 до 50 с шагом 5
b.	Нейросеть должна обучиться и сделать инференс с каждым вариантом наборов параметров из представленного списка.
c.	На каждый набор параметров запустите инференс 3 раза
d.	при каждом запуске результат работы сети должен сохраняться в файл. В тот же файл сохранять набор параметров текущего запуска - название параметра и его текущее значение..
e.	Для каждого набора параметров должен создаваться свой файл.
"""

import numpy as np
import task_2 as model

neural = model.Keras_model(5, 4, 1, 8, 10, 10, 2)
neural.set_data('data.txt')
neural.prepare_dataset()
test_batch = neural.X

for layer_1 in range(5, 16):
    for layer_2 in range(4, 11):
        for epochs in range(10, 50, 5):
            for batch_size in range(10, 50, 5):
                neural.set_hyperparameters(layer_1, layer_2, 1, 8, epochs, batch_size, 2)
                neural.learn()

                with open (f'./res/out {layer_1}-{layer_2}-{epochs}-{batch_size}.txt', "a+") as f:
                    f.write(f'Parameter: layer 1 = {layer_1}, layer_2 = {layer_2}, epochs = {epochs}, batch_size = {batch_size}\n')
                    for i in range(3):
                        f.write(f'{neural.predict(test_batch[:5])}\n\n')