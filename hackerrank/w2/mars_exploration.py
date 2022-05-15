def marsExploration(s):
  arr = list(s)
  answer = 0
  for i in range(len(arr)):
    if i % 3 == 0 and arr[i] != 'S':
      answer += 1
    elif i % 3 == 1 and arr[i] != 'O':
      answer += 1
    elif i % 3 == 2 and arr[i] != 'S':
      answer += 1
  return answer

if __name__ == "__main__":
  s ="SOSSPSSQSSOR"
  print(marsExploration(s))
