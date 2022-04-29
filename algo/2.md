# 全探索
## 線形探索法
- ひとつひとつの要素を順に調べていく
- N個の整数(a0..aN)と整数値vが与えられたとき、ai = vとなるデータが存在するか判定
- 途中でreturnしても計算量のオーダーは最悪ケースを考えているので変わらずO(N)
```python
def find_value(a, n, v):
  for i in range(n):
    if a[i] == v:
      return True
  return False

def find_min_value(a, n, v):
  min_value = 20000000
  for i in range(n):
    if a[i] < min_value:
      min_value = a[i]
  return min_value
```

## ペアの全探索
- N個の整数(a0..aN-1)とN個の整数(b0..bN-1)が与えられ、2個の整数列から整数を選んで和をとる
- その和の中で整数K以上の範囲内での最小値を求める
- 線形探索でO(N^2), 二分探索でO(NlogN)で解ける
```python
def find_min_sum_pair(n,k,a,b):
  min_sum = 20000000
  for i in range(len(a)):
    for j in range(len(b)):
      pair_sum = a[i] + b[j]
      if k <= pair_sum and pair_sum < min_sum:
        min_sum = pair_sum
  return min_sum
```

## 組み合わせの全探索
- N個の正の整数(a0..aN-1)と正の整数Wが与えられ、N個の正の整数の中から何個かの整数を選んで総和をWとすることができるか判定
- N個の整数からなる集合の部分集合は2^N通り
- ２進数とビット演算を使用する
- `1 << i`で整数iを２進数にしている
- `bit and (1 << i)`で整数iがbitの部分集合に含まれるか判定
```python
def find_partial_sum(n,w,a):
  # 1 << nは2^N個の組み合わせ
  for bit in range(0,(1 << n)):
    sum = 0
    for i in range(n):
      # N = 8, {a0,a2,a3,a6}, bit = 01001101
      # 整数bitを二進法表現で表したときに，そのbitのi桁目が１になっているかどうかを判定
      # 1になっていれば部分集合に含まれるので加算
      if (bit and (1 << i)):
        sum += a[i]
    if sum == w:
      return True
  return False
```
