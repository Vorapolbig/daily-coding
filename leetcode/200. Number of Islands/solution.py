def solution(grid):
  count = 0
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if (grid[row][col] == "1"):
        count += 1
        checkNew(grid,row,col)
  return count

def checkNew(grid,row,col):
  # print(row)
  if ((row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])) or grid[row][col] == "0"):
    return
  grid[row][col] = "0"
  checkNew(grid, row+1, col)
  checkNew(grid, row-1, col)
  checkNew(grid, row, col+1)
  checkNew(grid, row, col-1)
  
test1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
test2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(solution(test2))

