import math

def findMedian(arr):
  arr.sort()
  idx = math.floor(len(arr)/2)
  return(arr[idx])

if __name__ == "__main__":
  arr = [5,3,1,2,4]
  print(findMedian(arr))
