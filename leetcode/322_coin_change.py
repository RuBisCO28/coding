# https://engineer.yeele.net/algorithm/leetcode-medium-322-coin-change/

from typing import List
import sys

# class Solution:
#   def coinChange(self, coins: List[int], amount: int) -> int:
#     if amount <= 0 or coins is None or len(coins) == 0: return 0
#     dp = [[0]*amount for _ in range(len(coins))]
#     MAXN = sys.maxsize

#     for i in range(len(dp)):
#       for j in range(len(dp[0])):
#         coin = coins[i]
#         if i == 0:
#           if (j+1) % coin == 0:
#             dp[i][j] = int((j+1)/coin)
#           else:
#             dp[i][j] = MAXN
#         else:
#           if j-coin >= 0:
#             that = dp[i][j-coin] + 1
#           else:
#             if coin == j + 1: that = 1
#             else: that = MAXN
#           dp[i][j] = min(that, dp[i-1][j])
#     # for row in dp:
#     #   print(row)
#     return -1 if dp[i][j] == MAXN else dp[i][j]

class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
      for x in range(coin, amount + 1):
        dp[x] = min(dp[x], dp[x - coin] + 1)
        print(dp)
    print(dp)
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1,2,5]
amount = 11
result = Solution()
print(result.coinChange(coins,amount))
