def superReducedString(s):
  arr = list(s)
  while True:
    l = len(arr)
    print(l, arr)
    for i in range(l):
      if (i+1) != l:
        if arr[i] == arr[i+1]:
          arr.pop(i)
          arr.pop(i)
          break
    if len(arr) == l:
      if l == 0:
        return "Empty String"
      else:
        return ''.join(arr)

if __name__ == '__main__':
  s = "aaabccddd"
  s = "abba"
  print(superReducedString(s))



# aaabccddd
# abccddd
# abddd
# abd
