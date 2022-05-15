def diagonalDifference(arr):
  x = 0
  y = 0
  j = len(arr) - 1
  for i in range(len(arr)):
    x += arr[i][i]
    y += arr[i][j]
    j -= 1
  return abs(x-y)

if __name__ == "__main__":
  arr = [[11,2,4],[4,5,6],[10,8,-12]]
  print(diagonalDifference(arr))
