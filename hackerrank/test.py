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

def almostSorted(arr):
  arr_s = sorted(arr)
  dfi = [i for i in range(len(arr)) if (arr[i] - arr_s[i]) != 0]
  print(dfi)
  l = len(dfi)
  if l == 0:
    print("yes")
  elif l == 2:
    print("yes")
    print("swap", dfi[0]+1, dfi[1]+1)
  elif sorted(arr[dfi[0]:dfi[l-1]+1]) == list(reversed(arr[dfi[0]:dfi[l-1]+1])):
    print("yes")
    print("reverse", dfi[0]+1, dfi[l-1]+1)
  else:
    print("no")

if __name__ == '__main__':
  k = 2
  arr = [1,5,3,4,2]
  print(pairs(k, arr))
  arr = [1,2]
  arr = [4,2]
  arr = [1,5,4,3,2,6]
  arr = [3,1,2]
  print(almostSorted(arr))

