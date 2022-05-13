def recursion(n):
  print("called {}".format(n))
  if n == 0: return 0

  result = n + recursion(n-1)
  print("result {}".format(result))

  return result

if __name__ == "__main__":
  recursion(5)
