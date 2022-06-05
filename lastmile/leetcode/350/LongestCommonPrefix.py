from typing import List


class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minstr=min(strs, key=len)
        result=minstr
        for i, c in enumerate(minstr):
            for each in strs:
                if each[i]!=c:
                    result=min(result, minstr[:i], key=len)
        return result



if __name__ == '__main__':
    init = LongestCommonPrefix()
    print(init.longestCommonPrefix(["flower","flow","flight"]))
