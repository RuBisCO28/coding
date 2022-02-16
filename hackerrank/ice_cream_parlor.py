def icecreamParlor(m, arr):
  l = len(arr)
  d = {i+1: arr[i] for i in range(l)}
  sd = sorted(d.items(), key=lambda x:x[1], reverse=True)
  answer = []
  for i in range(l):
    if m > sd[i][1]:
      tmp = m - sd[i][1]
      for j in range(i+1, l):
        if sd[j][1] == tmp:
          return sorted([sd[i][0],sd[j][0]])

if __name__ == '__main__':
  m = 4
  arr = [1,4,5,3,2]
  print(icecreamParlor(m, arr))
