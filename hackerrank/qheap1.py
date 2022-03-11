# Time limit exceeded
# if __name__ == '__main__':
#   arr = []
#   nq = int(input())
#   for _ in range(nq):
#     l = str(input()).split()
#     if l[0] == '1':
#       arr.append(l[1])
#     elif l[0] == '2':
#       arr.pop(0)
#     elif l[0] == '3':
#       print(arr[0])

# Time limit exceeded(heapifyで整えるのに時間かかる?)
# import heapq
#
# if __name__ == '__main__':
#   arr = []
#   for _ in range(int(input())):
#     l = list(map(int, input().split()))
#     if l[0] == 1:
#       heapq.heappush(arr, l[1])
#     elif l[0] == 2:
#       arr.remove(l[1])
#       heapq.heapify(arr)
#     elif l[0] == 3:
#       print(arr[0])

import heapq

if __name__ == '__main__':
  arr = []
  lookup = set()
  for _ in range(int(input())):
    l = list(map(int, input().split()))
    if l[0] == 1:
      heapq.heappush(arr, l[1])
      lookup.add(l[1])
    elif l[0] == 2:
      lookup.discard(l[1])
    elif l[0] == 3:
      while arr[0] not in lookup:
        heapq.heappop(arr)
      print(arr[0])
