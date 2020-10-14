from collections import defaultdict
from typing import List


class MostCommonWord:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in paragraph:
            if c in "!?',;.":
                paragraph=paragraph.replace(c, ' ')

        counts=defaultdict(int)
        for word in paragraph.lower().split():
            if word not in banned:
                counts[word]+=1
        return max(counts, key=counts.get)

if __name__ == '__main__':
    init = MostCommonWord()
    print(init.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
