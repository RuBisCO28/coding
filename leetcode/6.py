import itertools

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    arr = list(s)
    j = 0
    flag = True
    answer = [[] for i in range(numRows)]
    for i in range(len(arr)):
      if j > numRows - 2 and flag == True:
        print(arr[i], j, flag)
        answer[j].append(arr[i])
        flag = not bool(flag)
        j-=1
      elif j <= 0 and flag == False:
        print(arr[i], j, flag)
        answer[j].append(arr[i])
        flag = not bool(flag)
        j+=1
      else:
        if flag == True:
          print(arr[i], j, flag)
          answer[j].append(arr[i])
          j+=1
        if flag == False:
          print(arr[i], j, flag)
          answer[j].append(arr[i])
          j-=1
    return ''.join(list(itertools.chain.from_iterable(answer)))

result = Solution()
s = "PAYPALISHIRING"
# s = "A"
numRows = 3
print(result.convert(s, numRows))


