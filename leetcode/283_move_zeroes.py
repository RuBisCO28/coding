from typing import Optional
from typing import List

"""
Do not return anything, modify nums in-place instead.
"""
class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    for i in range(len(nums)):
      while i <= len(nums) - 2:
        # print(nums)
        if nums[i] == 0:
          nums[i], nums[i+1] = nums[i+1], nums[i]
        elif nums[i-1] == 0:
          nums[i], nums[i-1] = nums[i-1], nums[i]
        i += 1
    return nums

result = Solution()
nums = [0,1,0,3,12]
nums = [0,0,1]
print(result.moveZeroes(nums))


