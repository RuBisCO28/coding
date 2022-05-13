def partial_sum(n,w,a):
  print(n,w,a)
  if n == 0:
    if w == 0:
      return True
    else:
      return False
  # a[n-1]を選ばない
  if (partial_sum(n-1,w,a)): return True

  # a[n-1]を選ぶ
  if (partial_sum(n-1,w-a[n-1],a)): return True

  # どちらもfalseはfalse
  return False

if __name__ == "__main__":
  n = 4
  w = 14
  a = 3,2,6,5
  print(partial_sum(n,w,a))
