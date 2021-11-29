class Solution:
  def romanToInt(self, s: str) -> int:
    arr = list(s)
    answer = 0
    for i in range(len(arr)):
      if arr[i] == 'M':
        answer += 1000
      elif arr[i] == 'D':
        answer += 500
      elif arr[i] == 'C':
        if (i != len(arr) - 1) and (arr[i+1] == 'M' or arr[i+1] == 'D'):
          answer -= 100
        else:
          answer += 100
      elif arr[i] == 'L':
          answer += 50
      elif arr[i] == 'X':
        if (i != len(arr) - 1) and (arr[i+1] == 'C' or arr[i+1] == 'L'):
          answer -= 10
        else:
          answer += 10
      elif arr[i] == 'V':
          answer += 5
      elif arr[i] == 'I':
        if (i != len(arr) - 1) and (arr[i+1] == 'X' or arr[i+1] == 'V'):
          answer -= 1
        else:
          answer += 1
    return answer

result = Solution()
s = "III"
s = "IV"
s = "IX"
s = "LVIII"
s = "MCMXCIV"
print(result.romanToInt(s))
