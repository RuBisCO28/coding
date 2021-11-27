# Time Limit Exceeded
# class Solution:
#   def maxArea(self, height) -> int:
#     area = 0
#     max_area = 0
#     leng = len(height)
#     for i in range(leng):
#       for j in range(i, leng):
#         if i != j:
#           if height[i] > height[j]:
#             area = height[j] * (j - i)
#           else:
#             area = height[i] * (j - i)
#           if max_area < area:
#             max_area = area
#           print(i, j, height[i], height[j], area)
#     return max_area

class Solution:
  def maxArea(self, height) -> int:
    i = 0
    j = len(height) - 1
    area = 0
    max_area = 0
    while i != j:
      area = min(height[i], height[j]) * (j - i)
      if max_area < area:
        max_area = area
      if height[i] < height[j]:
        i += 1
      else:
        j -= 1
    return max_area

result = Solution()
height = [1,8,6,2,5,4,8,3,7]
height = [2,3,4,5,18,17,6]
print(result.maxArea(height))
