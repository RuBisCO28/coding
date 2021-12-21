def rotateLeft(d, arr):
  answer = [0] * len(arr)
  s = len(arr)
  for i in range(s):
    pos = i - d + s
    if pos == s:
      answer[0] = arr[i]
    elif pos > s:
      answer[i-d] = arr[i]
    else:
      print(i,i-d+s)
      answer[i-d+s] = arr[i]
  return answer


if __name__ == '__main__':
  arr = [1,2,3,4,5]
  d = 4
  # arr = [41,73,89,7,10,1,59,58,84,77,77,97,58,1,86,58,26,10,86,51]
  # d = 10
  print(rotateLeft(d, arr))
