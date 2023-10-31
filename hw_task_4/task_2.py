"""
2.	Создайте матрицу 8х8 состоящую из 1 и 0 и заполненную в шахматном порядке
"""
import numpy as np


def chess_board():
    board = []

    for i in range(8):
        line = []
        for j in range(8):

            if (i + j) % 2 == 0:
                cell = 1
            else:
                cell = 0
            line.append(cell)
        board.append(line)
    martix = np.array(board)
    return martix


print(chess_board())
