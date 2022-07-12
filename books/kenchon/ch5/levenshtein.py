## 編集距離
# ２つの文字列S,Tが与えられます．Sに以下の３通りの操作を繰り返し施すことでTに変換したいものとします
# そのような一連の操作のうち，操作回数の最小値を求めてください．なお，この最小値をSとTとの編集距離とよびます
# 変更：S中の文字を１つ選んで任意の文字に変更する
# 削除：S中の文字を１つ選んで削除する
# 挿入：Sの好きな箇所に好きな文字を１文字挿入する

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
