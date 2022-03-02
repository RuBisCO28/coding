from collections import Counter

def check_valid(s,a,b):
  arr = [s[i] for i in range(len(s)) if s[i] == a or s[i] == b ]
  # print(a,b,''.join(arr))
  for j in range(len(arr)-1):
    if arr[j] == arr[j+1]:
      return 0
  return len(arr)

def alternate(s):
  # print(s)
  arr = list(Counter(s).keys())
  max_length = 0
  for i in range(len(arr)):
    for j in range(i, len(arr)):
      if i != j:
        l = check_valid(list(s),arr[i],arr[j])
        if l > max_length:
          max_length = l
  return max_length

if __name__ == '__main__':
  # s = "beabeefeab"
  # s = "asdcbsdcagfsdbgdfanfghbsfdab"
  s = "asvkugfiugsalddlasguifgukvsa"
  print(alternate(s))
