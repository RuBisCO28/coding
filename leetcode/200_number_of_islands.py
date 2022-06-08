from typing import Optional
from typing import List

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    def check(i,j):
      if grid[i][j] == "1":
        grid[i][j] = "2" # visited
        if i - 1 >= 0:
          check(i-1,j)
        if j - 1 >= 0:
          check(i,j-1)
        if i + 1 <= len(grid) - 1:
          check(i+1,j)
        if j + 1 <= len(grid[0]) - 1:
          check(i,j+1)

    count = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == '1':
          check(i,j)
          count += 1
    return count

result = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(result.numIslands(grid))
