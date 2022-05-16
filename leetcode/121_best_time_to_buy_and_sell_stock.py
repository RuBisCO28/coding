# Time limit exceeded
# class Solution(object):
#   def maxProfit(self, prices):
#     max_v = 0
#     for i in range(len(prices)-1):
#       df = max(prices[i+1:]) - prices[i]
#       if df > max_v:
#         max_v = df
#     return max_v

# class Solution(object):
#   def maxProfit(self, prices):
#     l = len(prices)
#     answer = 0
#     if l == 1:
#       return 0
#     max_v = max(prices[1:])
#     max_idx = prices.index(max_v)
#     for i in range(l-1):
#       if i > max_idx:
#         max_v = max(prices[i+1:])
#         max_idx = prices.index(max_v)
#       df = max_v - prices[i]
#       if answer < df:
#         answer = df
#     return answer

class Solution(object):
  def maxProfit(self, prices):
    l = len(prices)
    max_v = 0 # difference
    min_v = float('inf') # bottom value
    for i in range(l):
      if prices[i] < min_v:
        min_v = prices[i]
      elif prices[i] - min_v > max_v:
        max_v = prices[i] - min_v
    return max_v

prices = [7,1,5,3,6,4]
prices = [2,4,1]
result = Solution()
print(result.maxProfit(prices))

