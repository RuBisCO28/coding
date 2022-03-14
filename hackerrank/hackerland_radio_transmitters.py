# def hackerlandRadioTransmitters(x, k):
#   x = sorted(x)
#   c = 0
#   first_uncovered = 0
#   l = len(x)
#   while first_uncovered < l:
#     i = first_uncovered
#     while i < l and x[i] - x[first_uncovered] <= k:
#       i += 1
#     while first_uncovered < l and x[first_uncovered] - x[i - 1] <= k:
#       first_uncovered += 1
#     c += 1
#   return c

def hackerlandRadioTransmitters(x, k):
  x = sorted(x)
  c = 0
  i = 0
  l = len(x)
  print(x)
  while i < l:
    c += 1
    loc = x[i] + k
    print(x[i],loc)
    while i < l and x[i] <= loc:
      i += 1
    print(i)
    loc = x[i-1] + k
    while i < l and x[i] <= loc:
      i += 1
    print(i)
  return c

if __name__ == '__main__':
  k = 2
  x = [7,2,4,6,5,9,12,11]
  # k = 1
  # x = [1,2,3,4,5]
  print(hackerlandRadioTransmitters(x, k))
