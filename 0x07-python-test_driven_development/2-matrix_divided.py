#/usr/bin/python3
def matrix_divided(matrix, div):
    for i in matrix:
        for j in i:
            if type(i) is not int or type(i) is not float:
                if type(j) is not int or type(j) is not float:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")