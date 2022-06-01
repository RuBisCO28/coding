from typing import List

class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    arr = [i+1 for i in range(n)] #
    values = [0 for j in range(n)]
    everybody = dict(zip(arr, values))
    judge = dict(zip(arr, values))
    answer = -1
    for i in range(len(trust)):
      if trust[i][0] in everybody:
        everybody[trust[i][0]] = 1
      if trust[i][1] in judge:
        judge[trust[i][1]] += 1
    for i in judge:
      if everybody[i] == 0 and judge[i] == (n - 1):
        answer = i
    return answer

result = Solution()
N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
N = 3
trust = [[1,3],[2,3],[3,1]]
N = 3
trust = [[1,2],[2,3]]
print(result.findJudge(N, trust))

# the town judge trusts nobody
# internal array index 0 won't be town judge, everybody
