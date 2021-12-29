# Plus Minus
```python
def plusMinus(arr):
    plus_num = 0
    minius_num = 0
    zero_num = 0
    answer = []
    for i in range(len(arr)):
        if arr[i] > 0:
            plus_num += 1
        if arr[i] == 0:
            zero_num += 1
        if arr[i] < 0:
            minius_num += 1
    answer = [plus_num, minius_num, zero_num]
    for j in range(3):
        print("{0:.6f}".format(answer[j]/len(arr)))
```

# Mini-Max Sum
```python
def miniMaxSum(arr):
    sum = 0
    arr.sort()
    for i in range(5):
        sum += arr[i]
    max = sum - arr[0]
    min = sum - arr[4]
    print(min, max)
```

# Time Conversion
```python
def timeConversion(s):
    hour = 0
    if 'PM' in s:
        hour = 12 + int(s[0:2])
        if hour == 24:
          return s[0:8]
        else:
          return str(hour) + s[2:8]
    if 'AM' in s:
        hour = int(s[0:2])
        if hour == 12:
          return "00" + s[2:8]
        else:
          return s[0:8]
```

# Breaking the Records
```python
def breakingRecords(scores):
    # Write your code here
    min_score = scores[0]
    max_score = scores[0]
    min_brk = 0
    max_brk = 0
    for i in range(len(scores)):
        if scores[i] > max_score:
            max_brk += 1
            max_score = scores[i]
        if scores[i] < min_score:
            min_brk += 1
            min_score = scores[i]
    return [max_brk, min_brk]
```

# Camel Case 4
```python
import sys

def splitStr(arr):
  result = ""
  for i in range(len(arr)):
    if i > 3 and arr[i] != '(' and arr[i] != ')':
      if arr[i].isupper():
        if i != 4:
          result += " "
        result += arr[i].lower()
      else:
        result += arr[i]
  return result

def convertStr(arr):
  result = ""
  flag = 0
  if arr[2] == 'V':
    for i in range(len(arr)):
      if i > 3:
        if flag == 1:
          result += arr[i].upper()
          flag = 0
        elif arr[i] == " ":
          flag = 1
        else:
          result += arr[i]
  if arr[2] == 'C':
    for i in range(len(arr)):
      if i == 4:
        result += arr[i].upper()
      elif i > 3:
        if flag == 1:
          result += arr[i].upper()
          flag = 0
        elif arr[i] == " ":
          flag = 1
        else:
          result += arr[i]
  if arr[2] == 'M':
    for i in range(len(arr)):
      if i > 3:
        if flag == 1:
          result += arr[i].upper()
          flag = 0
        elif arr[i] == " ":
          flag = 1
        else:
          result += arr[i]
    result += "()"
  return result

def convertCamel(s):
  arr = list(s)
  if arr[0] == 'S':
    result = splitStr(arr)
  if arr[0] == 'C':
    result = convertStr(arr)
  return result
```

# Divisible Sum Pairs
```python
def divisibleSumPairs(n, k, ar):
    # Write your code here
    sum = 0
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if i != j:
                sum = ar[i] + ar[j]
                if sum % k == 0:
                    cnt += 1
    return cnt
```

# Sparse Arrays
```python
def matchingStrings(strings, queries):
    # Write your code here
    l = [0] * len(queries)
    for i in range(len(queries)):
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                l[i] += 1
    return l
```

# Lonely Integer
```python
def lonelyinteger(a):
    flag = [0] * len(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i] == a[j]:
                flag[i] = 1
    if 0 in flag:
        return a[flag.index(0)]
    else:
        return a[0]
```

# Grading Students
```python
import math
# 1: 4, 2: 3, 3: 2, 4: 1, 5: 0, 6: 4, 7: 3, 8: 2, 9: 1, 0: 0

def gradingStudents(grades):
    # Write your code here
    answer = []
    for i in range(len(grades)):
        next_mul_val = 5 * (math.floor(grades[i] / 5) + 1)
        if next_mul_val >= 37:
            if next_mul_val - grades[i] < 3:
                answer.append(next_mul_val)
            else:
                answer.append(grades[i])
        else:
            answer.append(grades[i])
    return answer
```

# Flipping bits
```python
def flippingBits(n):
    n_bin = format(n, 'b')
    s = list('{:032}'.format(int(n_bin)))
    answer = [ '0' if s[i] == '1' else '1' for i in range(len(s))]
    return int(''.join(answer),2)
```

# Diagonal Difference
```python
def diagonalDifference(arr):
    x = 0
    y = 0
    j = len(arr) - 1
    for i in range(len(arr)):
        x += arr[i][i]
        y += arr[i][j]
        j -= 1
    if x > y:
        return x - y
    else:
        return y - x
```

# Counting Sort
```python
def countingSort(n, arr):
    answer = [0] * n
    for i in range(n):
        answer[arr[i]] += 1
    return answer[:max(arr)+1]
```

# Counting Valleys
```python
def countingValleys(steps, path):
    answer = 0
    pos = 0
    flag = False
    for i in range(steps):
        if path[i] == 'U':
            pos += 1
        else:
            pos -= 1
        if pos < 0 and flag == False:
            flag = True
            answer += 1
        if pos == 0 and flag == True:
            flag = False
    return answer
```

# Pangrams
```python
def pangrams(s):
    arr = list(s.lower())
    arr = [i for i in arr if i != ' ']
    if len(set(arr)) == 26:
        return 'pangram'
    else:
        return 'not pangram'
```

# Mars Exploration
```python
def marsExploration(s):
    arr = list(s)
    answer = 0
    for i in range(len(arr)):
        if i % 3 == 0 and arr[i] != 'S':
            answer += 1
        elif i % 3 == 1 and arr[i] != 'O':
            answer += 1
        elif i % 3 == 2 and arr[i] != 'S':
            answer += 1
    return answer
```

# Flipping the Matrix
```python
def flip(matrix):
  sums = 0
  n = int(len(matrix[0]) / 2)
  for i in range(n):
    for j in range(n):
      l = []
      l.append(matrix[i][j]) # current matrix
      l.append(matrix[2 * n - 1 - i][j])  # bottom left
      l.append(matrix[i][2 * n - 1- j]) # top right
      l.append(matrix[2* n - 1 - i][2 * n - 1- j]) # bottom right

      maxv = max(l)
      sums += maxv

  return sums

if __name__ == '__main__':
  matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
  print(flip(matrix))
```

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
  print(arr)
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
