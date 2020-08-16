from collections import defaultdict
from typing import List


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0

        combo_dict = defaultdict(list)
        N = len(beginWord)
        for word in wordList:
            for i in range(N):
                combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        queue = [(beginWord, 1)]

        visited = {beginWord: True}

        while queue:
            curr, level = queue.pop()
            for i in range(N):
                gen = curr[:i] + '*' + curr[i + 1:]
                for val in combo_dict[gen]:
                    if val == endWord:
                        return level + 1
                    if val not in visited:
                        queue.append((val, level + 1))
                        visited[val]=True
                combo_dict[gen]=[]

        return 0


if __name__ == '__main__':
    init = WordLadder()
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) #5
