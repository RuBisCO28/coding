# 計算量
## 計算量とO記法
- `アルゴリズムAの計算時間T(N)がおおむねP(N)に比例する`ということをT(N)＝O(P(N))であると表し，計算量はO(P(N))である

## 計算量の実践的な求め方
- あるアルゴリズムの計算時間T(N)が`T(N) = 3N^2 + 5N + 100`と表されるとき，T(N)はおおむねN^2に比例するO(N^2)
- 定数倍や低次の項目の影響を受けないように考えることで、for文の反復回数を評価することができる

## 計算時間
- $1000N$             : O($N$)  
- $5N^2 + 10N + 7$    : O($N^2$)
- $4N^2 + 3N\sqrt{N}$ : O($N^2$)
- $N\sqrt{N}+5NlogN$  : O($N\sqrt{N}$)
- $2^N+N^{2019}$      : O($2^N$)
- $1+\frac{1}{2}+...+\frac{1}{N}<=1+\int^{N}_{1}\frac{1}{x}dx=logN+1$ : O($logN$)

