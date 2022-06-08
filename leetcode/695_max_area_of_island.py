from typing import Optional
from typing import List

class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def check(i,j,area):
      if grid[i][j] == 1:
        grid[i][j] = 2 # visited
        area += 1
        if i - 1 >= 0:
          area = check(i-1,j,area)
        if j - 1 >= 0:
          area = check(i,j-1,area)
        if i + 1 <= len(grid) - 1:
          area = check(i+1,j,area)
        if j + 1 <= len(grid[0]) - 1:
          area = check(i,j+1,area)
      return area

    max_area = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j] == 1:
          area = 0
          count_area = check(i,j,area)
          if max_area < count_area:
            max_area = count_area
    return max_area

result = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(result.maxAreaOfIsland(grid))
