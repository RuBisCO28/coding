def plusMinus(arr):
  plus_num = 0
  minius_num = 0
  zero_num = 0
  answer = []
  for i in range(len(arr)):
    if arr[i] > 0:
      plus_num += 1
    if arr[i] == 0:
      zero_num += 1
    if arr[i] < 0:
      minius_num += 1
  answer = [plus_num, minius_num, zero_num]
  for j in range(3):
    print("{0:.6f}".format(answer[j]/len(arr)))

if __name__ == "__main__":
  arr = [-4, 3, -9, 0, 4, 1]
  print(plusMinus(arr))
