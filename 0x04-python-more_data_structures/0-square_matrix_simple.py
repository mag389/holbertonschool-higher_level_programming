#!/usr/bin/python3
def square_matrix_simple(mat=[]):
    newmatrix = [[0 for i in range(len(mat[j]))] for j in range(len(mat))]
    for k in range(0, len(newmatrix)):
        for l in range(0, len(newmatrix[k])):
            newmatrix[k][l] = mat[k][l] ** 2
    return newmatrix
