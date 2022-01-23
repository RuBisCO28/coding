class Solution:
  def reverse(self, x: int) -> int:
    if x == 0:
      return 0
    answer = ""
    minus_flag = False
    arr = list(str(x))
    i = len(arr) - 1
    while i >= 0:
      if arr[i] == '-':
        minus_flag = True
      elif arr[i] != 0:
        answer += arr[i]
      i -= 1
    if -2**31 <= int(answer) and int(answer) <= (2**31 - 1):
      if minus_flag:
        return -1 * int(answer)
      else:
        return int(answer)
    else:
      return 0

result = Solution()
x = 123
x = -123
x = 120
x = 1534236469
print(result.reverse(x))


