from collections import defaultdict


class WordLadder:

    def ladderLength(self, source, target, dictionary):
        patternMap=defaultdict(list)
        for word in dictionary:
            for i in range(len(word)):
                patternMap[word[:i]+'*'+word[i+1:]].append(word)

        queue=[(source, 1)]
        #visited=[False] * len(patternMap.keys())
        visited={}
        while queue:
            word, level =queue.pop(0)
            visited[word]=True
            if word==target:
                return level
            for i in range(len(word)):
                pat_word=word[:i]+'*'+word[i+1:]
                if pat_word not in patternMap: continue
                for nei in patternMap[pat_word]:
                    if nei not in visited:
                        queue.append((nei, level+1))
        return 0





if __name__ == '__main__':
    init = WordLadder()
    print(init.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
    # "hit" -> "hot" -> "dot" -> "dog" -> "cog",
