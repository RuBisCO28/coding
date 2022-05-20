# success but not good solution
# class Solution:
#   def hammingWeight(self, n: int) -> int:
#     return len([i for i in list(bin(n)) if i == '1'])

class Solution:
  def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
      n &= n - 1
      print(n)
      count += 1
    return count

n = 11
result = Solution()
print(result.hammingWeight(n))

