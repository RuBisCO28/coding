def rotate_row(matrix, i):
  matrix[i] = matrix[i][::-1]
  print(matrix)

def flip(matrix):
  for i in range(len(matrix)):
    rotate_row(matrix, i)

if __name__ == '__main__':
  matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
  flip(matrix)
