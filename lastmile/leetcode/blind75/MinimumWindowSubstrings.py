import sys
from collections import Counter


class MinimumWindowSubstrings:
    def minWindow(self, s: str, t: str) -> str:
        M=len(s)
        N=len(t)
        if N>M:
            return ""
        pmap=Counter(t)
        ws=0
        matches=0
        minlength=sys.maxsize
        result=""

        for we, endchar in enumerate(s):
            if endchar in pmap:
                pmap[endchar]-=1
                if pmap[endchar]==0:
                    matches+=1

            while matches==len(pmap):
                startchar=s[ws]
                if startchar in pmap:
                    if pmap[startchar]==0:
                        matches-=1
                    pmap[startchar] += 1

                if (we-ws+1)<minlength:
                    minlength=we-ws+1
                    result=s[ws:we+1]

                ws+=1

        return result





if __name__ == '__main__':
    init = MinimumWindowSubstrings()
    print(init.minWindow(s="ab", t="a")) #a
    print(init.minWindow(s="a", t="b")) #''
    print(init.minWindow(s="ADOBECODEBANC", t="ABC"))  # BANC
    print(init.minWindow(s="a", t="a"))  # a
    print(init.minWindow(s="a", t="aa"))  # ''
    print(init.minWindow(s="aa", t="aa"))  # aa
