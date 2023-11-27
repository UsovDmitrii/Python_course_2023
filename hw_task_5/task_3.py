"""
3.	Создайте DataFrame с рандомными числами, размером 10х10.
a.	добавьте индексы столбцов и строк в виде латинских букв
b.	Выведите в консоль
i.	Размерность матрицы
ii.	индексы столбцов
iii.	среднее значение всех чисел матрицы
iv.	запишите матрицу в csv

"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,10,size=(10,10)), index = list('abcdefghik'), columns= list('abcdefghik'))
print(f'Размерность матрицы {df.shape}')
print(f'Индексы столбцов {df.columns.array}')

df.to_csv('res_of_task_3')

