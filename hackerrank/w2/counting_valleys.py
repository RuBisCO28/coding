def countingValleys(steps, path):
  answer = 0
  pos = 0
  flag = False
  for i in range(steps):
    if path[i] == 'U':
      pos += 1
    else:
      pos -= 1
    if pos < 0 and flag == False:
      flag = True
      answer += 1
    if pos == 0 and flag == True:
      flag = False
  return answer

if __name__ == "__main__":
  steps = 8
  path = "UDDDUDUU"
  print(countingValleys(steps, path))
