"""
9.	Постройте класс для анализа файла с данными:
a.	У класса есть константа - путь к файлу при инициализации
b.	Скопируйте готовый DataSet, будет прикреплен к ДЗ
c.	В файле представлен публичный набор данных - 5000 инструментов искусственного интеллекта
d.	Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
e.	Создайте метод который возвращает ответ на вопрос - на какой тип инструмента платный или бесплатный чаще оставляют обзор (Review)
* Бесплатным считаем только полностью бесплатный инструмент (Free)
f.	Создайте метод, который возвращает категорию задач (Useable For) для которой больше всего бесплатных инструментов
g.	Создайте метод возвращающий топ 3 инструмента по запросу. Параметры запроса:
i.	Платный или бесплатный - добавить возможность сортировки.
ii.	задачи - (поиск искомой подстроки в результирующей строке)
iii.	Основная категория - (поиск искомой подстроки в результирующей строке)

По умолчанию параметры необязательные и не должны влиять на выборку.
"""
import pandas as pd
import numpy as np
class Data_analizer():
    file_path = 'all_ai_tool.csv'

    def read_file(self):
        self.data = pd.read_csv(Data_analizer.file_path, on_bad_lines='skip', low_memory=False)
        self.data['Review'] = pd.to_numeric(self.data['Review'],errors='coerce')
        return True
    def most_rewiewed_group(self):
        res = ''

        data_group = self.data.groupby('Free/Paid/Other')
        data_2 = self.data.dropna()

        free_soft_count = len(data_group.groups['Free'])
        free_soft_review_count = self.data.groupby('Free/Paid/Other')['Review'].sum()['Free']
        free_soft_rev_index = free_soft_review_count/free_soft_count

        not_free_soft_count = self.data.count()['AI Tool Name'] - free_soft_count
        not_free_soft_review_count = self.data.sum()['Review'] - free_soft_review_count
        not_free_soft_rev_index = not_free_soft_review_count/not_free_soft_count
        if free_soft_rev_index > not_free_soft_rev_index:
            res = 'Бесплатный софт получет больше обзоров,{:.2f} обзора на программу'.format(free_soft_rev_index)
        elif free_soft_rev_index < not_free_soft_rev_index:
            res = 'Платный софт получет больше обзоров,{:.2f} обзора на программу'.format(not_free_soft_rev_index)
        else:
            res = 'Платные и бесплатные программы получют одинаковое число обзоров,{:.2f} обзора на программу'.format(free_soft_rev_index)
        return res

    def most_usable_for(self):
        res = ''

        data_group = self.data.groupby(['Useable For','Free/Paid/Other']).size()
        index = data_group.index
        arr = np.array(index)
        arr = np.apply_along_axis(list, 0, arr)
        for group in arr:
            if 'Free' in group:
                res = group[0]
                break
        return res




Ai_dataset = Data_analizer()
Ai_dataset.read_file()
Ai_dataset.most_usable_for()