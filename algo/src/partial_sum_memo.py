# 部分和問題に対する再帰関数を用いる計算量O(2N)のコードに対しメモ化して，O(NW)の計算量で動作するようにしてください

memo = [[-1 for j in range(16)] for i in range(5)]

def partial_sum_memo(n,w,a):
  if n == 0:
    if w == 0:
      return True
    else:
      return False

  # メモをチェック
  if (memo[n][w] != -1): return memo[n][w]

  # a[n-1]を選ばない
  if (partial_sum_memo(n-1,w,a)):
    memo[n][w] = 1
    return True

  # a[n-1]を選ぶ
  if (partial_sum_memo(n-1,w-a[n-1],a)):
    memo[n][w] = 1
    return True

  # どちらもfalseはfalse
  memo[n][w] = 0
  return False

if __name__ == "__main__":
  n = 4
  w = 14
  a = 3,2,6,5
  print(partial_sum_memo(n,w,a))
