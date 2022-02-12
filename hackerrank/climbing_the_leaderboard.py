# 数えるときにあらかじめsortしておくことで途中から数えられるようにしておく

# time limit exceeded
# import copy
# 
# def climbingLeaderboard(ranked, player):
#   arr = []
#   answer = []
#   ranked = sorted(set(ranked), reverse=True)
#   player = sorted(player)
#   for i in range(len(player)):
#     arr = copy.deepcopy(ranked)
#     arr.append(player[i])
#     answer.append(sorted(set(arr), reverse=True).index(player[i])+1)
#   return answer

def climbingLeaderboard(ranked, player):
  answer = []
  ranked = sorted(set(ranked), reverse=True)
  player = sorted(player, reverse=True)
  l = len(ranked)
  j = 0
  for i in range(len(player)):
    while j < l and player[i] < ranked[j]:
      j += 1
    answer.append(j+1)
  return answer[::-1]

if __name__ == '__main__':
  ranked = [100, 90, 90, 80]
  player = [70, 80, 105]
  print(climbingLeaderboard(ranked, player))

