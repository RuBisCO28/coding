# 再帰と分割統治法
## 再帰
- N＝0の場合は再帰呼び出しを行わず直接0を返している(ベースケースに対する処理)
  - この処理を行わないと，再帰呼び出しを無限に繰り返すことになります
- 再帰呼び出しを行ったときの引数が，ベースケースに近付くようにすること
```python
def recursion(n):
  print("called {}".format(n))
  if n == 0: return 0

  result = n + recursion(n-1)
  print("result {}".format(result))

  return result
```

## ユークリッドの互除法
- 2つの整数m,nの最大公約数を求める
- mをnで割ったときの余りをrとしたとき下記が成り立つ
  - GCD(m,r) = GCD(n,r)
- rが0であればnが求める最大公約数,rが0でないならm<-n,n<-rとしてmをnで割って余りのrを求める作業に戻る
```python
def gcd(m, n):
  if n == 0: return m

  return gcd(n, m % n)
```

## フィボナッチ
- 1,1,2,3,5,8...
- 計算量はO((1+sqrt(5)/2)^N)
```python
def fibo(n):
  print("called {}".format(n))
  if n == 0:
    return 0
  elif n == 1:
    return 1
  result = fibo(n-1) + fibo(n-2)
  print("n: {} result: {}".format(n,result))
  return result
```

## フィボナッチのメモ化
- 上記の方法だと同じ計算をしていて効率が悪い
- 同じ引数に対する答えをメモ化
```python
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
```

## 再帰による部分和問題
- N個の正の整数(a0..aN-1)と正の整数Wが与えられ、N個の正の整数の中から何個かの整数を選んで総和をWとすることができるか判定
- 下記２つの問題に分けられ、Nを小さくしていったときに0個の整数で作れるものの中に0があれば部分和が作れることとなる
  - N－1個の整数a0,a1,...,aN－2からWを作れるかどうか
  - N－1個の整数a0,a1,...,aN－2からW－aN－1を作れるかどうか
- 全体の計算量はO(2^N)
```python
def partial_sum(n,w,a):
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
```

