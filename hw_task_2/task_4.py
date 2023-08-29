"""
4.	Имеются два списка состоящие из произвольных элементов.
Напишите функцию которая возвращает пересечение списков
(элементы которые встречаются в и там и там)
"""


def common(list_1, list_2):
    res = []
    for item in list_1:
        if item in list_2:
            res.append(item)

    return res


list_1 = [1, '1', 2, 'two', [1, 2, 3], False, 'three', 'four']
list_2 = [1, 2, 'two', [1, 2, 3], 'three', 'four', 5, 'five', True]

print(common(list_1,list_2))
