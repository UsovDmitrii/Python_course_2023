"""
Замените классическое представление цикла for в примере на любую конструкцию, так чтоб результат оставался тот же
"""


def multiplier(lst):

    i = 0
    while i < len(lst):
        lst[i] *= i
        i += 1
    return lst


lst_1 = [2, 4, 5, 8, 9, 13]
print(multiplier(lst_1))

