from collections import defaultdict
from typing import List


class WordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        combo_dict=defaultdict(list)
        N = len(beginWord)
        for i in range(N):
            for word in wordList:
                combo_dict[word[:i]+'*'+word[i+1:]].append(word)

        queue=[]
        queue.append((beginWord, 1))
        visited={beginWord:True}

        while queue:
            curr, level=queue.pop(0)
            for i in range(N):
                inter=curr[:i]+'*'+curr[i+1:]
                for val in combo_dict[inter]:
                    if val==endWord:
                        return level+1
                    else:
                        if not val in visited:
                            queue.append((val, level+1))
                            visited[val]=True

        return 0


if __name__ == '__main__':
    init = WordLadder()
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) #5
