def matchingStrings(strings, queries):
  l = [0] * len(queries)
  for i in range(len(queries)):
    for j in range(len(strings)):
      if queries[i] == strings[j]:
        l[i] += 1
  return l

if __name__ == "__main__":
  strings = ['aba', 'baba', 'aba', 'xzxb']
  queries = ['aba', 'xzxb', 'ab']
  print(matchingStrings(strings, queries))
