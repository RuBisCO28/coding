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

```
