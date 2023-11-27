"""
6.	Напишите функцию которая
a.	принимает строку - название категории
b.	проверяет есть ли такая категория в наборе данных emojis.csv
c.	возвращает сколько процентов эмоджи сделано по этой категории (пример: 10%). Или сообщение об отсутствии категории в наборе данных.

"""

import pandas as pd

df = pd.read_csv('emojis.csv')
def category_counter(df,category):
    group_data = df.groupby('Category').count()
    emoji_count = df.count().iloc[0]
    if category in group_data.Name:
        x = group_data.loc[category].iloc[0]
        return x/emoji_count
    else:
        raise Exception('Datasest not have given categiry')

print(category_counter(df,'People & Body'))
print(category_counter(df,'People'))
