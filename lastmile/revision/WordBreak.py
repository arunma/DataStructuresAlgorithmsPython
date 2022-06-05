from typing import List


class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True
        wordset=set(wordDict)

        for i in range(1, N+1):
            for j in range(i):
                #print (f"j: {j}:i: {i}  ->  s[j:i]: {s[j:i]}")
                if s[j:i] in wordset and dp[j]:
                    dp[i]=True
                    break
        return dp[-1]



if __name__ == '__main__':
    init = WordBreak()
    print(init.wordBreak(s="leetcode", wordDict=["leet", "code"]))  # true
    print(init.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))  # true
    print(init.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))  # false
