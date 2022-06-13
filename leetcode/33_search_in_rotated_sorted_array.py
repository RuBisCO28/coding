from typing import Optional
from typing import List

# class Solution:
#   def search(self, nums: List[int], target: int) -> int:
#     if target in nums:
#       return nums.index(target)
#     else:
#       return -1

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    if nums is None:
      return 0
    start = 0
    end = len(nums) - 1

    while start <= end:
      mid = (start + end) // 2
      # print(start,mid,end)
      if nums[mid] == target:
        return mid

      # left sorted portion
      if nums[start] <= nums[mid]:
        if target > nums[mid] or target < nums[start]:
          start = mid + 1
        else:
          end = mid - 1
      # right sorted portion
      else:
        if target < nums[mid] or target > nums[end]:
          end = mid - 1
        else:
          start = mid + 1
    return -1

result = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
target = 3
print(result.search(nums,target))
