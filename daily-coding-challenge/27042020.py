"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
def solution(matrix):
    if len(matrix) == 0:
        return 0
    rowMax = len(matrix)
    colMax = len(matrix[0])
    if rowMax == 0:
        return 0
    dp = [[0]*(colMax+1) for i in range(rowMax+1)]
    temp = 0
    for row in range(1,rowMax+1):
        for col in range(1,colMax+1):
            # print(dp)
            if matrix[row-1][col-1] == "0":
                dp[row][col] = 0
            else:
                dp[row][col] = min(min(dp[row-1][col],dp[row][col-1]),dp[row-1][col-1]) + 1
                temp = max(temp,dp[row][col])
            print(dp)
    return temp*temp

# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["1","1","1"],["1","1","1"],["1","1","1"]]
# matrix = [["0","0","1","1","1"],["1","0","1","1","1"],["0","1","1","1","1"],["1","0","1","1","1"]]
print(solution(matrix))