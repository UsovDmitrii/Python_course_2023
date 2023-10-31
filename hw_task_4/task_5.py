"""
5.	Создайте функцию, которая
a.	принимает число (количество элементов в матрице)
b.	Проверяет можно ли построить матрицы с размерностью из множителей принимаемого числа.
c.	При проверке не учитывать матрицы с множителем “1”
d.	постройте все возможные матрицы и выведите в консоль.
e.	если число нельзя разбить на множители без остатка выведите сообщение в консоль.

"""
import numpy as np


def matrix_generator(n):
    flag = False
    for i in range(2, (n // 2 + 1)):
        if n % i == 0:
            flag = True
            # print(f'i={i},n/i={n/i}')
            j = int(n / i)
            matrix = np.ones([i, j], int)
            print(matrix)
    if flag == False:
        print(f"Number {n} is simple")


matrix_generator(16)
