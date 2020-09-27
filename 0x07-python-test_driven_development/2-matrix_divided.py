#!/usr/bin/python3
""" Program that divide a matrix  with a x number """


def matrix_divided(matrix, div):
    """
    matrix its a list type with a sublist of numbers
    """
    horrors = {
        "mlist": "matrix must be a matrix (list of lists) of integers/floats",
        "rowlist": "Each row of the matrix must have the same size",
        "div_int": "div must be a number",
        "zero_div": "division by zero"
    }

    if type(matrix) is list and matrix != []:
        if len(matrix) == 0:
            raise TypeError(horrors["mlist"])
        nw = []
        row_list = None
        for sub_list in matrix:
            if type(sub_list) is list and sub_list != []:
                if row_list is None:
                    row_list = len(sub_list)
                if row_list != len(sub_list):
                    raise TypeError(horrors["rowlist"])
                for elemtl in sub_list:
                    if type(elemtl) is not int and type(elemtl) is not float:
                        raise TypeError(horrors["mlist"])
            else:
                raise TypeError(horrors["mlist"])
    else:
        raise TypeError(horrors["mlist"])

    if type(div) is not int and type(div) is not float:
        raise TypeError(horrors["div_int"])
    if div is 0:
        raise ZeroDivisionError(horrors["zero_div"])

    nw = list(map(lambda x: list(map(lambda x: round(x / div, 2), x)), matrix))
    return nw
