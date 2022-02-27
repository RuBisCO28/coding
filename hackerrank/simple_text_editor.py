if __name__ == '__main__':
  # nq = 8
  # ope = ['1 abc','3 3','2 3','1 xy','3 2', '4', '4', '3 1']
  # nq = 10
  # ope = ['1 ewcgpjfh','1 igqsbqyp','1 qsdliigcj','4','3 15','1 iilmgp','2 8','4','2 18','1 scwhors']
  nq = 7
  ope = ['1 giihangdtzjavcaxnbtudpcnmzggbdabocpeplzercnctkcvhoujbrpbztjlpuymabumbppgrydkdzbadcsjdtpdftlusapza',
'3 6',
'4',
'1 fcsivbvhtzydbhhopdnlaisgqhlkizqhezglxocqgymjedw',
'2 24',
'3 10',
'3 11']
  h = ['' for i in range(nq)]
  i = 0
  p = 0
  for _ in range(nq):
    l = ope[i].split()
    if l[0] == '1':
      if p == 0:
        h[p] = l[1]
      else:
        h[p] = h[p-1]
        h[p] += l[1]
      p += 1
    elif l[0] == '2':
      bk = int(l[1])
      h[p] = h[p-1][:-bk]
      p += 1
    elif l[0] == '3':
      print(h[p-1][int(l[1])-1])
    elif l[0] == '4':
      p -= 1
    # print(l[0], i, p, h)
    i += 1
