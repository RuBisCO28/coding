def getTotalX(a, b):
  answer = 0
  n = len(a)
  m = len(b)
  for i in range(a[n-1],b[0]+1):
    cnt = 0
    flag = True
    for j in range(m):
      if b[j] % i == 0:
        cnt += 1
    if cnt == len(b):
      for k in range(n):
        if i % a[k] != 0:
          flag = False
      if flag:
        answer += 1
  return answer

if __name__ == '__main__':
  a = [3, 4]
  b = [24, 48]
  # a = [2, 4]
  # b = [16, 32, 96]
  print(getTotalX(a,b))
