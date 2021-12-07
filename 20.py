def removeParentheses(s, flag):
  if '()' in s:
    s = s.replace('()','')
    flag = True
  if '{}' in s:
    s = s.replace('{}','')
    flag = True
  if '[]' in s:
    s = s.replace('[]','')
    flag = True
  if s == "":
    return True
  elif flag == False:
    return False
  else:
    return removeParentheses(s, False)

class Solution:
  def isValid(self, s: str) -> bool:
    answer = False
    if len(s) % 2 != 0:
      return False
    answer = removeParentheses(s, False)
    return answer

result = Solution()
s = "()[]{}"
s = "{[]}"
s = "([)]"
s = "(]"
print(result.isValid(s))
