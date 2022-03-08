def legoBlocks(n, m):
  mod = 10 ** 9 + 7
  block = [0] * m

  for i in range(min(m, 4)):
    block[i] = 1

  for i in range(m):
    for j in range(1, 5):
      if i + j < m:
        block[i + j] = (block[i + j] + block[i]) % mod
    x = n
    tmp = block[i]
    block[i] = 1
    while x > 0:
      if x % 2 == 1:
        block[i] = (block[i] * tmp) % mod
      tmp = (tmp * tmp) % mod
      x //= 2

  ans = [0] * m
  for i in range(m):
    ans[i] = block[i]
    for j in range(i):
      ans[i] = (ans[i] - ans[j] * block[i - 1 - j]) % mod
  return (ans[m - 1] + mod) % mod

if __name__ == '__main__':
  n,m = 2,2
  n,m = 1,3
  print(legoBlocks(n, m))
