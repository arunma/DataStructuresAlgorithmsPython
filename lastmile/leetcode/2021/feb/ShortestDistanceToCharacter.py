import sys
from typing import List


class ShortestDistanceToCharacter:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result=[0] * len(s)
        pos=-len(s)
        for i in range(len(s)):
            if s[i]==c:
                pos=i
            result[i]=i-pos

        for i in reversed(range(len(s))):
            if s[i]==c:
                pos=i
            else:
                result[i]=min(result[i], pos-i)
        return result




if __name__ == '__main__':
    init=ShortestDistanceToCharacter()
    print(init.shortestToChar(s = "loveleetcode", c = "e")) #[3,2,1,0,1,0,0,1,2,2,1,0]
    print(init.shortestToChar(s = "aaab", c = "b")) #[3,2,1,0]
