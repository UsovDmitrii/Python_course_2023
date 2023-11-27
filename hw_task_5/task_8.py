""""
Создайте DataFrame из файла BCT-USD.csv
a.	выведите в консоль месяц за который был самый маленький объем (Volume)
"""

import pandas as pd
df = pd.read_csv('BCT-USD.csv')
df['Date'] = df['Date'].astype("datetime64[ns]")

res = df.sort_values(by='Volume')
print(res['Date'][0].month)