# 計算式はどちらもbe = 2 * be - arr[i]
# 最終的にenergyが0になってればよい
# 逆から計算して答えを導く
# 割った余りはenergyに足す必要あり
def chiefHopper(arr):
  min_energy = 0
  for i in range(len(arr)-1,-1,-1):
    min_energy = (min_energy + arr[i]) // 2 + (min_energy + arr[i]) % 2
  return min_energy

if __name__ == '__main__':
  arr = [2,3,4,3,2]
  arr = [3,4,3,2,4]
  print(chiefHopper(arr))
