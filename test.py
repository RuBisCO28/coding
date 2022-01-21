def calc(t1, t2):
  return t1 + (t2 * t2)

def fibonacciModified(t1, t2, n):
  a = t1
  b = t2
  c = 0
  for i in range(n-2):
    c = calc(a, b)
    a = b
    b = c
  return c

if __name__ == '__main__':
  t1 = 0
  t2 = 1
  n = 6
  print(fibonacciModified(t1, t2, n))

