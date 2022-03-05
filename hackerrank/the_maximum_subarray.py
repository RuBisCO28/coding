def Subarray2(arr):
  print(arr)
  pl = 0
  ms = 0
  sa = []
  flag = 0
  for i in range(len(arr)-1):
    print(arr[i],pl,ms,sa)
    if arr[i] > 0 and arr[i+1] > 0:
      if i == (len(arr)-2):
        if pl != 0:
          pl += arr[i] + arr[i+1]
          sa.append(pl)
        else:
          sa.append(arr[i]+arr[i+1])
      else:
        pl += arr[i]
    if arr[i] < 0 and arr[i+1] < 0:
      if i == (len(arr)-2):
        if ms != 0:
          ms += arr[i] + arr[i+1]
          sa.append(ms)
        else:
          sa.append(arr[i]+arr[i+1])
      else:
        ms += arr[i]
    if arr[i] > 0 and arr[i+1] < 0:
      flag += 1
      if i == (len(arr)-2):
        if pl != 0:
          pl += arr[i]
          sa.append(pl)
          sa.append(arr[i+1])
        else:
          sa.append(arr[i])
          sa.append(arr[i+1])
      else:
        pl += arr[i]
        sa.append(pl)
        pl = 0
    if arr[i] < 0 and arr[i+1] > 0:
      flag += 1
      if i == (len(arr)-2):
        if ms != 0:
          ms += arr[i]
          sa.append(ms)
          sa.append(arr[i+1])
        else:
          sa.append(arr[i])
          sa.append(arr[i+1])
      else:
        ms += arr[i]
        sa.append(ms)
        ms = 0
  if flag == 0:
    if arr[0] > 0:
      return sum(arr)
    else:
      return max(arr)
  tmp = 0
  l = len(sa)
  print(sa)
  for j in range(1, l+1):
    for k in range(0,l-j+1):
      # print(j,k,sum(sa[k:k+j]))
      if sum(sa[k:k+j]) > tmp:
        tmp = sum(sa[k:k+j])
  return tmp

def Subarray3(arr):
  answer = []
  l = len(arr)
  answer.append(max(arr))
  for j in range(2, l+1):
    for k in range(0,l-j+1):
      print(j,k,sum(arr[k:k+j]))
      answer.append(sum(arr[k:k+j]))
  return max(answer)

def Subarray4(arr):
  d = {}
  sa = []
  flag = 0
  l = len(arr)
  for i in range(l):
    if i == 0:
      tmp = arr[i]
    elif i == (l-1):
      if (arr[i] >= 0 and tmp >= 0) or (arr[i] < 0 and tmp < 0):
        sa.append(tmp+arr[i])
      else:
        sa.append(tmp)
        sa.append(arr[i])
        flag += 1
    else:
      if (arr[i] >= 0 and tmp >= 0) or (arr[i] < 0 and tmp < 0):
        tmp += arr[i]
      else:
        sa.append(tmp)
        tmp = arr[i]
        flag += 1
  if flag == 0:
    if arr[0] > 0:
      return sum(arr)
    else:
      return max(arr)
  answer = 0
  l = len(sa)
  for j in range(1, l+1):
    for k in range(0,l-j+1):
      # print(j,k,sum(sa[k:k+j]))
      if sum(sa[k:k+j]) > tmp:
        answer = sum(sa[k:k+j])
  return answer

def Subarray(arr):
  print(arr)
  curSum = maxSum = arr[0]
  for num in arr[1:]:
    curSum = max(num, curSum + num)
    maxSum = max(maxSum, curSum)
    print(num, curSum,maxSum)
  return maxSum

def Subsequence(arr):
  pl = [i for i in arr if i >= 0]
  if len(pl) > 0:
    return sum(pl)
  else:
    ms = [j for j in arr if j < 0]
    return max(ms)

def maxSubarray(arr):
  answer = []
  answer.append(Subarray(arr))
  answer.append(Subsequence(arr))
  return answer

if __name__ == '__main__':
  arr = [-1,2,3,-4,5,10]
  arr = [1,2,3,4]
  arr = [2,-1,2,3,4,-5]
  arr = [2,-1,2,3,4,5]
  arr = [-2,-3,-1,-4,-6]
  arr = [-1,2,-1,4]
  print(maxSubarray(arr))
