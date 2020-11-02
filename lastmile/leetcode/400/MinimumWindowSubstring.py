import sys
from collections import Counter


class MinimumWindowSubstring:
    # def minWindow(self, s: str, t: str) -> str:
    #     if len(t) > len(s): return ''
    #     patMap = Counter(t)
    #
    #     ws = 0
    #     matched = 0
    #     minLeft = 0
    #     minLen = sys.maxsize
    #
    #     for we, endChar in enumerate(s):
    #         if endChar in patMap:
    #             patMap[endChar]-=1
    #             if patMap[endChar]==0:
    #                 matched+=1
    #
    #         while matched==len(patMap) and ws<len(s):
    #             startChar=s[ws]
    #             if startChar in patMap:
    #                 patMap[startChar]+=1
    #                 if patMap[startChar]>0:
    #                     matched-=1
    #             if (we - ws + 1) < minLen:
    #                 minLen = we - ws + 1
    #                 minLeft = ws
    #
    #             ws+=1
    #
    #     if minLen==sys.maxsize:
    #         return ''
    #
    #     return s[minLeft:minLeft+minLen]

    def minWindow(self, s: str, t: str) -> str:
        pmap = Counter(t)

        ws = 0

        matches = 0
        result = ''
        minLength = sys.maxsize
        minLeft = 0
        for we, endchar in enumerate(s):
            if endchar in pmap:
                pmap[endchar] -= 1
                if pmap[endchar] == 0:
                    matches += 1

            while matches == len(pmap):
                stchar = s[ws]
                if stchar in pmap:
                    pmap[stchar] += 1
                    if pmap[stchar] > 0:
                        matches -= 1

                if (we - ws + 1) < minLength:
                    result = s[ws:we + 1]
                    minLength = we - ws + 1

                ws += 1

        if minLength == sys.maxsize:
            return ''
        return result

if __name__ == '__main__':
    init = MinimumWindowSubstring()
    print(init.minWindow(s="ab", t="a")) #a
    print(init.minWindow(s="a", t="b")) #''
    print(init.minWindow(s="ADOBECODEBANC", t="ABC"))  # BANC
    print(init.minWindow(s="a", t="a"))  # a
    print(init.minWindow(s="a", t="aa"))  # ''
    print(init.minWindow(s="aa", t="aa"))  # aa
