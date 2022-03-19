# wrong logic
# def commonChild(s1, s2):
#   max_c = 0
#   for i in range(len(s2)):
#     a = 0
#     c = 0
#     j = i
#     print("---------",j,s2[j])
#     while j < len(s2):
#       if c == 0 and s2[j] not in s1[a:]:
#         break
#       if s2[j] in s1[a:]:
#         a += s1[a:].index(s2[j]) + 1
#         print(s2[j],s1[a:],a,j)
#         c += 1
#       j += 1
#     if max_c < c:
#       max_c = c
#   return max_c

# Timelimit exceeded
# def commonChild(s1, s2):
#   prev_ai = [0 for i in range(len(s1)+1)]
#   for ai in range(len(s1)):
#     new_ai= [0]
#     for bi in range(len(s2)):
#       if s1[ai] == s2[bi]:
#         new_ai.append(prev_ai[bi] + 1)
#       else:
#         new_ai.append(max(new_ai[-1], prev_ai[bi + 1]))
#     prev_ai = new_ai
#   return new_ai[len(s1)]

def commonChild(s1, s2):
  maxAt = {}
  for i1 in range(len(s1)):
    maxForI1 = 0
    for i2 in range(len(s2)):
      potentialSum = maxForI1 + 1
      other = maxAt.get(i2, 0)
      if other > maxForI1:
        maxForI1 = other

      if s1[i1] == s2[i2]:
        maxAt[i2] = potentialSum
  return max(maxAt.values(), default=0)


if __name__ == '__main__':
  # s1 = "SHINCHAN"
  # s2 = "NOHARAAA"
  # s1 = "ABCD"
  # s2 = "ABDC"
  s1 = "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS"
  s2 = "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC"
  print(commonChild(s1, s2))

