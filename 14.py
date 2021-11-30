class Solution:
  def longestCommonPrefix(self, strs) -> str:
    arr = []
    cnt = 0
    answer = ""
    if len(strs) == 1:
      return strs[0]
    for i in range(len(strs)):
      arr.append(len(strs[i]))
    for i in range(min(arr)):
      tmp = strs[0][i]
      for j in range(len(strs)):
        if tmp == strs[j][i]:
          cnt += 1
      if cnt == len(strs):
        answer += strs[0][i]
        cnt = 0
      else:
        return answer
    return answer

result = Solution()
strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
strs = ["a"]
strs = ["ab", "a"]
print(result.longestCommonPrefix(strs))
