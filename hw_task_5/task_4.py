"""
4.	Создайте DataFrame из файла emojis.csv.
a.	в столбце Rank указан рейтинг смайлов, отсортированный в порядке убывания частоты. (чем чаще использовался эмоджи тем ниже значение)
b.	Выведите в консоль самую популярную подкатегорию эмоджи

"""

import pandas as pd
import numpy as np

df = pd.read_csv('emojis.csv')
group_data_m = df.groupby('Subcategory').mean()
group_data_m = group_data_m.sort_values('Rank')
print('Most popular category is:',group_data_m.index[0])
