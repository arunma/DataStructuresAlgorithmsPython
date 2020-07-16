from typing import List


class WordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0]=True
        for i in range(n + 1):
            for j in range(i + 1):
                if s[j:i] in words and dp[j]:
                    dp[i]=True
        return dp[n]


    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     words = set(wordDict)
    #     ws = 0
    #     for we in range(len(s) + 1):
    #         if s[ws:we] in words:
    #             words.remove(s[ws:we])
    #             ws = we
    #     return ws == we


if __name__ == '__main__':
    init = WordBreak()
    #print(init.wordBreak(s="leetcode", wordDict=["leet", "code"]))  # true
    #print(init.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))  # true
    print(init.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))  # false
    #print(init.wordBreak(s="aaaaaaa", wordDict=["aaaa", "aaa"]))  # true
