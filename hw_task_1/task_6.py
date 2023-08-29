"""
Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них.
"""


def pos_rate(list1):

    pos_list = []
    for num in list1:
        if num > 0:
            pos_list.append(num)
    return len(pos_list)


num_list = [-1, 2, 3, -4, 5, 6, 0]
print(pos_rate(num_list))
print(pos_rate([1, 2, 3, 4, 5, 6]))
print(pos_rate([-1, -2, -3, -4, -5, -6]))
print(pos_rate([0, 0, 0, 0, 0, 0]))
