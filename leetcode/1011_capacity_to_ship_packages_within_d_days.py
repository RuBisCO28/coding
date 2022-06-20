from typing import Optional
from typing import List

class Solution:
  def shipWithinDays(self, weights: List[int], days: int) -> int:
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
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(result.shipWithinDays(weights,days))
