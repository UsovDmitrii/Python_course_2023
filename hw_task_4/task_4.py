"""
4.	Создать вектор размера 10 со значениями от 0 до 1, не включая ни то, ни другое.
"""
import numpy as np

arr = 0.98 * np.random.random_sample(size=10) + 0.1

print(arr)
