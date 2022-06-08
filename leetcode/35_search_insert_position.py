from typing import Optional
from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    if nums is None:
      return 0
    start = 0
    end = len(nums) - 1
    while start <= end:
      mid = (start + end) // 2
      print(start,mid,end)
      if nums[mid] == target:
        return mid

      if nums[mid] < target:
        start = mid + 1
      else:
        end = mid - 1
    return start

result = Solution()
nums = [1,3,5,6]
target = 5
target = 2
target = 7
target = 0
print(result.searchInsert(nums,target))
