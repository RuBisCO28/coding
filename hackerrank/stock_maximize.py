# def stockmax(prices):
#   l = len(prices)
#   answer = 0
#   for i in range(l-1):
#     m = max(prices[i+1:])
#     # print(i,prices[i],m)
#     if prices[i] < m:
#       answer += (m-prices[i])
#   return answer

def stockmax(prices):
  l = len(prices)
  answer = 0
  m = prices[l-1]
  for i in range(l-1, -1, -1):
    # print(i,prices[i],m)
    if prices[i] >= m:
      m = prices[i]
    answer += (m - prices[i])
  return answer

if __name__ == '__main__':
  prices = [1,3,1,2]
  prices = [5,4,3,4,5]
  prices = [1,2,3,4]
  print(stockmax(prices))
