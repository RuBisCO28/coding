# 動的計画法
## 例題
- 下記例題において、頂点iにいたる最小コストを求める」という「大きな」問題を２つの「小さな」部分問題に分解
  - 頂点i－1にいたる最小コストを求める（頂点i－1からiヘ移動する場合）
  - 頂点i－2にいたる最小コストを求める（頂点i－2からiへ移動する場合）
- 「元の問題の最適性を考えるときに，小さな部分問題についても最適性が要請される」という構造を，部分構造最適性(optimal substructure)とよぶ
- このような構造を利用して各部分問題に対する最適値を順に決定していく手法を動的計画法(dynamic programming,DP)とよぶ
```python
# N個の足場があって，i(＝0,1,...,N－1)番目の足場の高さはhiで与えられます
# 最初０番目の足場にカエルがいて，以下のいずれかの行動を繰り返してN－1番目の足場を目指します
# 足場iから足場i＋1へと移動する(コストは|hi－hi＋1|)足場iから足場i＋2へと移動する(コストは|hi－hi＋2|)
# カエルがN－1番目の足場にたどり着くまでに要するコストの総和の最小値を求めてください

def frog(trees):
  arr = []
  for i in range(len(trees)):
    if i == 0:
      arr.append(0)
    elif i == 1:
      arr.append(trees[i] - trees[i-1])
    else:
      arr.append(min(abs(trees[i] - trees[i-1]) + arr[i-1],abs(trees[i] - trees[i-2]) + arr[i-2]))
  return arr[-1]
```

## ナップザック問題
- N個の品物があり，i(＝0,1,...,N－1)番目の品物の重さはweight i，価値はvalue iで与えられます
- このN個の品物から，重さの総和がWを超えないように，いくつか選びます
- 選んだ品物の価値の総和として考えられる最大値を求めてください(ただし，Wやweight iは０以上の整数とします)
- 品物: (weight,value)＝{(2,3),(1,2),(3,6),(2,1),(1,3),(5,85)}
```python
# 部分和問題と同じく0 - i-1番目の品物からいくつか選んだ後にi番目の品物を選ぶ、選ばないという2通りの選択肢があるのでこれを解いてく
# dp[i][w]: 最初のi個の品物[0, 1, ... i-1]までの中から重さがwを超えないように選んだときの価値の総和の最大値
# i番目の品物を選ぶとき: chmax(dp[i+1][w], dp[i][w-weight[i]]+value[i])
# i番目の品物を選ばないとき: chmax(dp[i+1][w], dp[i][w])
# 計算量はO(2^N)->O(NW)ですむようになる

def knapsack(items, w):
  n = len(items)
  dp = [[0] * (w + 1) for _ in range(n + 1)]
  for i in range(n):
    for j in range(w + 1):
      if j < items[i][0]:
        dp[i+1][j] = dp[i][j]
      else:
        dp[i+1][j] = max(dp[i][j], dp[i][j - items[i][0]]+items[i][1])
  print(dp[n][w])
```

## 編集距離
# ２つの文字列S,Tが与えられます．Sに以下の３通りの操作を繰り返し施すことでTに変換したいものとします
# そのような一連の操作のうち，操作回数の最小値を求めてください．なお，この最小値をSとTとの編集距離とよびます
# 変更：S中の文字を１つ選んで任意の文字に変更する
# 削除：S中の文字を１つ選んで削除する
# 挿入：Sの好きな箇所に好きな文字を１文字挿入する

```python
# dp[i][j]←Sの最初のi文字分と，Tの最初のj文字分との間の編集距離
# 変更操作(Sのi文字目とTのj文字目とを対応させる)：
# S[i－1]＝T[j－1]のとき:コストを増やさずに済みますのでchmin(dp[i][j],dp[i1][j1])
# S[i－1]≠T[j－1]のとき:変更操作が必要ですのでchmin(dp[i][j],dp[i-1][j-1]+1)
# 削除操作(Sのi文字目を削除)：
# Sのi文字目を削除する操作を行いますのでchmin(dp[i][j],dp[i1][j]+1)
# 挿入操作(Tのj文字目を削除)：
# Tのj文字目を削除する操作を行いますのでchmin(dp[i][j],dp[i][j1]+1)
def levenshtein(s, t):
  n, m = len(s), len(t)
  dp = [[0] * (m+1) for _ in range(n+1)]

  for i in range(n + 1):
    dp[i][0] = i

  for j in range(m + 1):
    dp[0][j] = j

  for i in range(1, n+1):
    for j in range(1, m+1):
      cost = 0 if s[i-1] == t[j-1] else 1
      dp[i][j] = min(dp[i-1][j] + 1, # insertion
                     dp[i][j-1] + 1, # deletion
                     dp[i-1][j-1] + cost # replacement
                     )
  return dp[-1][-1]

if __name__ == "__main__":
  s = 'logistic'
  t = 'algorithm'
  print(levenshtein(s, t)) 
```

## 区間分割最適化
# N個の要素が１列に並んでいて，これをいくつかの区間に分割したいものとします
# 各区間[l,r)にはスコアcl,rが付いているとします
# KをN以下の正の整数としてK＋1個の整数t0,t1,...,tKを0＝t0＜t1＜...tK＝Nを満たすようにとったとき
# 区間分割[t0,t1),[t1,t2),...,[tK－1,tK)のスコアによって定義します
# N要素の区間分割の仕方をすべて考えたときの，考えられるスコアの最小値を求めてください
# たとえばN＝10, K＝4, t＝(0,3,7,8,10)とした場合のスコアはc0,3＋c3,7＋c7,8＋c8,10となります
