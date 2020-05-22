#!/usr/bin/python3
""" matrix multiplication """


def matrix_mul(m_a, m_b):
    """ matrix mul function"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for line in m_a:
        if type(line) is not list:
            raise TypeError("m_a must be a list of lists")
    for line in m_b:
        if type(line) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) is 0 or len(m_a[0]) is 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) is 0 or len(m_b[0]) is 0:
        raise ValueError("m_b can't be empty")

    for line in m_a:
        for num in line:
            if type(num) is not int and type(num) is not float:
                    raise TypeError("m_a should contain only \
integers or floats")
    for line in m_b:
        for num in line:
            if type(num) is not int and type(num) is not float:
                    raise TypeError("m_b should contain only \
integers or floats")

    len_a = len(m_a[0])
    len_b = len(m_b[0])
    for line in m_a:
        if len(line) is not len_a:
            raise TypeError("each row of m_a must be of the same size")
    for line in m_b:
        if len(line) is not len_b:
            raise TypeError("each row of m_b must be of the same size")

    if len_a is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_mat = [[0 for i in range(0, len_b)] for j in range(0, len(m_a))]

    for row in range(0, len(m_a)):
        for num in range(0, len(new_mat[0])):
            for n_a in range(0, len_a):
                new_mat[row][num] += m_a[row][n_a] * m_b[n_a][num]
    return new_mat
