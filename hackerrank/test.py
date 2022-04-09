# something wrong
# def noPrefix(words):
#   n = len(words)
#   min_comb = 2 * n
#   answer = 0
#   for i in range(n):
#     for j in range(1,n-i):
#       if i != j:
#         if len(words[i]) > len(words[j]):
#           if words[j] == words[i][:len(words[j])]:
#             if i + j < min_comb:
#               answer = i
#               min_comb = i + j
#         else:
#           if words[i] == words[j][:len(words[i])]:
#             if i + j < min_comb:
#               answer = j
#               min_comb = i + j
#   if min_comb != 2 * n:
#     print("BAD SET")
#     print(words[answer])
#   else:
#     print("GOOD SET")
#   return

import bisect

def noPrefix(words):
  arr = []
  for i in range(len(words)):
    s = words[i]
    p = bisect.bisect_right(arr, s) # bisectでアルファベット順に並べ替えてる？
    print(s,p,arr)

    # 挿入位置が2番目以降で挿入位置の一つ前の値が挿入しようとしているものと部分一致する時
    if p >= 1 and s.startswith(arr[p - 1]):
      print("BAD SET")
      print(s)
      return

    # 挿入位置が全体の長さより前で、挿入しようとしているものの値が、挿入位置の値と部分一致する時
    if p < len(arr) and arr[p].startswith(s):
      print("BAD SET")
      print(s)
      return

    arr.insert(p, s)
  print("GOOD SET")
          
if __name__ == '__main__':
  # words = ['aab', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad']
  words = ['hgiiccfchbeadgebc','biiga','edchgb','ccfdbeajaeid','ijgbeecjbj','bcfbbacfbfcfbhcbfjafibfhffac','ebechbfhfcijcjbcehbgbdgbh','ijbfifdbfifaidje','acgffegiihcddcdfjhhgadfjb','ggbdfdhaffhghbdh','dcjaichjejgheiaie','d','jeedfch','ahabicdffbedcbdeceed','fehgdfhdiffhegafaaaiijceijdgbb','beieebbjdgdhfjhj','ehg','fdhiibhcbecddgijdb','jgcgafgjjbg','c','fiedahb','bhfhjgcdbjdcjjhaebejaecdheh','gbfbbhdaecdjaebadcggbhbchfjg','jdjejjg','dbeedfdjaghbhgdhcedcj','decjacchhaciafafdgha','a','hcfibighgfggefghjh','ccgcgjgaghj','bfhjgehecgjchcgj','bjbhcjcbbhf','daheaggjgfdcjehidfaedjfccdafg','efejicdecgfieef','ciidfbibegfca','jfhcdhbagchjdadcfahdii','i','abjfjgaghbc','bddeejeeedjdcfcjcieceieaei','cijdgbddbceheaeececeeiebafgi','haejgebjfcfgjfifhihdbddbacefd','bhhjbhchdiffb','jbbdhcbgdefifhafhf','ajhdeahcjjfie','idjajdjaebfhhaacecb','bhiehhcggjai','bjjfjhiice','aif','gbbfjedbhhhjfegeeieig','fefdhdaiadefifjhedaieaefc','hgaejbhdebaacbgbgfbbcad','heghcb','eggadagajjgjgaihjdigihfhfbijbh','jadeehcciedcbjhdeca','ghgbhhjjgghgie','ibhihfaeeihdffjgddcj','hiedaegjcdai','bjcdcafgfjdejgiafdhfed','fgdgjaihdjaeefejbbijdbfabeie','aeefgiehgjbfgidcedjhfdaaeigj','bhbiaeihhdafgaciecb','igicjdajjdegbceibgebedghihihh','baeeeehcbffd','ajfbfhhecgaghgfdadbfbb','ahgaccehbgajcdfjihicihhc','bbjhih','a','cdfcdejacaicgibghgddd','afeffehfcfiefhcagg','ajhebffeh','e','hhahehjfgcj','ageaccdcbbcfidjfc','gfcjahbbhcbggadcaebae','gi','edheggceegiedghhdfgabgcd','hejdjjbfacggdccgahiai','ffgeiadgjfgecdbaebagij','dgaiahge','hdbaifh','gbhccajcdebcig','ejdcbbeiiebjcagfhjfdahbif','g','ededbjaaigdhb','ahhhcibdjhidbgefggdjebfcf','bdigjaehfchebiedajcjdh','fjehjgbdbaiifi','fbgigbdcbcgffdicfcidfdafghajc','ccajeeijhhb','gaaagfacgiddfahejhbgdfcfbfeedh','gdajaigfbjcdegeidgaccjfi','fghechfchjbaebcghfcfbdicgaic','cfhigaciaehacdjhfcgajgbhhgj','edhjdbdjccbfihiaddij','cbbhagjbcadegicgifgghai','hgdcdhieji','fbifgbhdhagch','cbgcdjea','dggjafcajhbbbaja','bejihed','eeahhcggaaidifdigcfjbficcfhjj']
  print(noPrefix(words))
