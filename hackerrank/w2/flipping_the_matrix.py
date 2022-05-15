def flip(matrix):
  answer = 0
  n = int(len(matrix[0]) / 2)
  for i in range(n):
    for j in range(n):
      l = []
      l.append(matrix[i][j]) # current value
      l.append(matrix[2 * n - 1 - i][j])  # bottom left
      l.append(matrix[i][2 * n - 1- j]) # top right
      l.append(matrix[2 * n - 1 - i][2 * n - 1 - j]) # bottom right

      answer += max(l)

  return answer

if __name__ == '__main__':
  matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
  print(flip(matrix))
