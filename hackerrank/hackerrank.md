# Permuting Two Arrays
```python
def twoArrays(k, A, B):
  if min([x + y for (x, y) in zip(sorted(A), reversed(sorted(B)))]) >= k:
    return "YES"
  return "NO"
```

# Subarray Division 2
```python
def birthday(s, d, m):
  return sum([1 for i in range(len(s)-m+1) if sum(s[i:i+m])==d])
```

# XOR Strings 3
```python
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res
```

# Sales by Match
```python
def sockMerchant(n, ar):
  answer = 0
  cnt = 0
  ar.sort()
  print(ar)
  for i in range(n):
    if i == 0:
      tmp = ar[i]
      cnt += 1
    elif ar[i] == tmp:
      cnt += 1
      if cnt == 2:
        cnt = 0
        answer += 1
    elif ar[i] != tmp:
      cnt = 1
      tmp = ar[i]
    print(i, ar[i], tmp, cnt, answer)
  return answer
```

# Migratory Birds
```python
def migratoryBirds(arr):
  answer = {}
  arr.sort()
  for i in range(len(arr)):
    if i == 0:
      tmp = arr[i]
      answer[str(arr[i])] = 1
    elif arr[i] == tmp:
      answer[str(tmp)] += 1
    elif arr[i] != tmp:
      answer[str(arr[i])] = 1
      tmp = arr[i]
    # print(i, arr[i], tmp, cnt, answer)
  result = [kv for kv in answer.items() if kv[1] == max(answer.values())]
  return int(result[0][0])
```

# Maximum Perimeter Triangle
```python
def maximumPerimeterTriangle(sticks):
  n = len(sticks)
  answer = [-1]
  sums = 0
  for i in range(n):
    for j in range(i, n):
      if i != j:
        for k in range(j, n):
          if j != k:
            if sticks[i] + sticks[j] > sticks[k] and sticks[i] + sticks[k] > sticks[j] and sticks[k] + sticks[j] > sticks[i]:
              if sums < sticks[i] + sticks[j] + sticks[k]:
                sums = sticks[i] + sticks[j] + sticks[k]
                answer = [sticks[i],sticks[j],sticks[k]]
  return sorted(answer)
```

# Zig Zag Sequence
```python
def findZigZagSequence(a, n):
  a.sort()
  mid = int((n + 1)/2) - 1
  a[mid], a[n-1] = a[n-1], a[mid]

  st = mid + 1
  ed = n - 2
  while(st < ed):
    a[st], a[ed] = a[ed], a[st]
    st = st + 1
    ed = ed - 1
```

# Drawing Book
```python
def pageCount(n, p):
  if n == p:
    return 0
  if n % 2 == 0:
    if n - p > p - 1:
      if n == 2:
        return 0
      if p % 2 == 0:
        return int((p - 1) / 2) + 1
      return int((p - 1) / 2)
    else:
      if p % 2 == 0:
        return int((n - p) / 2)
      return int((n - p) / 2) + 1
  else:
    if n - p > p - 1:
      if n == 3:
        return 0
      if p % 2 == 0:
        return int((p - 1) / 2) + 1
      return int((p - 1) / 2)
    else:
      return int((n - p) / 2)
  ```

# getTotalX
```python
def getTotalX(a, b):
  answer = 0
  n = len(a)
  m = len(b)
  for i in range(a[n-1],b[0]+1):
    cnt = 0
    flag = True
    for j in range(m):
      if b[j] % i == 0:
        cnt += 1
    if cnt == len(b):
      for k in range(n):
        if i % a[k] != 0:
          flag = False
      if flag:
        answer += 1
  return answer
```

# Picking Numbers
```python
def pickingNumbers(a):
  a.sort()
  cnt = 0
  max_cnt = 0
  for i in range(len(a)):
    cnt = 1
    for j in range(i+1, len(a)):
      if a[j] - a[i] > 1:
        break
      else:
        cnt += 1
    # print(i,a[i],cnt)
    if max_cnt < cnt:
      max_cnt = cnt
  return max_cnt
```

# Left Rotation
```python
def rotateLeft(d, arr):
  answer = [0] * len(arr)
  s = len(arr)
  for i in range(s):
    pos = i - d + s
    if pos == s:
      answer[0] = arr[i]
    elif pos > s:
      answer[i-d] = arr[i]
    else:
      answer[i-d+s] = arr[i]
  return answer
```

