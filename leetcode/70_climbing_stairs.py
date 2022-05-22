# https://qiita.com/KueharX/items/5a8993968c995b074737

class Solution:
  def climbStairs(self, n: int) -> int:
    if n <= 1:
      return 1
    dp = [1, 1]
    for _ in range(2, n + 1):
      dp[1], dp[0] = dp[1] + dp[0], dp[1]
      print(dp)
    return dp[1]

# # fibo memo
# memo = [-1 for i in range(50)]

# class Solution:
#   def climbStairs(self, n: int) -> int:
#     if n <= 1:
#       return 1
#     if (memo[n] != -1): return memo[n]

#     memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
#     return memo[n]

n = 5
result = Solution()
print(result.climbStairs(n))

# 1,1,1,1,1
# 1,2,3,5,8

# 1,1,1,1
# 1,2,1
# 2,1,1
# 1,1,2
# 2,2
