class Solution:
  def myAtoi(self, s: str) -> int:
    if s == "" or s == "+" or s == "-":
      return 0
    arr = list(s.strip())
    minus_flag = False
    answer = []
    result = 0
    if len(arr) == 0:
      return 0
    if arr[0] != '-' and arr[0] != '+' and (not arr[0].isdecimal()):
      return 0
    if (arr[0] == '-' and arr[1] == '+') or (arr[0] == '+' and arr[1] == '-'):
      return 0
    for i in range(len(arr)):
      if i == 0 and arr[i] == '-':
        minus_flag = True
      elif arr[i].isdecimal():
        answer.append(arr[i])
      elif i == 0 and arr[i] == '+':
        continue
      else:
        if i == 0:
          return 0
        else:
          break
    if len(answer) == 0:
      return 0
    if minus_flag:
      result = -1 * int(''.join(answer))
    else:
      result = int(''.join(answer))
    if -2**31 <= result and result <= (2**31 - 1):
      return result
    elif -2**31 > result:
      return -2**31
    elif result > (2**31 - 1):
      return 2**31 - 1

result = Solution()
s = [
  "    42",
  "-42",
  "4193 with words",
  "words and 987",
  "-91283472332",
  "0032",
  "3.14159",
  "words and 987",
  "+-12", # 0
  "-+12", # 0
  "",
  "+",
  "00000-42a1234", # 0
  "-abc", # 0
  "-13+8", # -13
  "+1", # 1
  "    +0a32", # 0
  "   -42", # -42
  "123-" # 123
]
for i in range(len(s)):
  print(result.myAtoi(s[i]))
