import math

class Solution:
  def isPalindrome(self, x: int) -> bool:
    arr = list(str(x))
    if len(arr) == 1:
      return True
    if arr[0] == "-":
      return False
    cnt = math.floor(len(arr)/2)
    for i in range(cnt):
      # print(i, len(arr)-i-1)
      if arr[i] != arr[len(arr)-i-1]:
        return False
    return True

result = Solution()
x = 121121
x = 12112
print(result.isPalindrome(x))


