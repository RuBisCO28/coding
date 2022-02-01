import copy

r = 6
c = 7

def markBomb(og, ng):
  for i in range(r):
    for j in range(c):
      if og[i][j] == 'O':
        # center
        ng[i][j] = '-'
        # top
        if i > 0:
          ng[i-1][j] = '-'
        # bottom
        if i < r - 1:
          ng[i+1][j] = '-'
        # left
        if j > 0:
          ng[i][j-1] = '-'
        # right
        if j < c - 1:
          ng[i][j+1] = '-'
  return ng

def plantBomb(ng):
  for i in range(r):
    for j in range(c):
      if ng[i][j] == '.':
        ng[i][j] = 'O'
  return ng

def detonateBomb(ng):
  for i in range(r):
    for j in range(c):
      if ng[i][j] == '-':
        ng[i][j] = '.'
  return ng

def bomberMan(n, grid):
  og = []
  ng = []
  answer = []
  for i in range(r):
    og.append(list(grid[i]))
    print(og[i])
  for i in range(r):
    ng.append(list(grid[i]))
  print("-------------")
  for i in range(1, n + 1):
    if i % 3 == 1:
      ng = markBomb(og, ng)
      for i in range(r):
        print(ng[i])
      print("-------------")
    elif i % 3 == 2:
      ng = plantBomb(ng)
      for i in range(r):
        print(ng[i])
      print("-------------")
    elif i % 3 == 0:
      ng = detonateBomb(ng)
      og = []
      for i in range(r):
        og.append(copy.deepcopy(ng[i]))
        print(og[i])
      print("-------------")
  for i in range(r):
    ng[i] = ['.' if j== '-' else j for j in ng[i]]
    answer.append(''.join(ng[i]))
    print(answer[i])
  return answer

if __name__ == '__main__':
  n = 3
  grid =['.......', '...O...', '....O..',\
         '.......', 'OO.....', 'OO.....']
  result = bomberMan(n, grid)

