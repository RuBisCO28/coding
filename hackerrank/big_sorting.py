# Time limit exceeded
# def bigSorting(unsorted):
#  answer = [int(i) for i in unsorted]
#  answer.sort()
#  return [str(i) for i in answer]

# Time limit exceeded
# def bigSorting(unsorted):
#  d = {i: int(k) for i, k in enumerate(unsorted)}
#  s = sorted(d.items(), key=lambda x:x[1])
#  return [str(i[1]) for i in s]

def bigSorting(unsorted):
  unsorted.sort(key=int)
  return unsorted

if __name__ == '__main__':
  unsorted = ['1','200','150','3', '3']
  print(bigSorting(unsorted))

