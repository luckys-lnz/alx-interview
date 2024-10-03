#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]
            temp.append(k[i - 1][j] + k[i - 1][j + 1])
        temp.append(1)
        k.append(temp)
    return k

# #!/usr/bin/python3
# """Create a function def pascal_triangle(n):
# that returns a list of lists of integers representing
# the Pascal’s triangle of n:

# Keyword arguments:
# n -- an integer lists of list of integers representing pascals triangle.
# Return: an empty list if n <= 0
# """

# def pascal_triangle(n):
#     # Return an empty list if n is less than or equal to 0
#     if n <= 0:
#         return []
    
#     # Initialize the triangle list
#     triangle = []

#     for row in range(n):
#         # Start each row with an empty list
#         current_row = [1] # manually set the first elemnt to 1.
        
#         # Calculate the values for the current row using the values from the previous row
#         if row > 1:  # Change from row > 0 to row > 1
#             for col in range(1, row):
#                 current_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
#             current_row.append(1)  # Last element is always 1
#         elif row == 1:
#             current_row.append(1)  # Add the second 1 for the second row
        
#         # Append the current row to the triangle
#         triangle.append(current_row)
    
#     return triangle


