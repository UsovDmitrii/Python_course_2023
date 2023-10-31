"""
6.	Постройте класс для анализа файла с данными:
a.	Класс принимает путь к файлу при инициализации
b.	Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
Файл состоит из строк с произвольным текстом, элементами массива должны быть строки.
c.	Создайте метод поиска по тексту. Метод принимает паттерн поиска и возвращает список всех найденных совпадений.

"""
import numpy as np
import re

class text_manager():
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = []

    def read(self):
        f = open(self.file_path)
        self.file = f
        for line in self.file:
            self.text.append(line)

    def search_re(self,pat: str):
        pattern = pat

        res = []
        for line in self.text:
            result = re.findall(pattern,line)
            res.extend(result)
        return res


file_path = 'test_task_6.txt'
pattern = 't\w{3}\d{2}'

tm = text_manager(file_path)
tm.read()

print(tm.text)
print(tm.search_re(pattern))
