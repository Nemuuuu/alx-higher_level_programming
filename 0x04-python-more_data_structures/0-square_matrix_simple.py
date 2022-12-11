#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqd = [[row * row for row in col] for col in matrix]
    return sqd