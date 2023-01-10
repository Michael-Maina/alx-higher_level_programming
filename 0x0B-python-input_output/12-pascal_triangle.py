#!/usr/bin/python3
"""  """


def pascal_triangle(n):
    """ Returns a list of lists of integers
    representing the Pascal’s triangle of n """
    result = []
    if n <= 0:
        return result
    else:
        for i in range(n+1):
            a = n! / i!(n - 1)!
            result.append[a]

        return result
