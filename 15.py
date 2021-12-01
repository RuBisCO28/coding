# Time Limit Exceeded
# def get_unique_list(seq):
#   seen = []
#   return [x for x in seq if x not in seen and not seen.append(x)]

# class Solution:
#   def threeSum(self, nums):
#     answer = []
#     if len(nums) == 0 or len(nums) == 1:
#       return []
#     for i in range(len(nums)):
#       for j in range(len(nums)):
#         for k in range(len(nums)):
#           if i != j and j != k and i != k:
#             if (nums[i] + nums[j] + nums[k]) == 0:
#               answer.append(sorted([nums[i], nums[j], nums[k]]))
#     return get_unique_list(answer)

class Solution:
  def threeSum(self, nums):
  # def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    answer = []
    for i in range(len(nums)-2):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      left = i + 1
      right = len(nums) - 1

      while left < right:
        sums = nums[left] + nums[right] + nums[i]
        if sums < 0:
          left += 1
        elif sums > 0:
          right -= 1
        else:
          answer.append([nums[i], nums[left], nums[right]])
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left > right and nums[right] == nums[right - 1]:
            right -= 1
          left += 1
          right -= 1
    return answer

result = Solution()
nums = [-1,0,1,2,-1,-4]
# nums = [11,-8,9,-6,-10,14,-5,-10,2,-1,-14,-13,-5,9,-5,-12,9,5,-1,-4,-14,5,-11,3,6,-7,2,-14,9,-6,-8,-2,-7,8,7,-2,7,9,3,-14,-14,5,-12,-4,-9,-1,-8,7,11,-2,-11,4,-11,-15,-7,10,-7,10,4,10,11,11,-7,-11,4,7,2,-12,1,12,-10,2,2,-15,6,1,-1,13,-7,-12,-4,-11,7,0,-11,-15,-12,-10,2,7,-15,-2,3,-15,-6,14,-1,11,-13,-15,9,14,-5,-12,-15,-14,4,-9,6,5,-6,-13,9]
print(result.threeSum(nums))
