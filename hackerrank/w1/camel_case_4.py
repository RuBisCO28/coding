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

