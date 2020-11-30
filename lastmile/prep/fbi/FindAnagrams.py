from collections import Counter
from typing import List


class FindAnagrams:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        ws = 0

        patternLen = len(p)
        pCounter = Counter(p)
        matched = 0

        for we, endChar in enumerate(s):
            if endChar in pCounter:
                pCounter[endChar] -= 1
                if pCounter[endChar] == 0:
                    matched += 1
                    if matched == len(pCounter):
                        result.append(we - patternLen + 1)

            if we >= patternLen - 1:
                startChar = s[ws]
                ws += 1
                if startChar in pCounter:
                    if pCounter[startChar] == 0:
                        matched -= 1
                    pCounter[startChar] += 1

        return result


if __name__ == '__main__':
    init = FindAnagrams()
    print(init.findAnagrams("cbaebabacd", "abc")) #[0,6]
    #print(init.findAnagrams("abab", "ab")) #[0,1,2]
    print(init.findAnagrams("acdcaeccde", "c")) #[1,3,6,7]
