#!/usr/bin/python3
"""Island Perimeter - ALX Interview"""

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 to perimeter
                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # If top cell is land, decrement perimeter by 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # If left cell is land, decrement perimeter by 2

    return perimeter
