# O(logN)
def binary_search(arr, key):
  left = 0
  right = len(arr) - 1
  while right >= left:
    mid = left + (right - left) // 2
    if arr[mid] == key:
      return mid
    elif arr[mid] > key:
      right = mid - 1
    elif arr[mid] < key:
      left = mid + 1
  return -1

if __name__ == "__main__":
  arr = [3,5,8,10,14,17,21,39]
  key = 17
  print(binary_search(arr, key))
