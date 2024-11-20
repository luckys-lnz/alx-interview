#!/usr/bin/python3

"""Rotate a 2d matrix 90 deg clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in-place.

    The rotation is achieved by:
    1. Transposing the matrix (converting rows into columns).
    2. Reversing each row to complete the rotation.

    Args:
        matrix: A square 2D matrix to rotate.

    Returns:
        None: The matrix is inplace matrix.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
