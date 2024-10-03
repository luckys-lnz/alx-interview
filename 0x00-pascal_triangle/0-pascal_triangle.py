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
        # Start each row with an empty list
        current_row = [1] # manually set the first elemnt to 1.
        
        # Calculate the values for the current row using the values from the previous row
        if row > 1:  # Change from row > 0 to row > 1
            for col in range(1, row):
                current_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
            current_row.append(1)  # Last element is always 1
        elif row == 1:
            current_row.append(1)  # Add the second 1 for the second row
        
        # Append the current row to the triangle
        triangle.append(current_row)
    
    return triangle
