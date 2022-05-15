import math
# 1: 4, 2: 3, 3: 2, 4: 1, 5: 0, 6: 4, 7: 3, 8: 2, 9: 1, 0: 0

def gradingStudents(grades):
  answer = []
  for i in range(len(grades)):
    next_mul_val = 5 * (math.floor(grades[i] / 5) + 1)
    if next_mul_val >= 37:
      if next_mul_val - grades[i] < 3:
        answer.append(next_mul_val)
      else:
        answer.append(grades[i])
    else:
      answer.append(grades[i])
  return answer

if __name__ == "__main__":
  grades = [73, 67, 38, 33]
  print(gradingStudents(grades))
