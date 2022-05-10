# 計算量はO(N)
memo = [-1 for i in range(50)]

def tribo_memo(n):
  print("called {}".format(n))
  if n == 0:
    return 0
  elif n == 1:
    return 0
  elif n == 2:
    return 1

  memo[n] = tribo_memo(n-1) + tribo_memo(n-2) + tribo_memo(n-3)
  print("n: {} result: {}".format(n,memo[n]))
  return memo[n]

if __name__ == "__main__":
  print(tribo_memo(6))
