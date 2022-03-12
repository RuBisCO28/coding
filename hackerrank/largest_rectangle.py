def largestRectangle(h):
  n = len(h)
  answer = 0
  for i in range(n):
    p = h[i]
    area = p
    front = i + 1
    back = i - 1
    while True:
      if (front > n - 1) and (back < 0):
        break
      if (front <= n - 1):
        if p <= h[front]:
          area += p
          front += 1
        else:
          front = n
      if (back >= 0):
        if p <= h[back]:
          area += p
          back -= 1
        else:
          back = -1
    if area > answer:
      answer = area
  return answer

if __name__ == '__main__':
  h = [1,2,3,4,5]
  h = [11,11,10,10,10]
  print(largestRectangle(h))
