#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j != len(matrix[0]) - 1:
                    print('{}'.format(matrix[i][j]), end=' ')
                else:
                    print('{}'.format(matrix[i][j]), end='')
            print()
