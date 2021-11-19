# Time limited answer
# class Solution:
#   def longestPalindrome(self, s: str) -> str:
#     arr = list(s)
#     if len(arr) == 1:
#       return s
#     ch_uniq = list(set(arr))
#     if len(ch_uniq) == 1:
#       return s
#     answer = arr
#     max_length = 0
#     for i in range(len(arr)):
#       for j in range(i, len(arr)):
#         if i != j:
#           if arr[i] == arr[j]:
#             if arr[i:j+1] == list(reversed(arr[i:j+1])):
#               if len(arr[i:j+1]) > max_length:
#                 answer = arr[i:j+1]
#                 max_length = len(arr[i:j+1])
#     if max_length > 0:
#       return ''.join(answer)
#     else:
#       return ''.join(arr[0])

class Solution:
  def longestPalindrome(self, s: str) -> str:
    arr = list(s)
    if len(arr) == 1:
      return s
    i = len(arr)
    answer = ""
    while i > 0:
      for j in range(len(arr)-i+1):
        # print(arr[j:i+j], arr[j], arr[i+j-1])
        if arr[j] == arr[i+j-1]:
          if arr[j:i+j] == list(reversed(arr[j:i+j])):
            answer = arr[j:i+j]
            return ''.join(answer)
      i-=1
    return ''.join(arr[0])

result = Solution()
# s = "ac"
# s = "bb"
# s = "aacabdkacaa"
# s = "aaaaaaaaaa"
s = "anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"
print(result.longestPalindrome(s))


