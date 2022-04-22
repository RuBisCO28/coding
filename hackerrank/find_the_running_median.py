# time limit exceeded
# def runningMedian(a):
#   arr = sorted(a)
#   answer = []
#   for i in range(len(a)-1,-1,-1):
#     j = len(arr) // 2
#     # print(j,arr)
#     if len(arr) % 2 != 0:
#       answer.append(float(arr[j]))
#     else:
#       ave = (arr[j] + arr[j-1]) / 2
#       answer.append(ave)
#     arr.remove(a[i])
#   return list(reversed(answer))

# bit演算で右シフトを1ビット行うと値を1/2にできる
def insert(l, n):
  [start, end] = [0, len(l)]
  while start < end:
    mid = (start + end) >> 1
    if(l[mid] <= n):
      start = mid + 1
    else:
      end = mid
  l.insert(start, n)
  print(l)

def getMedian(l):
  if len(l) % 2 == 1:
    return l[len(l) >> 1]
  return (l[(len(l) >> 1) - 1] + l[len(l) >> 1]) / 2

def runningMedian(a):
  result = []
  l = []
  for i in a:
    insert(l, i)
    result.append(getMedian(l))
  return result

if __name__ == "__main__":
  a = [12, 4, 5, 3, 8, 7]
  print(runningMedian(a))

