#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and returns a new matrix.

    Args:
    matrix (list): A list of lists containing integers or floats.
    div (int or float): The divisor to divide all elements of the matrix by.

    Returns:
    list: A new matrix where all elements have been divided by the divisor and rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats, or if each row of the matrix is not of the same size.
              If the divisor is not a number (integer or float).
    ZeroDivisionError: If the divisor is equal to 0.

    """
    # Check if matrix is valid
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Check if each row of matrix has the same size
    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    # Check if divisor is valid
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Divide all elements of the matrix by the divisor and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return (new_matrix)
