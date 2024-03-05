#!/usr/bin/python3
"""Island Perimeter Problem in one line
"""


def island_perimeter(grid):
    """island_perimeter 👿

    Args:
        grid list[list[int]]: mutilevel list

    Returns:
        int: perimiter
    """
    return sum(4 - (grid[i - 1][j] if i > 0 and
                    grid[i - 1][j] == 1 else 0) -
               (grid[i][j - 1] if j > 0 and
                grid[i][j - 1] == 1 else 0) -
               (grid[i + 1][j] if i < len(grid) - 1 and
                grid[i + 1][j] == 1 else 0) -
               (grid[i][j + 1] if j < len(grid[0]) - 1 and
                grid[i][j + 1] == 1 else 0)
               for i in range(len(grid)) for j in range(len(grid[0]))
               if grid[i][j] == 1)
