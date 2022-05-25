# Constraints:
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order => skip check
# newInterval.length == 2
# 0 <= start <= end <= 105

# consider pattern when overlap
# overlap at the only edge of right
# overlap at the only edge of left
# all overlap
# outside(not overlap)

from http.client import NETWORK_AUTHENTICATION_REQUIRED
from typing import List

# class Solution:
#   def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#     nst,ned = newInterval[0],newInterval[1]
#     answer = []
#     min_v = nst
#     max_v = ned
#     if len(intervals) == 0:
#       answer.append([min_v, max_v])
#       return answer
#     if len(newInterval) == 0:
#       answer.append([st, ed])
#       return answer
#     if(len(intervals)) != 1:
#       for i in range(len(intervals)):
#         st,ed = intervals[i][0],intervals[i][1]
#         # print(st,ed,nst,ned,min_v,max_v)
#         if ned < st:
#           answer.append([st,ed])
#         elif ed < nst:
#           answer.append([st,ed])
#         elif st <= nst and ned <= ed:
#           answer.append([st,ed])
#         elif nst < st and ed < ned:
#           if min_v > nst:
#             min_v = nst
#           if max_v < ned:
#             max_v = ned
#         elif st < nst and nst <= ed and ed < ned:
#           if min_v > st:
#             min_v = st
#           if max_v < ned:
#             max_v = ned
#         elif nst < st and st <= ned and ned < ed:
#           if min_v > nst:
#             min_v = nst
#           if max_v < ed:
#             max_v = ed
#       answer.append([min_v, max_v])
#       return sorted(answer)
#     else:
#       st,ed = intervals[0][0],intervals[0][1]
#       # print(st,ed,nst,ned,min_v,max_v)
#       if ned < st:
#         answer.append([st,ed])
#       elif ed < nst:
#         answer.append([st,ed])
#       elif st <= nst and ned <= ed:
#         answer.append([st,ed])
#       elif nst < st and ed < ned:
#         answer.append([min_v,max_v])
#       elif st < nst and nst <= ed and ed < ned:
#         answer.append([st,ned])
#       elif nst < st and st <= ned and ned < ed:
#         answer.append([nst,ed])
#       return answer

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    n = len(intervals)
    answer = []
    i = 0

    while i < n and intervals[i][1] < newInterval[0]:
      answer.append(intervals[i])
      i += 1

    print(answer)

    while i < n and intervals[i][0] <= newInterval[1]:
      newInterval[0] = min(newInterval[0], intervals[i][0])
      newInterval[1] = max(newInterval[1], intervals[i][1])
      i += 1

    answer.append(newInterval)

    # while i < n:
    #   answer.append(intervals[i])
    #   i += 1

    return answer

result = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
# intervals = [[1,5]]
# newInterval = [2,3]
# intervals = []
# newInterval = [5,7]
# intervals = [[1,5]]
# newInterval = [2,7]
# intervals = [[1,5]]
# newInterval = [6,8]
print(result.insert(intervals, newInterval))
