import sys
from collections import Counter


class MinimumWindowSubstring:
    def minWindow(self, s: str, p: str) -> str:
        if not s:
            return ''

        counter=Counter(p)
        ws=0
        matches=0
        result=''
        length=sys.maxsize

        for we,endChar in enumerate(s):
            if endChar in counter:
                counter[endChar]-=1
                if counter[endChar]==0:
                    matches+=1

            while matches==len(counter):
                startChar=s[ws]
                if startChar in counter:
                    if counter[startChar]==0:
                        matches-=1
                    counter[startChar]+=1

                if length>(we-ws+1):
                    length=we-ws+1
                    result=s[ws:we+1]

                ws+=1

        result=result if len!=sys.maxsize else ''
        return result





if __name__ == '__main__':
    init = MinimumWindowSubstring()
    print(init.minWindow("abcdebdde", "bde"))
