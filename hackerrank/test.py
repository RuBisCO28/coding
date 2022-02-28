
# def getWays(n, c):
#   arr = []
#   for i in range(len(c)):
#     tmp = n
#     while True:
#       if tmp < c[i]:
#         break
#       tmp -= c[i]
#       arr.append(c[i])
#   arr.sort(reverse=True)
#   print(arr)
#   cnt = 0
#   for j in range(len(arr)):

#   return cnt

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


# 6,5,5,3,3,3,2,2,2,2,2
# 6,5,10,3,6,9,2,4,6,8,10

# 10(5,5)
# 10(2,2,2,2,2)
# 6,4(6,2,2)
# 6,4(3,3,2,2)
# 5,3,2
