#!/usr/bin/python3
"""
Lazy matrix mul module
contains:
matrix_mul function
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Multiplicates two matrices """
    return numpy.matmul(m_a, m_b)
