#!/usr/bin/python3
"""A Pascal's Triangle function"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the specified row n"""
    if n <= 0:
        return []

    triangles = [[1]]
    for i in range(1, n):
        previous = triangles[-1]
        new = [1]
        for j in range(1, i):
            new_elem = previous[j - 1] + previous[j]
            new.append(new_elem)
        new.append(1)
        triangles.append(new)
    return (triangles)
