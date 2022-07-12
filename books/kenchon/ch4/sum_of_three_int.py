# ２つの正の整数K,Nが与えられます
# 0<=X,Y,Z<=Kを満たす整数(X,Y,Z)の組であってX＋Y＋Z＝Nを満たすものが何通りあるかを求める
# O(N^2)のアルゴリズムを設計してください
# 出典:AtCoderBeginnerContest051BSumofThreeIntegers

if __name__ == "__main__":
  k = 8
  n = 6
  # O(N^3)
  # for x in range(k):
  #   for y in range(k):
  #     for z in range(k):
  #       if x + y + z == n:
  #         print(x,y,z)

  # O(N^2)
  # for i in range(k):
  #   for j in range(k):
  #     if 0 <= n - (i+j) and n - (i+j) <= k:
  #       print(i,j,n - (i+j))

  # M=min(k,n), O(M^2)
  # 求めたいnが小さい場合、n以上k以下の値を足した時点で、超えるので計算する必要がない
  for x in range(min(n,k)+1):
    for y in range(min(n,k)+1):
      z = n - x - y
      if 0 <= z and z <= k:
        print(x,y,z)

