# sortして隣接比べて重複したらtrue
# hashにいれて重複した時点でtrue
# setで長さ比較

class Solution:
  def containsDuplicate(self, nums):
    if len(nums) == len(list(set(nums))):
      return False
    else:
      return True

nums = [1,1,1,3,3,4,3,2,4,2]
nums = [1,2,3,1]
result = Solution()
print(result.containsDuplicate(nums))

