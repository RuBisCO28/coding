class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 0: return 0
    if len(s) == 1 or len(s.strip(' ')) == 0: return 1

    tmp = []
    max_length = 0
    cnt = 0
    for i in s:
      if i in tmp:
        tmp = tmp[tmp.index(i)+1:]
        tmp.append(i)
        cnt = len(tmp)
      else:
        cnt += 1
        tmp.append(i)
      if cnt > max_length:
        max_length = cnt
    return max_length

result = Solution()
s = "pwwkew"
# s = "au" # 2
# s = "aab" # 2
# s = "dvdf" # 3
print(result.lengthOfLongestSubstring(s))
