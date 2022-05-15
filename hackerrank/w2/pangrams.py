def pangrams(s):
  arr = list(s.lower())
  arr = [i for i in arr if i != ' ']
  if len(set(arr)) == 26:
    return 'pangram'
  else:
    return 'not pangram'

if __name__ == "__main__":
  s = "We promptly judged antique ivory buckles for the next prize"
  print(pangrams(s))
