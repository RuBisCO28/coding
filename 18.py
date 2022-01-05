class Solution:
  # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
  def fourSum(self, nums, target):
    nums.sort()
    answer = []
    for i in range(len(nums)-3):
      if i > 0 and nums[i] == nums[i-1]:
        continue
      for j in range(i+1, len(nums)-2):
        if j > i + 1 and nums[j] == nums[j-1]:
          continue
        left = j + 1
        right = len(nums) - 1

        while left < right:
          sums = nums[i] + nums[j] + nums[left] + nums[right]
          if sums < target:
            left += 1
          elif sums > target:
            right -= 1
          else:
            answer.append([nums[i], nums[j], nums[left], nums[right]])
            while left < right and nums[left] == nums[left + 1]:
              left += 1
            while left < right and nums[right] == nums[right - 1]:
              right -= 1
            left += 1
            right -= 1
    return answer

result = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
nums = [2,2,2,2,2]
target = 8
print(result.fourSum(nums, target))
