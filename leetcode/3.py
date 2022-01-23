

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    cnt = 0
    tmp = []
    max_length = 0
    arr = list(s)
    if len(arr) == 0:
      return 0
    if len(arr) == 1 or len(s.strip(' ')) == 0:
      return 1
    for x in arr:
      if x in tmp:
        tmp = tmp[tmp.index(x)+1:]
        tmp.append(x)
        cnt = len(tmp)
      else:
        tmp.append(x)
        cnt += 1
      if cnt > max_length:
        max_length = cnt
    return max_length

result = Solution()
# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = "   "
# s = "c"
# s = "au"
s = "dvdf"
print(result.lengthOfLongestSubstring(s))