# Number Line Jumps
```python
def kangaroo(x1, v1, x2, v2):
  if v2 - v1 == 0:
    return 'NO'
  z = (x1 - x2) / (v2 - v1)
  if z > 0 and z.is_integer():
    return 'YES'
  return 'NO'
```

# Separate the Numbers
```python
import math

def sequential(s,sub_string):
  if not s: return True
  if s.startswith(sub_string):
    l = len(sub_string)
    return sequential(s[l:],str(int(sub_string)+1))
  return False

def separateNumbers(s):
  step = math.floor(len(s)/2)
  for i in range(1, step + 1):
    sub_string = s[:i]
    if sequential(s,sub_string):
      return "YES " + sub_string
  return "NO"
```

# Closest Numbers
```python
def closestNumbers(arr):
  arr.sort()
  min_diff = arr[1] - arr[0]
  answer = []
  for i in range(1, len(arr)):
    if arr[i] - arr[i-1] < min_diff:
      min_diff = arr[i] - arr[i-1]
      answer = []
      answer.append(arr[i-1])
      answer.append(arr[i])
    elif arr[i] - arr[i-1] == min_diff:
      min_diff = arr[i] - arr[i-1]
      answer.append(arr[i-1])
      answer.append(arr[i])
  return answer
```

# Tower Breakers
```python
def towerBreakers(n, m):
  if m == 1:
    return 2
  else:
    if n % 2 == 0:
        return 2
    else:
        return 1
```

# Minimum Absolute Difference in an Array
```python
def minimumAbsoluteDifference(arr):
  arr.sort()
  answer = arr[1] - arr[0]
  for i in range(1, len(arr)):
    if abs(arr[i] - arr[i-1]) < answer:
      answer = abs(arr[i] - arr[i-1])
  return answer
```

# Caesar Cipher
```python
def caesarCipher(s, k):
  la = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  ua = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  answer = []
  k -= int(k / 26) * 26
  for i in s:
    if i.isalpha():
      if i.islower():
        if la.index(i)+k < 26:
          answer.append(la[la.index(i)+k])
        else:
          answer.append(la[la.index(i)+k-26])
      else:
        if ua.index(i)+k < 26:
          answer.append(ua[ua.index(i)+k])
        else:
          answer.append(ua[ua.index(i)+k-26])
    else:
      answer.append(i)
  return ''.join(answer)
```

# Making Anagram
```python
# Time exceeded
# def anagram(s):
#   l = len(s)
#   if l % 2 != 0:
#     return -1
#   else:
#     hf = int(l / 2)
#     first = s[:hf]
#     second = list(s[hf:])
#     cnt = 0
#     for i in range(hf):
#       if second.count(first[i]) > 0:
#         second.remove(first[i])
#       else:
#         cnt += 1
#     return cnt

from collections import Counter

def anagram(s):
  if len(s) % 2 != 0:
    return -1
  else:
    l = len(s)//2
    a = Counter(s[:l])
    b = Counter(s[l:])
    return l-sum((a & b).values())
```

# Max Min
```python
def maxMin(k, arr):
  result = 1000000000
  arr.sort()
  for i in range(n-k+1):
    result = min(result, arr[i+k-1]-arr[i])
  return result
```

# Strong Password
```python
def minimumNumber(n, password):
  numbers = "0123456789"
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  special_characters = "!@#$%^&*()-+"

  mn = 4
  nb = 0
  lc = 0
  uc = 0
  sc = 0
  for i in range(n):
    if password[i] in numbers: nb += 1
    if password[i] in lower_case: lc += 1
    if password[i] in upper_case: uc += 1
    if password[i] in special_characters: sc += 1
  if nb > 0 and lc > 0 and uc > 0 and sc > 0:
    if n < 6:
      return 6 - n
    else:
      return 0
  else:
    if nb > 0: mn -= 1
    if lc > 0: mn -= 1
    if uc > 0: mn -= 1
    if sc > 0: mn -= 1
    if 6 - n > mn:
      return 6 - n
    else:
      return mn
```

