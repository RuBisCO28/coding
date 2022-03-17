def pairs(k, arr):
  arr.sort()
  # print(arr)
  c = 0
  j = 0
  for i in range(len(arr)):
    while j < len(arr):
      if i != j:
        # print(arr[i],arr[j], j)
        df = arr[j] - arr[i]
        if df > k:
            break
        if df == k:
          c += 1
      j += 1
  return c

if __name__ == '__main__':
  k = 2
  arr = [1,5,3,4,2]
  print(pairs(k, arr))

