#!/usr/bin/python3
""" lasy matr mul"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ lazy mul f'n """
    newmat = numpy.matmul(m_a, m_b)
    return newmat
