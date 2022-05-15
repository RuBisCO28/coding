def countingSort(arr):
  n = len(arr)
  answer = [0] * n
  for i in range(n):
    answer[arr[i]] += 1
  return answer

if __name__ == "__main__":
  arr = [1,1,3,2,1]
  print(countingSort(arr))
