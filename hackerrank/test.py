n = 8

def minimumBribes(q):
  ori = [i for i in range(1,n+1)]
  answer = 0
  for i in range(n):
    print(i, ori[i], q[i])
    print("before", ori)
    if ori[i] != q[i]:
      m = abs(ori.index(q[i])-i)
      answer += m
      if m <= 2:
        tmp = []
        tmp += ori[:i]
        tmp += [ori[i+m]]
        tmp += ori[i:i+m] 
        if i+m != n - 1:
          tmp += ori[i+m+1:]
          print(ori[:i], ori[i+m], ori[i:i+m], ori[i+m+1:], m)
        else:
          print(ori[:i], ori[i+m], ori[i:i+m], m)
        ori = tmp
      else:
        return 'Too chaotic'
    print("after", ori)
  return answer

if __name__ == '__main__':
  q = [5,1,2,3,7,8,6,4]
  q = [1,2,5,3,7,8,6,4]
  print("goal", q)
  print("**********")
  result = minimumBribes(q)
  print(result)