# dynamic array
```python
def queryOne(n, q, l):
  if ( q[1] ^ l ) % n == 0:
    return 0
  else:
    return 1

def dynamicArray(n, q, queries):
  tmp = [0] * n
  lastAnswer = 0
  answer = []
  for i in range(n):
    tmp[i] = []
  for i in range(q):
    if queries[i][0] == 1:
      idx = queryOne(n, queries[i], lastAnswer)
      tmp[idx].append(queries[i][2])
    elif queries[i][0] == 2:
      idx = queryOne(n, queries[i], lastAnswer)
      lastAnswer = tmp[idx][queries[i][2] % len(tmp[idx])]
      # print(idx, tmp[idx][queries[i][2] % len(tmp[idx])])
      answer.append(lastAnswer)
  return answer 

if __name__ == '__main__':
  n = 2
  q = 5
  queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
  print(dynamicArray(n, q, queries))

def dynamicArray(n, queries):
  sequences = [[] for _ in range(n)]
  last_answer = 0
  answer = []
    
  for i in range(q):
    q_type = queries[i][0]
    x = queries[i][1]
    y = queries[i][2]
    seq_num = (x ^ last_answer) % n
        
    if q_type == 2:
      last_answer = sequences[seq_num][y % len(sequences[seq_num])]
      answer.append(last_answer)
    else:
      sequences[seq_num].append(y)
  return answer
```

# smartnumber2
```python
def is_smart_number(num):
  val = int(math.sqrt(num))
  if ((num / val) - int(num / val) == 0) and (num % math.sqrt(num) == 0):
    return True
  return False
```

# Missing Numbers
```python
def missingNumbers(arr, brr):
  answer = []
  dsct = list(set(brr))
  for i in range(len(dsct)):
    if arr.count(dsct[i]) != brr.count(dsct[i]):
      answer.append(dsct[i])
  return answer
```

# The fulling count sort
```python
# wrong answer
#def countSort(arr):
#  seq = [[] for _ in range(n)]
#  answer = []
#  for i in range(n):
#    seq[i].append(arr[i][0])
#    seq[i].append(i)
#    seq[i].append(arr[i][1])
#  s_arr = sorted(seq)
#  half = n / 2
#  for j in range(n):
#    if s_arr[j][1] < half:
#      answer.append('-')
#    else:
#      answer.append(s_arr[j][2])
#  print(' '.join(answer))
  
def countSort(arr):
  tmp = []
  for i in range(n):
    x = int(arr[i][0])
    s = str(arr[i][1])
        
    if i < n//2:
      tmp.append((x, "-"))
    else:
      tmp.append((x, s))
      
  print(" ".join(map(lambda x: x[1], sorted(tmp, key = lambda x: x[0]))))
```

# Grid Challenge
```python
def gridChallenge(grid):
  v_grid = [[] for _ in range(len(grid[0]))]
  for i in range(n):
    s_arr = sorted(grid[i])
    for j in range(len(grid[0])):
      v_grid[j].append(s_arr[j])
  for k in range(len(grid[0])):
    if v_grid[k] != sorted(v_grid[k]):
      return 'NO'
  return 'YES'
```

# SansaXOR
```python
from functools import reduce

def sansaXor(n, arr):
  c = 0
  answer = "A"
  while(c < n):
    for i in range(c+1):
      # print(arr[i:n-c+i])
      pair = arr[i:n-c+i] 
      if answer == "A":
        answer = reduce(lambda x, y: x ^ y, pair)
      else:
        answer ^= reduce(lambda x, y: x ^ y, pair)
    c += 1
  return answer

def sansaXor(arr):
  c = 0
  answer = 0
  if len(arr) % 2 == 0:
    return 0
  for ind in range(0, len(arr), 2):
    answer ^= arr[ind]
  return answer
```

# fibonacci
```python
def calc(t1, t2):
  return t1 + (t2 * t2)

def fibonacciModified(t1, t2, n):
  a = t1
  b = t2
  c = 0
  for i in range(n-2):
    c = calc(a, b)
    a = b
    b = c
  return c
```

# prime date
```python
import re
month = []

def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 29
    elif year % 100 == 0:
        month[2] = 28
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28

def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31

def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while(True):
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1
        if x % 4 == 0 or x % 7 == 0:
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 =  y1 + 1
                m1 = 1
    return result;

for i in range(1, 15):
    month.append(31)

line = input()
date = re.split('-| ', line)
d1 = int(date[0])
m1 = int(date[1])
y1 = int(date[2])
d2 = int(date[3])
m2 = int(date[4])
y2 = int(date[5])

result = findPrimeDates(d1, m1, y1, d2, m2, y2)
print(result)
```

