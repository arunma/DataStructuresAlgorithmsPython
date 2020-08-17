from typing import List


# https://leetcode.com/problems/palindrome-partitioning/discuss/182307/Java%3A-Backtracking-Template-General-Approach
class PalindromicPartitioning:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        self.partitionInner(s, result, [])
        return result

    def partitionInner(self, s:str, result:List[List[str]], curr:List[str]):
        if not s:
            result.append(curr.copy())
            return
        for i in range(1, len(s)+1):
            curr_str=s[:i]
            if self.isPalin(curr_str):
                curr.append(curr_str)
                next_str=s[i:]
                self.partitionInner(next_str, result, curr)
                curr.pop(-1)

    def isPalin(self, s):
        return s == s[::-1]


if __name__ == '__main__':
    init = PalindromicPartitioning()
    print(init.partition("aab"))
    '''
    [
        ["aa","b"],
        ["a","a","b"]
    ]
    '''
