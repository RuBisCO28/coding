def migratoryBirds(arr):
  answer = {}
  arr.sort()
  for i in range(len(arr)):
    if i == 0:
      tmp = arr[i]
      answer[str(arr[i])] = 1
    elif arr[i] == tmp:
      answer[str(tmp)] += 1
    elif arr[i] != tmp:
      answer[str(arr[i])] = 1
      tmp = arr[i]
    # print(i, arr[i], tmp, cnt, answer)
  result = [kv for kv in answer.items() if kv[1] == max(answer.values())]
  return int(result[0][0])

if __name__ == '__main__':
  arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
  arr = [1,2,3,4,5,4,3,2,1,3,4]
  print(migratoryBirds(arr))