# sherlock and array
```python
def balancedSums(arr):
  l = 0
  r = 0
  arr = [i for i in arr if i != 0]
  n = len(arr)
  for i in range(n):
    if i == 0:
      l = [0]
      r = arr[i+1:]
    elif i == n - 1:
      l = arr[:i]
      r = [0]
    else:
      l = arr[:i]
      r = arr[i+1:]
    if sum(l) == sum(r):
      return 'YES'
  return 'NO'

def balancedSums(arr):
  l = 0
  r = sum(arr)
  for i in range(n):
    r -= arr[i]
    if r == l:
      return 'YES'
    l += arr[i]
  return 'NO'
```

# Misère Nim
```python
def misereNim(s):
  if set(s) == {1}:
    if len(s) % 2 == 0:
      return 'First'
    else:
      return 'Second'

  res = reduce((lambda x, y: x ^ y), s)
  if res == 0:
    return 'Second'
  else:
    return 'First'
```

# Gaming Array 1
```python
# time exceeded
#def gamingArray(arr):
#  mi = 0
#  winner = 0
#  while True:
#    mi = arr.index(max(arr))
#    arr = arr[:mi]
#    if len(arr) == 0:
#      break
#    winner += 1
#  if winner % 2 == 0:
#    return 'BOB'
#  else:
#    return 'ANDY'
  
def gamingArray(arr):
  m = 0
  c = 0
  for i in arr:
    if i > m:
      m = i
      c += 1
  if c % 2 == 0:
    return 'ANDY'
  else:
    return 'BOB'
```

# Forming a Magic Square
```python
import sys

matrix_list = [
[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
[[6, 1, 8], [7, 5, 3], [2, 9, 4]],
[[4, 9, 2], [3, 5, 7], [8, 1, 6]],
[[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
[[8, 3, 4], [1, 5, 9], [6, 7, 2]],
[[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
[[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
[[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]

def formingMagicSquare(s):
  cost_list = [sys.maxsize]
  for ref_mat in matrix_list:
    cost = 0
    for x in range(0, len(s)):
      for y in range(0, len(s)):
        if s[x][y] != ref_mat[x][y]:
          cost += abs(s[x][y] - ref_mat[x][y])
    cost_list.append(cost)
  print(cost_list)
  return min(cost_list)
```

# Recursive Digit Sum
```python
# time exceeded
def sd(p):
  arr = str(p)
  num = 0
  for i in str(p):
    num += int(i)
  if len(arr) == 1:
    return p 
  else:
    answer = sd(num)
    return answer

def superDigit(n, k):
  ori = ""
  for i in range(k):
    ori += n
  return sd(ori)


def sd(p):
  arr = str(p)
  num = 0
  for i in str(p):
    num += int(i)
  if len(arr) == 1:
    return p 
  else:
    answer = sd(num)
    return answer

def superDigit(n, k):
  ori = str(k*sum([int(i) for i in n]))
  return sd(ori)

def sd(p):
  if len(p) == 1:
    return int(p) 
  else:
    num = str(sum([int(i) for i in p]))
    return sd(num)

def superDigit(n, k):
  ori = str(k*sum([int(i) for i in n]))
  return sd(ori)
```

# Counter Game
```python
def counterGame(n):
  flag = True
  while True:
    if n == 1:
      break
    if ((n&(n-1)) == 0):
      n = int(n / 2)
    else:
      n -= int(2 ** math.floor(math.log2(n)))
    flag = not flag
  if flag:
    return 'Richard'
  else:
    return 'Louise'
```

# Sum vs XOR
```python
def sumXor(n):
  cnt = 0
  if n == 0:
    return 1
  if (n&(n-1)) == 0:
    return n
  for i in range(n):
    if n + i == n ^ i:
      cnt+=1
  return cnt

# (n+i)=(n^i)+2*(n&i)
# (n+i) = (n^i) => n & i = 0
# andして桁がcarryしなければよい -> 0の数を数えて2**(0の数)
def sumXor(n):
  unset_bits = 0
  while(n):
    if n & 1 == 0:
      unset_bits += 1
    n = n >> 1
  return 1 << unset_bits
```

