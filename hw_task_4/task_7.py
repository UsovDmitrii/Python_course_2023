"""
7.	напишите функцию которая
a.	принимает
i.	вектор A длинной X
ii.	размер слоя S - натуральное число
iii.	Булевый параметр last - по умолчанию False
b.	генерируется случайную матрицу B размером SxX
c.	создайте новую матрицу - произведение вектора A и матрицы B
d.	Найдите сумму каждой строки результирующей матрицы - должен получится вектор размером S
e.	Результирующий вектор проходит через функцию:
i.	Если last == False то функция - np.sin(x)
ii.	иначе np.maximum(x, 0)
f.	Вернуть результирующий массив и рандомную матрицу сгенерированную в начале функции,
g.	Для теста вызовите функцию 3 раза:
i.	первый - длинна вектора 5, заполнен случайными числами. Размер слоя 10
ii.	второй - на вход передайте вектор из предыдущего запуска. Размер слоя 10
iii.	третий - на вход передайте вектор из второго запуска, размер слоя 5 и last = True. Значения результата переведите в проценты и выведите в консоль.

h.	Вы написали прототип прямого распространения полносвязной нейронной сети.

"""
import numpy as np


def neyron(vec, S, last=False):
    x = len(vec)
    matrix = np.random.random_sample([S, x])
    new_matrix = matrix*vec
    sum = np.sum(new_matrix, axis = 0)
    if last == False:
        sum = np.sin(sum)
    elif last == True:
        sum = np.maximum(sum, 0)
    return matrix, sum

Vector = np.random.rand(5)
Matrix_1, f_vec = neyron(Vector, 10)
Matrix_2, f_vec_2 = neyron(f_vec, 10)
Matrix_3, f_vec_3 = neyron(f_vec_2, 5, last= True)

Matrix_4 = Matrix_3*100
print(Matrix_4)
