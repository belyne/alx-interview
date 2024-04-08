#!/usr/bin/python3
"""Island Perimeter - ALX Interview"""


def check_val(x):
    """Check if the value is 0 and return 1, otherwise return 0."""
    if x == 0:
        return 1
    return 0


def island_perimeter(grid):
    """Calculate the perimeter of the island in the given 2D grid.

    Args:
        grid (list): A 2D grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    row = len(grid)
    col = len(grid[0])
    assert (1 <= row <= 100) and (1 <= col <= 100), \
    "Length must be between 1 and 100"

    perimeter = 0
    for i in range(row):
        for j in range(col):
            assert grid[i][j] in [0, 1], "Grid numbers must be 0 or 1"
            if grid[i][j] == 1:
                if i - 1 < 0:
                    perimeter += 1
                else:
                    perimeter += check_val(grid[i - 1][j])
                if j - 1 < 0:
                    perimeter += 1
                else:
                    perimeter += check_val(grid[i][j - 1])

                try:
                    perimeter += check_val(grid[i + 1][j])
                except IndexError:
                    perimeter += 1
                try:
                    perimeter += check_val(grid[i][j + 1])
                except IndexError:
                    perimeter += 1

    return perimeter

