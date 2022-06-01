# Time limit exceeded
# class Solution:
#   def minWindow(self, s: str, t: str) -> str:
#     if s == t: return s
#     if len(s) < len(t): return ""
#     if len(t) == 1:
#       if t in s:
#         return t
#       else:
#         return ""
#     min_len = len(s)
#     answer = [0,0]
#     flag = True

#     for i in range(len(s)):
#       arr = list(t)
#       if s[i] in arr:
#         pos = 0
#         while i + pos < len(s):
#           if s[i+pos] in arr:
#             arr.remove(s[i+pos])
#             if len(arr) == 0 or min_len < pos + 1:
#               break
#           pos += 1
#         if len(arr) == 0:
#           print(i, i+pos, pos)
#           flag = False
#           if min_len >= pos + 1:
#             min_len = pos + 1
#             answer[0] = i
#             answer[1] = i + pos
#     if flag:
#       return ""
#     return s[answer[0]:answer[1]+1]

import collections

class Solution:
  def minWindow(self, s: str, t: str) -> str:
    if not t or not s:
      return ""

    dict_t = collections.Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None

    while r < len(s):
      character = s[r]
      window_counts[character] = window_counts.get(character, 0) + 1
      print(character, window_counts)

      # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
      if character in dict_t and window_counts[character] == dict_t[character]:
        formed += 1

      # Try and contract the window till the point where it ceases to be 'desirable'.
      while l <= r and formed == required:
          character = s[l]

          # Save the smallest window until now.
          if r - l + 1 < ans[0]:
              ans = (r - l + 1, l, r)

          # The character at the position pointed by the `left` pointer is no longer a part of the window.
          window_counts[character] -= 1
          if character in dict_t and window_counts[character] < dict_t[character]:
              formed -= 1

          # Move the left pointer ahead, this would help to look for a new window.
          l += 1

      # Keep expanding the window once we are done contracting.
      r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

result = Solution()
s = "ADOBECODEBANC"
t = "ABC"
s = "a"
t = "b"
s = "ab"
t = "a"
t = "b"
s = "abc"
t = "ac"
s = "acbbaca"
t = "aba"
# s = "aaflslflsldkalskaaa"
# t = "aaa"
print(result.minWindow(s,t))
