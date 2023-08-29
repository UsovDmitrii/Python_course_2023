"""
Напишите функцию которая:
a)	принимает список с произвольными значениями
b)	добавляет к нему произвольное значение
c)	возвращает результирующий список
"""


def add_value_to_list(list):

    import random
    x = random.randint(0, 100)
    list.append(x)

    return list1


list1 = [1, 2, 3, 'abc']
print(add_value_to_list(list1))
