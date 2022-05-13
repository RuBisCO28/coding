def breakingRecords(scores):
  min_score = scores[0]
  max_score = scores[0]
  min_brk = 0
  max_brk = 0
  for i in range(len(scores)):
    if scores[i] > max_score:
      max_brk += 1
      max_score = scores[i]
    if scores[i] < min_score:
      min_brk += 1
      min_score = scores[i]
  return [max_brk, min_brk]

if __name__ == "__main__":
  scores = [12, 24, 10, 24]
  print(breakingRecords(scores))
