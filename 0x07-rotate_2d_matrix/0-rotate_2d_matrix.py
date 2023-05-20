#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """

    if not isinstance(matrix, list):
        return

    rows = len(matrix)
    cols = len(matrix[0])

    # Transpose the matrix.
    for i in range(rows):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse the rows of the matrix.
    for i in range(rows // 2):
        matrix[i], matrix[rows - i - 1] = matrix[rows - i - 1], matrix[i]


