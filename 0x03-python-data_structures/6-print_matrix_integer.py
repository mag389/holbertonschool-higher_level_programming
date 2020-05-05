#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        if len(matrix) == 0:
            print("")
        if len(matrix) == 1 and len(matrix[0]) == 0:
            print("")
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end="")
                if j < len(matrix[i]) - 1:
                    print(" ", end="")
                else:
                    print("")
