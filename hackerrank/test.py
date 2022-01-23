month = []

def updateLeapYear(year):
  if year % 400 == 0:
    month[2] = 28
  elif year % 100 == 0:
    month[2] = 29
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

  # 2082025
  # 31082025
  # 4092025
  # 31092025
  while(True):
    x = d1
    x = x * 100 + m1
    x = x * 1000 + y1
    if x % 4 == 0 and x % 7 == 0:
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
        m1 = m1 + 1
  return result;

if __name__ == '__main__':
  for i in range(1, 15):
    month.append(31)

  d1 = int(2)
  m1 = int(8)
  y1 = int(2025)
  d2 = int(4)
  m2 = int(9)
  y2 = int(2025)

result = findPrimeDates(d1, m1, y1, d2, m2, y2)
print(result)
