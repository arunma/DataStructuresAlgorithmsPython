from typing import List


class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict:
                    dp[i]=dp[j]
        return dp[-1]

if __name__ == '__main__':
    init = WordBreak()
    print(init.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
