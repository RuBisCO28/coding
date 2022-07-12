# N個の足場があって，i(＝0,1,...,N－1)番目の足場の高さはhiで与えられます
# 最初０番目の足場にカエルがいて，以下のいずれかの行動を繰り返してN－1番目の足場を目指します
# 足場iから足場i＋1へと移動する(コストは|hi－hi＋1|)足場iから足場i＋2へと移動する(コストは|hi－hi＋2|)
# カエルがN－1番目の足場にたどり着くまでに要するコストの総和の最小値を求めてください

def frog(trees):
  arr = []
  for i in range(len(trees)):
    if i == 0:
      arr.append(0)
    elif i == 1:
      arr.append(trees[i] - trees[i-1])
    else:
      arr.append(min(abs(trees[i] - trees[i-1]) + arr[i-1],abs(trees[i] - trees[i-2]) + arr[i-2]))
  return arr[-1]

if __name__ == "__main__":
  trees = [2,9,4,5,1,6,10]
  print(frog(trees))
