def truckTour(petrolpumps):
  start = 0
  pav = 0
  dfc = 0
  for i in range(len(petrolpumps)):
    pav += petrolpumps[i][0] - petrolpumps[i][1]
    if pav < 0:
      start = i + 1
      dfc += pav
      pav = 0
  if pav+dfc >= 0:
    return start
  else:
    return -1

if __name__ == '__main__':
  petrolpumps = [[1,5],[10,3],[3,4]]
  petrolpumps = [[6,4],[3,6],[7,3]]
  print(truckTour(petrolpumps))
