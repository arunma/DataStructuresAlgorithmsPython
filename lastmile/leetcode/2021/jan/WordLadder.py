import collections
from collections import defaultdict
from typing import List


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        charList = {c for word in wordSet for c in word}

        queue = collections.deque()
        queue.append((beginWord, 1))

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for a in charList:
                    derived = word[:i] + a + word[i + 1:]
                    if derived in wordSet:
                        wordSet.remove(derived)
                        queue.append((derived, length + 1))
        return 0


if __name__ == '__main__':
    init = WordLadder()
    print(init.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"])) #5
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) #0
