from typing import Optional
from typing import List

# class Solution:
#   def findMin(self, nums: List[int]) -> int:
#     return sorted(nums)[0]

class Solution:
  def findMin(self, nums: List[int]) -> int:
    if nums is None:
      return 0
    start = 0
    end = len(nums) - 1

    if len(nums) == 1:
      return nums[0]
    if nums[end] > nums[0]:
      return nums[0]
    while start <= end:
      mid = (start + end) // 2
      # print(start,mid,end)
      if nums[mid] > nums[mid+1]:
        return nums[mid + 1]

      if nums[mid-1] > nums[mid]:
        return nums[mid]

      if nums[mid] > nums[0]:
        start = mid + 1
      else:
        end = mid - 1

result = Solution()
nums = [3,4,5,1,2]
print(result.findMin(nums))
