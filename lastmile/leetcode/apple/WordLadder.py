import string
from typing import List
from collections import deque

class WordLadder:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 0)])
        wordSet = set(wordList)
        N = len(beginWord)

        if endWord not in wordList:
            return 0
        while queue:
            curr, length = queue.popleft()
            if curr == endWord:
                return length + 1

            for i in range(N):
                for c in string.ascii_lowercase:
                    cand = curr[:i] + c + curr[i + 1:]
                    if cand in wordSet:
                        wordSet.remove(cand)
                        queue.append((cand, length + 1))

        return 0

    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     queue=deque([(beginWord, 0)])
    #     visited=set()
    #
    #     if endWord not in wordList:
    #         return 0
    #     while queue:
    #         curr, length=queue.popleft()
    #         if curr==endWord:
    #             return length+1
    #
    #         for cand in wordList:
    #             if cand not in visited and self.is_one_char_away(curr, cand):
    #                 visited.add(cand)
    #                 queue.append((cand, length+1))
    #
    #     return 0
    #
    #
    # def is_one_char_away(self, curr, cand):
    #     edit=0
    #     for c1, c2 in zip(curr, cand):
    #         if c1!=c2:
    #             edit+=1
    #         if edit>1:
    #             return False
    #     return edit==1

if __name__ == '__main__':
    init = WordLadder()
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) #5
    print(init.ladderLength("leet", "code", ["lest", "leet", "lose", "code", "lode", "robe", "lost"])) #6

