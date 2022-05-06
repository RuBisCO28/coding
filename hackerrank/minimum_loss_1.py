# Time limit exceeded
# def minimumLoss(price):
#   min_v = 9999999
#   for i in range(len(price)):
#     for j in range(i,len(price)):
#       df = price[i] - price[j]
#       if i != j and df >= 0 and min_v > df:
#         min_v = df
#   return min_v

# arr 20 7 8 2 5
# diff 13 -1 6 -3
# diff_sort -3 -1 6 13
# +にならなきゃいけなくて最小値になる組み合わせがわかればいけそう

import bisect

def minimumLoss(price):
  min_v=float('inf')
  stack=[price[0]]
  for num in price[1:]:
    if num < stack[0]:
      min_v = min(min_v,stack[0]-num)
      stack.insert(0,num)
    else:
      index = bisect.bisect(stack,num) # いい感じに入れる場所を探してくれるらしいがどうやってやっているんだ
      if index < len(stack):
        min_v = min(min_v,stack[index]-num)
      stack.insert(index,num)
    print(stack, min_v)
  return min_v

if __name__ == "__main__":
  # price = [20,7,8,2,5]
  price = [20,15,8,2,12]
  print(minimumLoss(price))
