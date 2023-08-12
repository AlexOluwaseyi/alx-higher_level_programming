#!/usr/bin/python3
'''
def print_matrix_integer(matrix=[[]]):
    x = len(matrix)
    if x > 0:
        y = len(matrix[0])
        for i in range(x):
            for j in range(y):
                print("{:d}".format(matrix[i][j]), end=" ")
            print()
    else:
        print()
'''


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            print("{:d}".format(num), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()
