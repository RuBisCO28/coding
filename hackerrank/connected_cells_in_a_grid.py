n = 4
m = 4
# num = 0

# def label(matrix,row,col,num):
#   print(num)
#   matrix[row][col] = num
#   for i in range(-1,2):
#     for j in range(-1,2):
#       if matrix[row+i][col+j] == 1:
#         label(matrix,row+i,col+j,num)

# def connectedCell(matrix):
#   matrix.insert(0, [0 for i in range(len(matrix[0]))])
#   matrix.append([0 for i in range(len(matrix[0]))])
#   for i in range(n+2):
#     matrix[i].insert(0,0)
#     matrix[i].append(0)
#   num = 1
#   print(matrix)
#   for i in range(n+2):
#     for j in range(m+2):
#       if matrix[i][j] == 1:
#         num += 1
#         print(num)
#         label(matrix,i,j,num)
#   return num

## NO
# def dfs(matrix,y,x):
#   matrix[y][x] = 0
#   for dx in range(-1,2):
#     for dy in range(-1,2):
#       ny = y + dy
#       nx = x + dx

#       if 0 <= nx < n and 0 <= ny < m and matrix[ny][nx] == 1:
#         dfs(matrix,ny,nx)
#   return

# def connectedCell(matrix):
#   cnt = 0
#   for i in range(m):
#     for j in range(n):
#       if matrix[i][j] == 1:
#         cnt += 1
#         dfs(matrix, i, j)
#   return cnt

## NO
# def dfs(matix, i, j, m, n, size):
#   matrix[i][j] = 0
#   dis = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
#   for di in dis:
#     n_i = i + di[0]
#     n_j = j + di[1]
#     if 0 <= n_i < m and 0 <= n_j < n and matrix[n_i][n_j] == 1:
#       size = dfs(matrix, n_i, n_j, m, n, size+1)
#   return size

# def connectedCell(matrix):
#   max_cnt = 0
#   for i in range(m):
#     for j in range(n):
#       if matrix[i][j] == 1:
#         size = dfs(matrix, i, j, m, n, 1)
#         max_cnt = max(size, max_cnt)
#   return max_cnt

## OK
# def connectedCell(matrix):
#   mx = 0
#   filled = [(i, j) for i, row in enumerate(matrix) for j,n in enumerate(row) if n]
#   while filled:
#     region = [filled.pop()]
#     count = 0
#     while region:
#       n = region.pop()
#       count += 1
#       for f in list(filled):
#         if abs(n[0] - f[0]) <= 1 and abs(n[1]-f[1]) <= 1:
#           region.append(f)
#           filled.remove(f)
#     else:
#       mx = max(mx, count)
#   return mx

## OK
def connected(matrix, i, j):
  if not (0 <= i < len(matrix)) or not (0 <= j < len(matrix[0])):
    return 0

  if matrix[i][j] != 1:
    return 0

  result = 1
  matrix[i][j] = 0

  for ii in range(i-1, i+2):
    for jj in range(j-1, j+2):
      if i != ii or j != jj:
        result += connected(matrix, ii, jj)

  return result

def connectedCell(matrix):
  max_cnt = 0
  for i in range(m):
    for j in range(n):
      max_cnt = max(max_cnt, connected(matrix, i, j))
  return max_cnt

if __name__ == '__main__':
  matrix = [[1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
  print(connectedCell(matrix))


