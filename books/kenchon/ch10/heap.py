
def min_heapify(arr, i):
  left = 2 * i + 1
  right = 2 * i + 2
  length = len(arr) - 1
  smallest = i

  if left <= length and arr[i] > arr[left]:
    smallest = left
  if right <= length and arr[smallest] > arr[right]:
    smallest = right
  if smallest != i:
    arr[i], arr[smallest] = arr[smallest], arr[i]
    min_heapify(arr, smallest)

def build_min_heap(arr):
  for i in reversed(range(len(arr)//2)): # n//2を根ノードに向かって走査
    min_heapify(arr,i)

if __name__ == "__main__":
  arr = [1,9,8,2,3,10,14,7,16,4]
  build_min_heap(arr)
  print(arr)
