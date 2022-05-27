# class Solution:
#   def characterReplacement(self, s: str, k: int) -> int:
#     l = len(s)
#     if l == 1: return 1
#     max_cnt = 0
#     for i in range(l):
#       j = k
#       word = s[i]
#       p = i
#       cnt = 0
#       arr = []
#       while j >= 0 and p < l:
#         if s[p] == word:
#           cnt += 1
#           arr.append(s[i])
#         else:
#           j -= 1
#           if j < 0:
#             break
#           cnt += 1
#           arr.append(s[j])
#         p += 1
#         # print(i,word,j,arr)
#       if max_cnt < cnt:
#         max_cnt = cnt
#     return max_cnt

# class Solution:
#   def characterReplacement(self, s: str, k: int) -> int:
#     arr = []
#     l = len(s)
#     for i in range(l):
#       f = i - 1
#       b = i + 1
#       cnt = 1
#       print("f,b: ",f,b)
#       while f >= 0:
#         if s[f] == s[i]:
#           cnt += 1
#         else:
#           break
#         f -= 1
#       print("cnt_f: ", cnt)
#       while b < l:
#         if s[b] == s[i]:
#           cnt += 1
#         else:
#           break
#         b += 1
#       print("cnt_b: ", cnt)
#       arr.append(cnt)
#       print("arr: ", arr)
#     return arr

# https://medium.com/@eric.christopher.ness/leetcode-424-longest-repeating-character-replacement-6b97196b67af
from collections import defaultdict
from typing import List

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    positions = defaultdict(list)
    max_length = 0

    # {'A': [1, 1, 0, 1, 0, 0, 1], 'B': [0, 0, 1, 0, 1, 1, 0]})
    for index, char in enumerate(s):
      if char not in positions.keys():
        positions[char] = [0] * len(s)
      positions[char][index] = 1

    for char_array in positions.values():
      char_length = self.calculate_length(char_array, k)
      if char_length > max_length:
        max_length = char_length
    return max_length

  # ahead増やしてみて、k以上になればbehindを増やして縮めるslide_window方式
  def calculate_length(self, char_positions: List, k: int) -> int:
    behind, ahead = 0, 0
    match_count = 1 if char_positions[0] == 1 else 0
    nomatch_count = 1 if char_positions[0] == 0 else 0
    max_length = 0

    while ahead < len(char_positions):
      print(char_positions[0], "ahead: ",ahead, "behind: ",behind, "match_cnt: ",match_count, "nomatch_cnt: ",nomatch_count,"length: ",max_length)
      if nomatch_count <= k:
        ahead += 1
        if ahead == len(char_positions):
          break
        if char_positions[ahead] == 1:
          match_count += 1
        else:
          nomatch_count += 1
      else:
        if char_positions[behind] == 1:
          match_count -= 1
        else:
          nomatch_count -= 1
        behind += 1
      length = match_count + nomatch_count
      if length > max_length and nomatch_count <= k:
        max_length = length
    return max_length

result = Solution()
s = "AABABBA"
k = 1
# s = "ABBB"
# k = 2
print(result.characterReplacement(s, k))
