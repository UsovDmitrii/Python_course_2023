"""
3.	Создайте матрицы 8x4 и 4x2 и перемножьте, результирующую матрицу выведите в консоль.
"""
import numpy as np

matrix_a = np.random.randint(10,size = (8,4))
matrix_b = np.random.randint(10,size = (4,2))

print(np.dot(matrix_a,matrix_b))

