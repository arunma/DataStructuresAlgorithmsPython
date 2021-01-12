from typing import List

class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortStr=min(strs, key=len)
        for i,c in enumerate(shortStr):
            for each in strs:
                if each[i]!=c:
                    return shortStr[:i]
        return shortStr

if __name__ == '__main__':
    init = LongestCommonPrefix()
    print(init.longestCommonPrefix(strs = ["flower","flow","flight"]))
