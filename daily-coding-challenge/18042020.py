"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

maxRow = len(grid)
maxCol = len(grid[0])
dp = [[0]*maxCol] * maxRow
def solution(grid):
    for row in range(maxRow):
        for col in range(maxCol):
            if row == 0 and col == 0:
                dp[row][col] = grid[row][col]
            else: 
                dp[row][col] = grid[row][col] + min((dp[row-1][col] if row !=0 else 9999999)\
            , (dp[row][col-1] if col != 0 else 9999999))
    return dp[maxRow-1][maxCol-1]

print(solution(grid))
