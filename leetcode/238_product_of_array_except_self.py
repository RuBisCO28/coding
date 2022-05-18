# left-right strategy
class Solution:
  def productExceptSelf(self, nums):
    r = 1
    z = False
    rn = 1
    for i in range(1,len(nums)):
      if z:
        rn *= nums[i]
      if nums[i] == 0:
        z = True
      r *= nums[i]
    answer = []
    answer.append(r)
    l = nums[0]
    for j in range(1, len(nums)):
      if j != 1:
        l *= nums[j-1]
      # print(l,nums[j],nums[j-1])
      if nums[j] != 0:
        r //= nums[j]
        answer.append(l*r)
      else:
        answer.append(l*rn)
    return answer

nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
result = Solution()
print(result.productExceptSelf(nums))

