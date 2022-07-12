# ペア和のK以上の中での最小値（再掲）
# N個の整数a0,a1,...,aN－1と，N個の整数b0,b1,...,bN－1が与えられます
# ２組の整数列からそれぞれ１個ずつ整数を選んで和をとります
# その和として考えられる値のうち，整数K以上の範囲内での最小値を求めてください

# 上記問題をいいかえると
# N個の正の整数b0,b1,...,bN－1が与えられます
# このうちK-ai以上の範囲内での最小値を求めてください
# O(N^2) => O(NlogN)

import bisect

def pair_sum(a, b):
  K = 10
  min_v = 10000000000
  arr = []
  for i in b:
    bisect.insort_left(arr, i)
  for i in range(len(a)):
    iter = bisect.bisect_left(arr, K - a[i])
    print(a[i],iter,arr[iter])
    if a[i] + arr[iter] < min_v:
      min_v = a[i] + arr[iter]
  return min_v

if __name__ == "__main__":
  a = [8,5,4]
  b = [4,1,9]
  print(pair_sum(a,b))

# 8,4 => 12
# 1,4,9
# 1,4,9 10-8=2, 2より上の最小値4, iter=1, 8+4=12
