def gcd(m, n):
  if n == 0: return m

  return gcd(n, m % n)

if __name__ == "__main__":
  print(gcd(51, 15))
