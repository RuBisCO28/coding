arr = [
'S;M;plasticCup()',
'C;V;mobile phone',
'C;C;coffee machine',
'S;C;LargeSoftwareBook',
'C;M;white sheet of paper',
'S;V;pictureFrame',
'S;V;iPad',
]

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
  print(result)

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
  print(result)

def convertCamel(s):
  arr = list(s)
  if arr[0] == 'S':
    splitStr(arr)
  if arr[0] == 'C':
    convertStr(arr)

if __name__ == '__main__':
  for i in range(len(arr)):
    convertCamel(arr[i])
