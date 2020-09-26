#!/usr/bin/python3
""" Program that divide a matrix  with a x number """


def matrix_divided(matrix, div):
    """
    matrix its a list type with a sublist of numbers
    """
    if type(matrix) is list:
        new_list = []
        row_list = None
        for sub_list in matrix:
            if type(sub_list) is list:
                if row_list is None:
                    row_list = len(sub_list)
                    for elemt_list in sub_list:
                        if type(elemt_list) is int or type(elemt_list) is float:
                            continue
                        else:
                            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                elif row_list != len(sub_list):
                    raise TypeError("Each row of the matrix must have the same size")
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    new_list = list(map(lambda x: list(map(lambda x: round(x / div, 2), x)), matrix))
    return new_list
