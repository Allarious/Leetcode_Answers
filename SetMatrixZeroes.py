from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    if i == 0 and j == 0:
                        matrix[0][0] = 'rd'
                    elif i == 0:  # r
                        if matrix[0][0] == 'd':
                            matrix[0][0] = 'rd'
                        elif matrix[0][0] == 'rd':
                            pass
                        else:
                            matrix[0][0] = 'r'
                        matrix[0][j] = 'c'
                    elif j == 0:  # d
                        if matrix[0][0] == 'r':
                            matrix[0][0] = 'rd'
                        elif matrix[0][0] == 'rd':
                            pass
                        else:
                            matrix[0][0] = 'd'
                        matrix[i][0] = 'c'
                    else:
                        matrix[i][0] = 'c'
                        matrix[0][j] = 'c'

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i == 0 or j == 0:
                    continue
                if matrix[i][0] == 'c' or matrix[0][j] == 'c':
                    matrix[i][j] = 0

        zero_to_right = False
        zero_to_down = False

        if matrix[0][0] == 'r':
            zero_to_right = True
        elif matrix[0][0] == 'd':
            zero_to_down = True
        elif matrix[0][0] == 'rd':
            zero_to_right = True
            zero_to_down = True

        for i in range(len(matrix[0])):
            if zero_to_right:
                matrix[0][i] = 0
            elif matrix[0][i] == 'c':
                matrix[0][i] = 0

        for i in range(len(matrix)):
            if zero_to_down:
                matrix[i][0] = 0
            elif matrix[i][0] == 'c':
                matrix[i][0] = 0