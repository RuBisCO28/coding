# N個の正の整数a0,a1,...,aN－1が与えられます
# これらに対して「N個の整数がすべて偶数ならば２で割った値に置き換える」という操作を，操作が行えなくなるまで繰り返します
# 何回の操作を行うことになるかを求めるアルゴリズムを設計してください
# 出典:AtCoderBeginnerContest081BShiftOnly

def how_many_times(n):
  exp = 0
  while n % 2 == 0:
    n /= 2
    exp += 1
  return exp

def shift_only(a):
  result = 1234567
  for i in a:
    result = min(result, how_many_times(i))
  return result

if __name__ == "__main__":
  a = [8, 12, 40]
  print(shift_only(a))
