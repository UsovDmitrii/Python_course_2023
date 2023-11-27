"""
2.	В DataFrame из предыдущего задания добавьте индексы строк в виде латинских букв.
Выведите на печать строку в которой все числа > 5, если такая есть
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,10,size=(10,10)))
df.index = list('abcdefghik')
for rov in df:

    flag = True
    for num in df[rov]:

        if num <=5:
            flag = False
    if flag == True:
        print(df[rov])
print(df)