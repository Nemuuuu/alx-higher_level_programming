#!/usr/bin/python3

def matrix_divided(matrix, div):
    for i in matrix:
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of list) of integers/floats")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            elif type(div) != int and type(div) != float:
                raise TypeError("div must be a number")
            else:
                print("{:.2f}".format(j/div),end=" ")
        print()
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))