# Parindrom Index
```python
# time exceeded
def palindromeIndex(s):
  #print(s)
  l = len(s)
  answer = -1
  tmp = s
  if len(set(tmp)) == 1:
    return answer
  for i in range(l):
    arr = s[0:i] + s[i+1:l]
    #print("arr: ", arr)
    answer = 0
    m = len(arr)
    if m % 2 == 0:
      rarr = list(reversed(arr[m//2:]))
      if arr[:m//2] == ''.join(rarr):
        if s[i] == s[i+1]:
          return i+1
        else:
          return i
    else:
      if arr[:(m//2)] == arr[(m//2)+1:]:
        return i
  return answer

if __name__ == '__main__':
  s = []
  s.append("aaab")
  s.append("baa")
  s.append("aaa")
  s.append("quyjjdcgsvvsgcdjjyq")
  s.append("hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh")
  s.append("fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf")
  s.append("bsyhvwfuesumsehmytqioswvpcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcpwsoiqtymhesmuseufwvhysb")
  s.append("fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf")
  s.append("mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm")
  s.append("tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt")
  s.append("lhrxvssvxrhl")
  s.append("prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp")
  s.append("kjowoemiduaaxasnqghxbxkiccikxbxhgqnsaxaaudimeowojk")
  for i in s:
    print(palindromeIndex(i))

def palindromeIndex(s):
  l = len(s)
  i = 0
  j = l-1
  while i<l:
    if s[i]!=s[j]:
      break
    i+=1
    j-=1
  if i>j: return -1
  a = i+1
  b = j
  while a<j and b>i+1:
    if s[a]!=s[b]:
      return j
    a+=1
    b-=1
  return i
```

# The BomberMan Game
```python
# my wrong answer
r = 6
c = 7

def markBomb(og, ng):
  for i in range(r):
    for j in range(c):
      if og[i][j] == 'O':
        # center
        ng[i][j] = '-'
        # top
        if i > 0:
          ng[i-1][j] = '-'
        # bottom
        if i < r - 1:
          ng[i+1][j] = '-'
        # left
        if j > 0:
          ng[i][j-1] = '-'
        # right
        if j < c - 1:
          ng[i][j+1] = '-'
  return ng

def plantBomb(ng):
  for i in range(r):
    for j in range(c):
      if ng[i][j] == '.':
        ng[i][j] = 'O'
  return ng

def detonateBomb(ng):
  for i in range(r):
    for j in range(c):
      if ng[i][j] == '-':
        ng[i][j] = '.'
  return ng

def bomberMan(n, grid):
  og = []
  ng = []
  answer = []
  for i in range(r):
    og.append(list(grid[i]))
    print(og[i])
  for i in range(r):
    ng.append(list(grid[i]))
  print("-------------")
  for i in range(1, n + 1):
    if i % 3 == 1:
      ng = markBomb(og, ng)
      for i in range(r):
        print(ng[i])
      print("-------------")
    elif i % 3 == 2:
      ng = plantBomb(ng)
      for i in range(r):
        print(ng[i])
      print("-------------")
    elif i % 3 == 0:
      ng = detonateBomb(ng)
      og = []
      for i in range(r):
        og.append(ng[i])
        print(og[i])
      print("-------------")
  for i in range(r):
    ng[i] = ['.' if j== '-' else j for j in ng[i]]
    answer.append(''.join(ng[i]))
    print(answer[i])
  return answer

if __name__ == '__main__':
  n = 3
  grid =['.......', '...O...', '....O..',\
         '.......', 'OO.....', 'OO.....']
  result = bomberMan(n, grid)

# answer
def bomberMan(n, grid):
    def timeLaps(g):
        t = list(map(lambda r:list(map(int,r.replace('O','1').replace('.','2') )),g))
        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][j] == 1:
                    t[i][j] = 3
                    # up
                    if i-1 >= 0:
                        if t[i-1][j] != 3:
                            t[i-1][j] = 3
                    # down
                    if i+1 < len(t):
                        if t[i+1][j] != 1:
                            t[i+1][j] = 3
                    # left
                    if j-1 >= 0:
                        if t[i][j-1] != 3:
                            t[i][j-1] = 3
                    # right
                    if j+1 < len(t[i]):
                        if t[i][j+1] != 1:
                            t[i][j+1] = 3
                elif t[i][j] != 3:
                    t[i][j] -= 1
        _t = list(map(lambda r: ''.join(list(map(str,r))), t))
        return list(map(lambda r: r.replace('1','O').replace('3','.'), _t))

    if n == 1:
        return grid
    elif n == 2:
        return list(map(lambda row: row.replace('.', 'O'), grid))
    else:
        if ((n - 1) / 2) % 2 == 1:
            return timeLaps(grid)
        elif ((n - 1) / 2) % 2 == 0:
            temp_grid = timeLaps(grid)
            return timeLaps(temp_grid)
        else:
            return list(map(lambda row: row.replace('.', 'O'), grid))
```
