"""
5.	Создайте DataFrame из файла emojis.csv. 
a.	Получите количество созданных эмоджи за каждый год
b.	Постройте график
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('emojis.csv')
group_data = df.groupby('Year').count()

plt.plot(group_data['Emoji'])
plt.show()