"""
7.	Напишите функцию которая
a.	Принимает два параметра (диапазон дат)
b.	Создайте DataFrame из файла BCT-USD.csv
c.	Строит графики по столбцам “Open” и “Close” за диапазон даты из параметров
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('BCT-USD.csv')
df['Date'] = df['Date'].astype("datetime64[ns]")
def graph_plot(df,start,finish):
    start = pd.to_datetime(start)
    finish = pd.to_datetime(finish)

    res = df[(df['Date'] >= start) & (df['Date'] <= finish)]
    plt.plot(res['Date'], res['Open'], label='Open')
    plt.plot(res['Date'], res['Close'], label='Close')
    plt.show()

start = '2021-10-21'
finish = '2021-12-03'
graph_plot(df,start,finish)
