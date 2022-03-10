# https://www.hackerrank.com/challenges/permutation-game/forum
# If the number is already 0, obviously whoever is playing at the time will lose, since can't make any more moves.
# So this is a "losing position" to whoever has the turn at the time.

# If the number is 1, whoever has the turn can only subtract it by 1.
# Now the number is 0, and then by our definition the other player will lose.
# So this is a "winning position" to whoever has the turn at the time.

# If the number is 2, whoever has the turn has two choices, subtract by 1 or subtract by 2.
# If he subtract by 1, then the number becomes 1, which is a "winning position" for the other player.
# So, the player who has 2 will lose. But wait, if he subtract by 2, then the number becomes 0, which is a "losing position" for the other player.
# So, since everyone "plays optimally", they will pick the better choice and subtract by 2, causing the player right now to win.
# So this is a "winning position" to whoever has the turn at the time.

# If the number is 3, it's the same, whoever has the turn can subtract 1, 2, or 3. Now it's obvious, that whoever has the turn will subtract by 3 and then he will win. So this is a "winning position" to whoever has the turn at the time.

# If the number is 4, whoever has the turn can subtract 1, 2, or 3.
# It's clear by now that no matter what he does, it will become a "winning position" for the other player,
# so this position is considered a "losing position". And so on, until 10.

# So, for such game theory problems, we can simply calculate the "winning" and "losing" positions.
# The same can be done for this problem, calculate which sequences are considered "winning" and which ones are considered "losing".
# If the initial sequence is a "winning" sequence, Alice wins, if not, then Bob wins.
# The rule of thumbs for game theory problem: Losing positions lead only to winning positions.
# Winning positions lead to at least one losing position. So that's the meaning of "perfect play".
# The calculation of these positions can be done quite easily by using a recursion with DP memoization,

def permutationGame(arr):
  isIncreasing = lambda arr: all([arr[i] < arr[i + 1] for i in range(len(arr) - 1)])
  memo = {}

  def findWinner(arr):
    key = tuple(arr)
    if key in memo: return memo[key]

    # If arr is ascending, then this player wins (base case)
    if isIncreasing(arr):
      memo[key] = True; return True

    # Calculate next turns: If next player has any available winning moves, this player lost
    for idx in range(len(arr)):
      if findWinner(arr[:idx] + arr[idx + 1:]): memo[key] = False; return False

    # Otherwise, this player wins because next player has no winning moves available
    memo[key] = True; return True

  return 'Bob' if findWinner(arr) else 'Alice'

if __name__ == '__main__':
  arr = [5,3,2,1,4]
  print(permutationGame(arr))

