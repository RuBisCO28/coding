# Time limit exceeded
# def contacts(queries):
#   words = []
#   answer = []
#   for i in range(len(queries)):
#     if queries[i][0] == "add":
#       words.append(queries[i][1])
#     else:
#       arr = [1 for j in words if j.startswith(queries[i][1])]
#       answer.append(sum(arr))
#   return answer

from collections import defaultdict

# 辞書を作る
# {'': 2, 'h': 2, 'ha': 2, 'hac': 2, 'hack': 2, 'hacke': 1, 'hacker': 1, 'hackerr': 1, 'hackerra': 1, 'hackerran': 1, 'hackerrank': 1})
def contacts(queries):
  trie = defaultdict(int)
  ans = []
  for action, text in queries:
    if action == "add":
      for i in range(len(text) + 1):
        trie[text[: i]] += 1
    else:
      ans.append(trie[text])
  return ans

if __name__ == "__main__":
  queries = [['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']]
  print(contacts(queries))

