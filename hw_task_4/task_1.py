"""
1.	Создайте вектор размером 10 с рандомными значениями, отсортируйте и выведите в консоль.
"""
import numpy as np

arr = np.random.randint(100,size = 10)
print(arr)
arr.sort()
print(arr)
