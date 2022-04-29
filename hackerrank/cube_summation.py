# something wrong
# def cubeSum(n, operations):
#   arr = []
#   total = 0
#   answer = []
#   for operation in operations:
#     if operation[0:6] == 'UPDATE':
#       op, x, y, z, v = operation.split()
#       # print(op,x,y,z,v)
#       arr.append([int(x),int(y),int(z),int(v)])
#     else:
#       op, x1, y1, z1, x2, y2, z2 = operation.split()
#       # print(op,x1,y1,z1,x2,y2,z2)
#       total = 0
#       for i in range(len(arr)):
#         if int(x1) <= arr[i][0] and arr[i][0] <= int(x2) and int(y1) <= arr[i][1] and arr[i][1] <= int(y2) and int(z1) <= arr[i][2] and arr[i][2] <= int(z2):
#           total += int(arr[i][3])
#       answer.append(total)
#   return answer

def cubeSum(n, operations):
  data = {}
  total = 0
  answer = []
  for operation in operations:
    if operation[0:6] == 'UPDATE':
      op, x, y, z, v = operation.split()
      data[x+" "+y+" "+z] = int(v)
    else:
      op, x1, y1, z1, x2, y2, z2 = operation.split()
      total = 0
      for k,v in data.items():
        corr = [int(s) for s in k.split()]
        if corr[0] <= int(x2) and int(x1) <= corr[0] and corr[1] <= int(y2) and int(y1) <= corr[1] and corr[2] <= int(z2) and int(z1) <= corr[2]:
          total += v
      answer.append(total)
  return answer

if __name__ == "__main__":
  n = 4
  operations = ['UPDATE 2 2 2 4', 'QUERY 1 1 1 3 3 3', 'UPDATE 1 1 1 23', 'QUERY 2 2 2 4 4 4', 'QUERY 1 1 1 3 3 3']
  print(cubeSum(n, operations))
