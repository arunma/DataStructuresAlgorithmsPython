from typing import List


class WordBreakII:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result=[]
        curr=[]
        self.helper(s, wordDict, result, curr, 0)
        return result

    def helper(self, s, wordDict, result, curr, index):
        if index==len(s):
            result.append(' '. join(curr))
            return

        if self.canSplit(s, wordDict): #Does pruning
            for i in range(index+1, len(s)+1):
                subs=s[index:i]
                if subs in wordDict:
                    curr.append(subs)
                    self.helper(s, wordDict, result, curr, i)
                    curr.pop()

    def canSplit(self, s, wordDict):
        dp=[False]*(len(s)+1)
        dp[0]=True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True

        return dp[-1]



if __name__ == '__main__':
    init = WordBreakII()
    print(init.wordBreak(s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]))
    print(init.wordBreak("aaaaaaa", ["aaaa","aaa"]))
