# Plus Minus
```python
import math
import os
import random
import re
import sys

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

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
```

# Mini-Max Sum
```python
import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    sum = 0
    arr.sort()
    for i in range(5):
        sum += arr[i]
    max = sum - arr[0]
    min = sum - arr[4]
    print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
```

# Time Conversion
```python
import math
import os
import random
import re
import sys

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

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
```

# Breaking the Records
```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

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

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
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

if __name__ == '__main__':
  for i in sys.stdin.readlines():
    print(convertCamel(i.strip()))

```

# Divisible Sum Pairs
```python

import math
import os
import random
import re
import sys

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

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
```

# Sparse Arrays
```python

import math
import os
import random
import re
import sys

def matchingStrings(strings, queries):
    # Write your code here
    l = [0] * len(queries)
    for i in range(len(queries)):
        for j in range(len(strings)):
            if queries[i] == strings[j]:
                l[i] += 1
    return l
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
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

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
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

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
```
