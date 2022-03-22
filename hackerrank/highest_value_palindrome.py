def highestValuePalindrome(s, n, k):
  lo = 0
  hi = n - 1
  arr = list(s)
  diff = 0

  for i in range(n//2):
    if arr[i] != arr[n-i-1]:
      diff += 1

  if diff > k:
    return '-1'

  while(hi >= lo):
    if k <= 0:
      break

    if arr[lo] == arr[hi]:
      if k > 1 and (k-2) >= diff and arr[lo] != '9':
        arr[lo] = '9'
        arr[hi] = '9'
        k -= 2
    else:
      if (k > 1 and (k-2) >= diff -1):
        if arr[lo] != '9':
          arr[lo] = '9'
          k -= 1
        if arr[hi] != '9':
          arr[hi] = '9'
          k -= 1
      else:
        if arr[lo] > arr[hi]:
          arr[hi] = arr[lo]
        else:
          arr[lo] = arr[hi]
        k -= 1
      diff -= 1

    if lo == hi and k > 0:
      arr[lo] = '9'
      k -= 1

    lo += 1
    hi -= 1

  return ''.join(arr)

if __name__ == '__main__':
  s = '3943'
  n = 4
  k = 1
  s = '092282'
  n = 6
  k = 3
  print(highestValuePalindrome(s, n, k))

# 違ったら結局変えないとだめ
# ただし片方だけ変えるのOK
# 同じだったら一旦スルーしてあとで余裕があれば端から9にしていく感じ?
# 奇数だったら真ん中は変える余裕あれば9にすると必要?


# 片方のうち大きい方に合わせて変える
# 両方9に変える

# 092282

# 292282

# 292292

# ***
# 992289
# 992299


