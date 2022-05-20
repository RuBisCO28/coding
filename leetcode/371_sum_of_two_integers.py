# success but not good solution
# class Solution:
#   def getSum(self, a, b):
#     return sum([a,b])

class Solution:
  def getSum(self, a, b):
    while a != 0 and b != 0:
      and_result = a & b
      xor_result = a ^ b # not carry
      a = and_result << 1 # carry
      b = xor_result
    if (a!=0):
      return a
    else:
      return b

a = 1
b = 2
result = Solution()
print(result.getSum(a, b))

