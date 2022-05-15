# This solution is also passed
# def lonelyinteger(a):
#   flag = [0] * len(a)
#   for i in range(len(a)):
#     for j in range(len(a)):
#       if i != j and a[i] == a[j]:
#         flag[i] = 1
#   if 0 in flag:
#     return a[flag.index(0)]
#   else:
#     return a[0]

from functools import reduce

# XOR(^)
def lonelyinteger(a):
  lonely_integer = reduce(lambda x, y: x ^ y, a)
  return lonely_integer

if __name__ == "__main__":
  arr = [1,2,3,4,3,2,1]
  print(lonelyinteger(arr))
