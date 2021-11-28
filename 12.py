import math

class Solution:
  def intToRoman(self, num: int) -> str:
    n = num
    answer = ""
    while n > 0:
      if n >= 1000:
        m = math.floor(n / 1000)
        n -= m * 1000
        answer += "M" * m
      elif n >= 100:
        c = math.floor(n / 100)
        n -= c * 100
        if c == 9:
          answer += "CM"
        elif c >= 5:
          answer += "D" + "C" * (c - 5)
        elif c == 4:
          answer += "CD"
        else:
          answer += "C" * c
      elif n >= 10:
        x = math.floor(n / 10)
        n -= x * 10
        if x == 9:
          answer += "XC"
        elif x >= 5:
          answer += "L" + "X" * (x - 5)
        elif x == 4:
          answer += "XL"
        else:
          answer += "X" * x
      elif n >= 1:
        i = math.floor(n / 1)
        n -= i * 1
        if i == 9:
          answer += "IX"
        elif i >= 5:
          answer += "V" + "I" * (i - 5)
        elif i == 4:
          answer += "IV"
        else:
          answer += "I" * i
    return answer

result = Solution()
num = 1994
print(result.intToRoman(num))
