from collections import Counter

def equalStacks(h1, h2, h3):
  arr = []
  tmp = 0
  if sum(h1) == sum(h2) and sum(h2) == sum(h3):
    return sum(h1)
  for i in range(len(h1)-1,-1,-1):
    tmp+=h1[i]
    arr.append(tmp)
  tmp = 0
  for i in range(len(h2)-1,-1,-1):
    tmp+=h2[i]
    arr.append(tmp)
  tmp = 0
  for i in range(len(h3)-1,-1,-1):
    tmp+=h3[i]
    arr.append(tmp)
  c = Counter(arr)
  if 3 in c.values():
    return max([i[0] for i in c.items() if i[1] == 3])
  else:
    return 0

if __name__ == '__main__':
  h1 = [3,2,1,1,1]
  h2 = [4,3,2]
  h3 = [1,1,4,1]
  # h1 = [1,1,1,1,2]
  # h2 = [3,7]
  # h3 = [1,3,1]
  print(equalStacks(h1, h2, h3))

