""""
9.	* Создайте DataFrame из файла BCT-USD.csv
a.	Выведите в консоль месяцы за которые зена при закрытия в конце месяца была выше цены открытия на начало месяца
b.	Если таких нет выведите соответствующее сообщение

"""

import pandas as pd

df = pd.read_csv('BCT-USD.csv')
df['Date'] = df['Date'].astype("datetime64[ns]").dt.month

filtered_df = df[df['Close'] > df['Open']]
months = filtered_df['Date'].unique()

if len(months) > 0:
    res = "Месяцы за которые зена при закрытия в конце месяца была выше цены открытия на начало месяца: "
    for month in months:
        res = res + str(month)+","
else:
    res = "Таких месяцев нет"
print(res)