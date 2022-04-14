def newPositions(grid, dp, x, y, n):
  ranges = [
    [[x, y] for x in range(x + 1, n)],
    [[x, y] for x in range(x - 1, -1, -1)],
    [[x, y] for y in range(y + 1, n)],
    [[x, y] for y in range(y - 1, -1, -1)]
  ]
  result = []
  for r in ranges:
    for [x, y] in r:
      if grid[x][y] == 'X' or dp[x][y] != -1:
        break
      result.append([x, y])
  return result

def minimumMoves(grid, startX, startY, goalX, goalY):
  grid = [list(row) for row in grid]
  n = len(grid)
  dp = [[-1 for i in range(n)] for i in range(n)]
  move = 0
  dp[startX][startY] = move
  currentPositions = [[startX, startY]]
  while len(currentPositions) > 0:
    nextPositions = []
    for [x, y] in currentPositions:
      nextPositions += newPositions(grid, dp, x, y, n)
    move += 1
    for [x, y] in nextPositions:
      dp[x][y] = move
    currentPositions = nextPositions
  return dp[goalX][goalY]

if __name__ == "__main__":
  grid = ['.X.','.X.', '...']
  startX = 0
  startY = 0
  goalX = 0
  goalY = 2
  print(minimumMoves(grid, startX, startY, goalX, goalY))

# .X.
# .X.
# ...

# 0,0 -> 2,0 -> 2,2 -> 0,2
# 探索してるぽい
