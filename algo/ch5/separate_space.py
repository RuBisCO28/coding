## 区間分割最適化
# N個の要素が１列に並んでいて，これをいくつかの区間に分割したいものとします
# 各区間[l,r)にはスコアcl,rが付いているとします
# KをN以下の正の整数としてK＋1個の整数t0,t1,...,tKを0＝t0＜t1＜...tK＝Nを満たすようにとったとき
# 区間分割[t0,t1),[t1,t2),...,[tK－1,tK)のスコアによって定義します
# N要素の区間分割の仕方をすべて考えたときの，考えられるスコアの最小値を求めてください
# たとえばN＝10, K＝4, t＝(0,3,7,8,10)とした場合のスコアはc0,3＋c3,7＋c7,8＋c8,10となります

def separate_space(n, k, t):
  dp = [[0] * (m+1) for _ in range(n+1)]

  for i in range(n + 1):
    dp[i][0] = i

  for j in range(m + 1):
    dp[0][j] = j

  for i in range(n+1):
    for j in range(n+1):
      cost = 0 if s[i-1] == t[j-1] else 1
      dp[i][j] = min(dp[i-1][j] + 1, # insertion
                     dp[i][j-1] + 1, # deletion
                     dp[i-1][j-1] + cost # replacement
                     )
  return dp[-1][-1]

if __name__ == "__main__":
  n = 10
  k = 4
  t = [0,3,7,8,10]
  print(separate_space(n, k, t))
