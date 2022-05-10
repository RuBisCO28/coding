def fibo(n):
  print("called {}".format(n))
  if n == 0:
    return 0
  elif n == 1:
    return 1
  result = fibo(n-1) + fibo(n-2)
  print("n: {} result: {}".format(n,result))
  return result

if __name__ == "__main__":
  print(fibo(6))
