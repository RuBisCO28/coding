def rotate_row(matrix, i):
  tmp = []
  for j in range(len(matrix)):
    if j == i:
      tmp.append(matrix[i][::-1])
    else:
      tmp.append(matrix[j])
  return tmp

def rotate_column(matrix, i):
  tmp = []
  for j in range(len(matrix)):
    if j == i:
      tmp.append(matrix[i][::-1])
    else:
      tmp.append(matrix[j])
  return tmp

def flip(matrix):
  for i in range(len(matrix)):
    tmp = rotate_row(matrix, i)
    print(tmp)
    print("\n")

if __name__ == '__main__':
  matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
  flip(matrix)
