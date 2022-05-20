from typing import List

# num: 現在のをとる
# curSum: 前のと合計した値をとる
# maxSum: なにもとらない

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    curSum = maxSum = nums[0]
    for num in nums[1:]:
      curSum = max(num, curSum + num)
      maxSum = max(num, curSum, maxSum)
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
result = Solution()
print(result.maxSubArray(nums))

