# import itertools

class Solution(object):
  # # itertools
  # def twoSum(self, nums, target):
  #   result=[]
  #   for conb in itertools.combinations(list(range(len(nums))), 2):
  #     result.append(list(conb))
  #     for item in result:
  #       tmp=0
  #       for item2 in item:
  #         tmp += nums[item2]
  #       if tmp==target:
  #         return(item)

  # # Brute Force
  # def BruteForce(self, nums, target):
  #   result=[]
  #   for i in range(len(nums)):
  #     for j in range(i,len(nums)):
  #       if i!=j:
  #         if nums[i] + nums[j] == target:
  #           result = [i,j]
  #   return result

  # Hash Map
  # 差分で残ったのをキーとして登録しておくことで一致するものが現れたときに合計がtargetになることの証明になる
  def HashMap(self, nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
      search_key = target - num
      if search_key not in hashmap:
        hashmap[num] = i
      else:
        return [i, hashmap[search_key]]

nums = [0,4,3,0]
target = 0
nums = [2,7,11,15]
target = 9
result = Solution()
print(result.HashMap(nums, target))

