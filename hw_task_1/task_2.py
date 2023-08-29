
"""
Напишите функцию которая
a)	принимает два списка
b)	возвращает длину самого длинного
"""

list1 = [4, 5, 6]
list2 = [1, 2, 3, 4]


def longest_list(list_1, list_2):

    a = len(list_1)
    b = len(list_2)
    if a >= b:
        return a
    else:
        return b


print(longest_list(list1, list2))
print(longest_list([], [1]))
print(longest_list([1, 2, 3], [1, 2]))
