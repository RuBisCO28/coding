n = 6

def pylons(k, arr):
  r = k - 1
  for i in range(n):
    if arr[i] == 0:
      if i+r <= n-1:
        print(i, i+r, arr[i:i+r])
      if i-r >= 0:
        print(i-r, i, arr[i-r:i])

if __name__ == '__main__':
  k = 2
  arr = [0,1,1,1,1,0]
  print(pylons(k, arr))

