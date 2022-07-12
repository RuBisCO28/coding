import sys
from typing import List

class Solution:
  # def maximumProduct(self, nums: List[int]) -> int:
  #   n = len(nums)
  #   if (n < 3):
  #     return -1

  #   leftMin = [-1 for i in range(n)]
  #   rightMin = [-1 for i in range(n)]
  #   leftMax = [-1 for i in range(n)]
  #   rightMax = [-1 for i in range(n)]

  #   max_product = -sys.maxsize - 1

  #   max_sum = nums[0]
  #   min_sum = nums[0]

  #   for i in range(1, n):
  #     leftMax[i] = max_sum

  #     if (nums[i] > max_sum):
  #       max_sum = nums[i]

  #     leftMin[i] = min_sum

  #     if (nums[i] < min_sum):
  #       min_sum = nums[i]

  #   max_sum = nums[n - 1]
  #   min_sum = nums[n - 1]

  #   for j in range(n - 2, -1, -1):
  #     rightMax[j] = max_sum

  #     if (nums[j] > max_sum):
  #       max_sum = nums[j]

  #     rightMin[j] = min_sum

  #     if (nums[j] < min_sum):
  #       min_sum = nums[j]

  #   print(leftMax,rightMax)
  #   print(leftMin,rightMin)

  #   for i in range(1, n - 1):
  #     max1 = max(nums[i] * leftMax[i] * rightMax[i],nums[i] * leftMin[i] * rightMin[i])
  #     max2 = max(nums[i] * leftMax[i] * rightMin[i],nums[i] * leftMin[i] * rightMax[i])

  #     max_product = max(max_product, max(max1, max2))

  #   return max_product

  def maximumProduct(self, nums: List[int]) -> int:
    n = len(nums)
    if (n < 3):
      return -1

    nums.sort()
    return max(nums[0] * nums[1] * nums[n - 1], nums[n - 1] * nums[n - 2] * nums[n - 3])

result = Solution()
nums = [ 1, 4, 3, -6, -7, 0 ]
print(result.maximumProduct(nums))

"""
1 2 3 ... 7 8 9
-1 1 2 ... 7 8 9
-2 -1 1 ... 7 8 9
-3 -2 -1 ... 7 8 9
-4 -3 -2 ... -1 8 9
-5 -4 -3 ... -2 -1 9
-6 -5 -4 ... -3 -2 -1
"""
