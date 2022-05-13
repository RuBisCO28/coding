memo = [-1 for i in range(50)]

def fibo_memo(n):
  print("called {}".format(n))
  if n == 0:
    return 0
  elif n == 1:
    return 1
  if (memo[n] != -1): return memo[n]

  memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
  print("n: {} result: {}".format(n,memo[n]))
  return memo[n]

if __name__ == "__main__":
  print(fibo_memo(6))
