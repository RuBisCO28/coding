class Solution:
  def threeSumClosest(self, nums, target):
  # def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    answer = {"sums": 0, "diff": 0}
    result = {"sums": 0, "diff": 0}
    for i in range(len(nums)-2):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      left = i + 1
      right = len(nums) - 1

      cnt = 0
      while left < right:
        sums = nums[left] + nums[right] + nums[i]
        if cnt == 0 and i == 0:
          result = {"sums": sums, "diff": abs(sums - target)}
          cnt += 1
        elif abs(sums - target) < result["diff"]:
          result = {"sums": sums, "diff": abs(sums - target)}
        # print(i, left, right, sums, abs(sums - target), result, cnt)
        if sums < target:
          left += 1
        elif sums > target:
          right -= 1
        else:
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left > right and nums[right] == nums[right - 1]:
            right -= 1
          left += 1
          right -= 1
      # print(i, result["diff"], answer["diff"])
      if i == 0:
        answer["diff"] = result["diff"]
        answer["sums"] = result["sums"]
      elif i != 0 and (answer["diff"] > result["diff"]):
        answer["diff"] = result["diff"]
        answer["sums"] = result["sums"]

    return answer["sums"]

result = Solution()
# nums = [-1,2,1,-4]
# nums = [0,0,0]
# target = 1
nums = [1,2,5,10,11]
target = 12
print(result.threeSumClosest(nums, target))
