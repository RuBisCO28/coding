if __name__ == '__main__':
  arr = []
  nq = int(input())
  for _ in range(nq):
    l = str(input()).split()
    if l[0] == '1':
      arr.append(l[1])
    elif l[0] == '2':
      arr.pop(0)
    elif l[0] == '3':
      print(arr[0])
