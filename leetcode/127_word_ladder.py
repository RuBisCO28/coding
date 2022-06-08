from typing import Optional
from typing import List

class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
      return 0
    counts = 1
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if beginWord in wordList:
      wordList.remove(beginWord)
    word_dic = {i:1 for i in wordList} # for O(1) search
    l = set([beginWord])
    r = set([endWord])
    ll = set([beginWord]) # record all the words appeared
    while l:
      tmp = []
      for word in l:
        for ch in letters:
          for i in range(len(word)):
            new = word[:i]+ch+word[i+1:]
            if (new not in ll) & (new in word_dic):
              tmp.append(new)
      l = set(tmp)
      counts += 1
      ll = ll | l
      if l & r:
        return counts

    return 0

result = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(result.ladderLength(beginWord,endWord,wordList))
