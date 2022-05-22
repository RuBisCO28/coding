def knapsack(items, w):
  n = len(items)
  dp = [[0] * (w + 1) for _ in range(n + 1)]
  for i in range(n):
    for j in range(w + 1):
      if j < items[i][0]:
        dp[i+1][j] = dp[i][j]
      else:
        dp[i+1][j] = max(dp[i][j], dp[i][j - items[i][0]]+items[i][1])
  print(dp[n][w])

if __name__ == "__main__":
  items = [[2,3],[1,2],[3,6],[2,1],[1,3],[5,85]] # weight, value
  w = 100
  items = [[9,15],[6,10],[4,6]] # weight, value
  w = 10
  print(knapsack(items, w))
