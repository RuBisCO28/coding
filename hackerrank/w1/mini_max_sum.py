def miniMaxSum(arr):
  sum = 0
  arr.sort()
  for i in range(5):
      sum += arr[i]
  max = sum - arr[0]
  min = sum - arr[4]
  print(min, max)

if __name__ == "__main__":
  arr = [-4, 3, -9, 0, 4, 1]
  print(miniMaxSum(arr))
