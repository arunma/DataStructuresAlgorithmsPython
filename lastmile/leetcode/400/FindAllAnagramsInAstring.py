from collections import Counter
from typing import List


class FindAllAnagramsInAstring:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        ws = 0

        result = []
        matches = 0

        for we, endChar in enumerate(s):
            if endChar in counter:
                counter[endChar] -= 1
                if counter[endChar]==0:
                    matches+=1
                    if matches==len(counter):
                        result.append(we-len(p)+1)

            if we+1>=len(p):
                startChar=s[ws]
                if startChar in counter:
                    if counter[startChar]==0:
                        matches-=1
                    counter[startChar]+=1
                ws+=1
        return result




if __name__ == '__main__':
    init = FindAllAnagramsInAstring()
    print(init.findAnagrams("cbaebabacd", "abc"))
    print(init.findAnagrams("abab", "ab"))
    print(init.findAnagrams("acdcaeccde", "c"))
