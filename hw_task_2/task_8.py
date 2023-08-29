"""
8.Пусть у нас есть список кортежей, которые описывают химические элементы (номер группы, порядковый номер, название)

elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

Отсортируйте список не учитывая при сортировке первый элемент каждого кортежа.

"""

elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

sorted_elements = sorted(elements, key=lambda a: [a[1], a[2]])

print(sorted_elements)