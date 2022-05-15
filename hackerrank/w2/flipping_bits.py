def flippingBits(n):
  n_bin = format(n, 'b')
  s = list('{:032}'.format(int(n_bin)))
  answer = [ '0' if s[i] == '1' else '1' for i in range(len(s))]
  return int(''.join(answer),2)

if __name__ == "__main__":
  n = 3
  print(flippingBits(n))
