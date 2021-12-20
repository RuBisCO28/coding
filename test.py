def pickingNumbers(a):
  a.sort()
  cnt = 0
  max_cnt = 0
  for i in range(len(a)):
    cnt = 1
    for j in range(i+1, len(a)):
      if a[j] - a[i] > 1:
        break
      else:
        cnt += 1
    # print(i,a[i],cnt)
    if max_cnt < cnt:
      max_cnt = cnt
  return max_cnt

if __name__ == '__main__':
  # a = [4,6,5,3,3,1]
  a = [1,2,2,3,1,2]
  print(pickingNumbers(a))
