#!/usr/bin/python3
"""returns the perimeter of an island."""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A grid where 0 represents water
                                    and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                # Check the top
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1
                # Check the bottom
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1
                # Check the left side
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1
                # Check the right side
                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1

    return perimeter
