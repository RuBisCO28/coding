# 十進法表記で各桁の値が7,5,3のいずれかであり，かつ7,5,3がいずれも一度以上は登場する整数を「753数」とよぶこととします
# 正の整数Kが与えられたときに，K以下の753数が何個あるかを求めるアルゴリズムを設計してください
# ただしKの桁数をdとしてO(3d)程度の計算量を許容できるものとします
# 出典:AtCoderBeginnerContest114C 755

# 3^kだが、forの数はわかっている前提なので違う
# def nagomi(k):
#   arr = [3,5,7]
#   answer = 0
#   for i in arr:
#     for j in arr:
#       if i != j:
#         for l in arr:
#           if i != j and j != l and i != l:
#             if (i*100 + j*10 + l) < k:
#               answer += 1
#   return answer

n = 573

def nagomi(cur,use,counter):
  if(cur > n): return
  if (use == 0b111):
    counter.append(1)

  # 両辺を2進数とみて，ビットごとにORをとる
  # ORをとることで含まれているかのフラグをもたせる
  # 一度目の 0 | 0b001から1 | 0b001になるのでフラグになる
  # 一度目の 0 | 0b010から2 | 0b010になるのでフラグになる
  # 一度目の 0 | 0b100から4 | 0b100になるのでフラグになる
  # 1,2,4は桁数???
  nagomi(cur * 10 + 7, use | 0b001, counter)
  nagomi(cur * 10 + 5, use | 0b010, counter)
  nagomi(cur * 10 + 3, use | 0b100, counter)

if __name__ == "__main__":
  res = []
  nagomi(0,0,res)
  print(sum(res))
