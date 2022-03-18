# Timelimit exceeded
# def solve(arr, queries):
#   answer = []
#   for i in queries:
#     min_v = 999999999999
#     for j in range(len(arr)-i+1):
#       if i == 1:
#         if min_v > arr[j]:
#           min_v = arr[j]
#       else:
#         if min_v > max(arr[j:j+i]):
#           min_v = max(arr[j:j+i])
#     answer.append(min_v)
#   return answer

def solve(arr, queries):
  answer = []
  for d in queries:
    maxes = []
    was_first = False
    for j in range(len(arr)-d+1):
      if j == 0 or was_first == True:
        # print(arr[i:i+d])
        maxes.append(max(arr[j:j+d]))
      else:
        # print("max({}, {})".format(maxes[-1], arr[i+d-1]))
        maxes.append(max(maxes[-1], arr[j+d-1]))

      if maxes[-1] == arr[j]:
        was_first = True
      else:
        was_first = False
    answer.append(min(maxes))
  return answer

if __name__ == '__main__':
  k = 2
  arr = [33,11,44,11,55]
  queries = [1,2,3,4,5]
  print(solve(arr, queries))

# 1,2,3,4,5
# 11,33,44,44,55
