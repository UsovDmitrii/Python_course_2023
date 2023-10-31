"""
8.	Постройте класс для анализа файла с данными:
a.	У класса есть константа - путь к файлу при инициализации
b.	Скопируйте готовый DataSet, будет прикреплен к ДЗ
c.	В файле представлен публичный набор данных с информацией о наблюдениях НЛО.
d.	Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
e.	Создайте метод который возвращает страну в которой больше всего наблюдений.
f.	Создайте метод который возвращает месяц за который чаще всего появлялись объекты НЛО

"""

import numpy as np
import pandas as pd


class Data_analizer():
    file_path = 'nlo.csv'

    def read_file(self):
        self.data = pd.read_csv(Data_analizer.file_path, on_bad_lines='skip', low_memory=False)
        self.data['datetime'] = pd.to_datetime(self.data['datetime'], errors='coerce')
        return True

    def most_visited_country(self):
        country_data = self.data.groupby('country')['country'].count()
        country_data = country_data.sort_values()
        return country_data.idxmax()

    def most_visited_month(self):
        self.data["month"] = self.data["datetime"].dt.month
        month_data = self.data.groupby('month')['month'].count()
        month_data = month_data.sort_values()
        return month_data.idxmax()


Dataset = Data_analizer()
Dataset.read_file()
print(Dataset.most_visited_country())
print(Dataset.most_visited_month())
