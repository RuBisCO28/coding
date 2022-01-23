def combination(a, b):
  answer = []
  for i in range(len(a)):
    for j in range(len(b)):
      answer.append(a[i]+b[j])
  return answer

def combination_t(a, b, c):
  answer = []
  for i in range(len(a)):
    for j in range(len(b)):
      for k in range(len(c)):
        answer.append(a[i]+b[j]+c[k])
  return answer

def combination_f(a, b, c, d):
  answer = []
  for i in range(len(a)):
    for j in range(len(b)):
      for k in range(len(c)):
        for l in range(len(d)):
          answer.append(a[i]+b[j]+c[k]+d[l])
  return answer

class Solution:
  # def letterCombinations(self, digits: str) -> List[str]:
  def letterCombinations(self, digits: str):
    arr = list(digits)
    tel = {"2": ['a', 'b', 'c'],"3": ['d', 'e', 'f'],"4": ['g', 'h', 'i'],"5": ['j', 'k', 'l'],"6": ['m', 'n', 'o']
          ,"7": ['p', 'q', 'r', 's'],"8": ['t', 'u', 'v'],"9": ['w', 'x', 'y', 'z']}
    if len(digits) == 4:
      return combination_f(tel[arr[0]], tel[arr[1]], tel[arr[2]], tel[arr[3]])
    elif len(digits) == 3:
      return combination_t(tel[arr[0]], tel[arr[1]], tel[arr[2]])
    elif len(digits) == 2:
      return combination(tel[arr[0]], tel[arr[1]])
    elif len(digits) == 1:
      return tel[digits]
    elif len(digits) == 0:
      return []

result = Solution()
# digits = "23"
# digits = "2"
# digits = "234"
digits = "5678"
print(result.letterCombinations(digits))
