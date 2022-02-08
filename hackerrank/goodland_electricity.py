# 1のある箇所で左右にk-1ずつ電力供給できるので次に設置する場所も同じ幅あるとして
# 次の箇所を決め、0の場合は-1して探り、配列の長さを超えてしまった場合は最後の位置から探索開始

def pylons(k, arr):
  print(arr)
  count = i = 0
  loc = i + k - 1
  n = len(arr)
  print("i=", i, ", loc=", loc, ", k=", k, ", c=", count)
  while i < n:
    if arr[loc] == 1:
      i = loc + k
      loc = i + k - 1
      count += 1
      print("1: ", "i=", i, ", loc=", loc, ", c=", count)
      if loc >= n:
        loc = n - 1
    else:
      loc -= 1
      print("0: ", "i=", i, ", loc=", loc, ", c=", count)
      if loc < i - k + 1 or loc < 0:
        return -1
  return count

if __name__ == '__main__':
  k = 2
  arr = [0,1,1,1,1,0]
  k = 3
  arr = [0,1,0,0,0,1,1,1,1,1]
  print(pylons(k, arr))
