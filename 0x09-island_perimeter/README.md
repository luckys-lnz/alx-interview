# 0x09. Island Perimeter

**Function Description**

- def island_perimeter(grid):
    Calculates the perimeter of the island described in grid.

**Parameters:**
- grid: A list of lists of integers, where:
- 0 represents water.
- 1 represents land.
    - Returns:
        - An integer representing the total perimeter of the island.


**Assumptions**

- The grid is completely surrounded by water.
- The grid contains only one island or nothing.
- The island does not have any lakes (water cells fully surrounded by land).
- The width and height of the grid do not exceed 100.


**Main file**
```
from 0-island_perimeter import island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12
```

