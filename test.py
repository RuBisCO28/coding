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

if __name__ == '__main__':
  password = "2bbbb"
  password = "2bb#A"
  # password = "Ab1"
  n = 5
  # n = 3
  print(minimumNumber(n, password))
