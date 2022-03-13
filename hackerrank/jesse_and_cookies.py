# Time limit exceeded
# def cookies(k, A):
#   A.sort()
#   l = len(A)
#   step = 0
#   while True:
#     if l < 2:
#       step = -1
#       break
#     if A[0] >= k:
#       break
#     first = A.pop(0)
#     second = A.pop(0)
#     A.append(first+2*second)
#     A.sort()
#     # print(A)
#     l -= 1
#     step += 1
#   return step

import heapq

def cookies(k, A):
  heapq.heapify(A)
  l = len(A)
  step = 0
  while True:
    if l < 2:
      if A[0] >= k:
        break
      else:
        step = -1
        break
    if A[0] >= k:
      break
    first = heapq.heappop(A)
    second = heapq.heappop(A)
    heapq.heappush(A,first+2*second)
    # print(A)
    l -= 1
    step += 1
  return step

if __name__ == '__main__':
  k = 9
  A = [2,7,3,6,4,6]
  k = 105823341
  A = [1 for i in range(100000)]
  print(cookies(k, A))
