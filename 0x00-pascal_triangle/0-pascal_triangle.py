#!/usr/bin/python3
"""Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n:

Keyword arguments:
n -- an integer lists of list of integers representing pascals triangle.
Return: an empty list if n <= 0
"""


def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []
    
    # Initialize the triangle list
    triangle = []

    for row in range(n):
        # Start each row with 1
        current_row = [1] * (row + 1)
        
        # Calculate the values for the current row using the values from the previous row
        for col in range(1, row):
            current_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
        
        # Append the current row to the triangle
        triangle.append(current_row)
    
    return triangle

# Example usage:
print(pascal_triangle(5))
