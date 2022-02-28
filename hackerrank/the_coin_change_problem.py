def getWays(n, c):
  table = [0 for k in range(n+1)]
  table[0] = 1
  m = len(c)
  for i in range(0, m):
    for j in range(c[i], n+1):
      table[j] += table[j-c[i]]
  print(table)
  return table[n]

if __name__ == '__main__':
  n = 3
  c = [8,3,1,2]
  n = 10
  c = [2,5,3,6]
  print(getWays(n, c))
