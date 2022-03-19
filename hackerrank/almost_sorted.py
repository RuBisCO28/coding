def almostSorted(arr):
  arr_s = sorted(arr)
  dfi = [i for i in range(len(arr)) if (arr[i] - arr_s[i]) != 0]
  # print(dfi)
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
  arr = [1,2]
  arr = [4,2]
  arr = [1,5,4,3,2,6]
  arr = [3,1,2]
  print(almostSorted(arr))

