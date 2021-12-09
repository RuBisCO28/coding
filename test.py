# def rotate_row(matrix, i):
#   tmp = []
#   for j in range(len(matrix)):
#     if j == i:
#       tmp.append(matrix[i][::-1])
#     else:
#       tmp.append(matrix[j])
#   return tmp

# def rotate_column(matrix, i):
#   tmp = []
#   for j in range(len(matrix)):
#     if j == i:
#       tmp.append(matrix[i][::-1])
#     else:
#       tmp.append(matrix[j])
#   return tmp

# def flip(matrix):
#   for i in range(len(matrix)):
#     tmp = rotate_row(matrix, i)
#     print(tmp)
#     print("\n")

def flip(matrix):
  sums = 0
  n = int(len(matrix[0]) / 2)
  for i in range(n):
    for j in range(n):
      l = []
      l.append(matrix[i][j]) # current matrix
      l.append(matrix[2 * n - 1 - i][j])  # bottom left
      l.append(matrix[i][2 * n - 1- j]) # top right
      l.append(matrix[2* n - 1 - i][2 * n - 1- j]) # bottom right

      maxv = max(l)
      sums += maxv

  return sums

if __name__ == '__main__':
  matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
  print(flip(matrix))

