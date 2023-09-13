#!/usr/bin/python3
"""
A pascal triangle function
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        row = [1]
        for i in range(1, len(triangle[-1])):
            row.append(triangle[-1][i-1] + triangle[-1][i])
        row.append(1)
        triangle.append(row)

    return triangle
