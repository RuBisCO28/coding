def gen_prime(n):
  nroot = int(n**(0.5))
  sieve = list(range(n+1))
  sieve[1] = 0

  for i in range(2, nroot+1):
    if sieve[i] != 0:
      m = n//i - i
      sieve[i*i: n+1:i] = [0] * (m+1)

  return [x for x in sieve if x !=0]

# def waiter(number, q):
#   answer = []
#   pl = []
#   prime_list = gen_prime(10000)
#   for i in range(q):
#     pl = []
#     for j in range(len(number)):
#       if number[j] % prime_list[i] == 0:
#         answer.append(number[j])
#       else:
#         pl.append(number[j])
#     if i != q - 1:
#       number = pl[::-1]
#     else:
#       number = pl
#     print(number,answer)
#   if len(number) != 0:
#     for k in number:
#       answer.append(k)
#   return answer

def waiter(number, q):
  prime_list = gen_prime(10000)
  answer = []
  b_stacks = []
  plate_stacks = [number, []]
  for ind in range(q):
    a_ind = int(ind % 2)
    b = []
    while len(plate_stacks[a_ind]) > 0:
      pl = plate_stacks[a_ind].pop()
      if pl % prime_list[ind] == 0:
        b.append(pl)
      else:
        plate_stacks[1 - a_ind].append(pl)
    b_stacks.append(b)
  for b in b_stacks:
    if len(b) > 0:
      answer.append(b[::-1])
  for pl in plate_stacks:
    if len(pl) > 0:
      answer.append(pl[::-1])
  return sum(answer,[])

if __name__ == '__main__':
  number = [3,4,7,6,5]
  q = 1
  # number = [3,3,4,4,9]
  # q = 2
  # number = [2,3,4,5,6,7]
  # q = 3
  # number = [80,37,86,79,8,39,43,41,15,33,30,15,45,55,61,74,49,49,20,66,77,19,85,44,81,82,27,5,36,83,91,45,39,44,19,44,71,49,8,66,81,40,29,60,35,31,44]
  # q = 21
  print(waiter(number, q))

