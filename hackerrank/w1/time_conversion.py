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

if __name__ == "__main__":
  s = "07:05:45PM"
  print(timeConversion(s))
