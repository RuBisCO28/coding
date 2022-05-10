def tribo(n):
  print("called {}".format(n))
  if n == 0:
    return 0
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  result = tribo(n-1) + tribo(n-2) + tribo(n-3)
  print("n: {} result: {}".format(n,result))
  return result

if __name__ == "__main__":
  print(tribo(6))
