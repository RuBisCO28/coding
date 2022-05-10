# def get_unique_list(seq):
#   seen = []
#   return [x for x in seq if x not in seen and not seen.append(x)]

# def shortPalindrome(s):
#   arr = []
#   for i in range(len(s)):
#     for j in range(i, len(s)):
#       if i != j and s[i] == s[j]:
#         arr.append([i,j])
#   t = []
#   for i in range(len(arr)):
#     for j in range(i,len(arr)):
#       if i != j:
#         if arr[i][1] < arr[j][0] and s[arr[i][1]] == s[arr[j][0]] and s[arr[i][0]] == s[arr[j][1]]:
#           t.append([arr[i][0],arr[i][1],arr[j][0],arr[j][1]])
#         if arr[i][0] < arr[j][0] and arr[j][1] < arr[i][1] and s[arr[i][0]] == s[arr[i][1]] and s[arr[j][0]] == s[arr[j][1]]:
#           t.append([arr[i][0], arr[j][0], arr[j][1], arr[i][1]])
#         if arr[j][0] < arr[i][0] and arr[i][1] < arr[j][1] and s[arr[i][0]] == s[arr[i][1]] and s[arr[j][0]] == s[arr[j][1]]:
#           t.append([arr[j][0], arr[i][0], arr[i][1], arr[j][1]])
#         if arr[j][1] < arr[i][0] and s[arr[i][1]] == s[arr[j][0]] and s[arr[i][0]] == s[arr[j][1]]:
#           t.append((arr[j][0], arr[j][1], arr[i][0], arr[i][1]))
#   return len(get_unique_list(t)) % (1000000000 + 7)

def shortPalindrome(s):
  arr1 = [0]*26
  arr2 = [[0]*26 for i in range(26)]
  arr3 = [0]*26
  ans = 0
  for i in range(len(s)):
    idx = ord(s[i]) - ord('a')
    ans += arr3[idx]
    for j in range(26):
      arr3[j] += arr2[j][idx]
    for j in range(26):
      arr2[j][idx] += arr1[j]
    arr1[idx] += 1
  return ans % (10**9+7)

if __name__ == "__main__":
  s = "abbaab"
  s = "ghhggh"
  s = "kkkkkkz"
  s = "akakak"
  print(shortPalindrome(s))
