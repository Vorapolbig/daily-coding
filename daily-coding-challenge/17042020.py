"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
def solution(grid):
    if len(grid) == 0:
        return 0
    n = 0
    maxRow =len(grid)
    maxCol =len(grid[0])
    for row in range(maxRow):
        for col in range(maxCol):
            # print(row,col,grid[row][col])
            if grid[row][col] == '1':
                n += 1
                checkNew(grid,row,col)
    return n 

def checkNew(grid,row,col):
    if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0])) or grid[row][col] == "0":
        return 
    grid[row][col] = "0"
    checkNew(grid, row+1, col)
    checkNew(grid, row-1, col)
    checkNew(grid, row, col+1)
    checkNew(grid, row, col-1)


# grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
grid = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
print(solution(grid))