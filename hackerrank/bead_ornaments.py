# 同じ色があったときは隣同士になるようにする
# 反転した時同じであれば除く

from operator import mul
from functools import reduce

def beadOrnaments(b):
  return int((reduce(mul, map(lambda x: x ** (x - 1), b), 1) * (sum(b) ** (len(b) - 2))) % (7 + 10 ** 9))

if __name__ == '__main__':
  b = [2,2]
  print(beadOrnaments(b))
