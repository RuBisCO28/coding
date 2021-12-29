
def closestNumbers(arr):
  arr.sort()
  print(arr)
  min_diff = arr[1] - arr[0]
  answer = []
  for i in range(1, len(arr)):
    if arr[i] - arr[i-1] < min_diff:
      min_diff = arr[i] - arr[i-1]
      answer = []
      answer.append(arr[i-1])
      answer.append(arr[i])
    elif arr[i] - arr[i-1] == min_diff:
      min_diff = arr[i] - arr[i-1]
      answer.append(arr[i-1])
      answer.append(arr[i])
  return answer

if __name__ == '__main__':
  arr = [-20,-3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854]
  arr = [-20,-3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854,-520,-470]
  print(closestNumbers(arr))
