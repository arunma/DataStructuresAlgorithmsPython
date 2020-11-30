from typing import List


class WordBreakII:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []

        result = []
        for word in wordDict:
            if s.startswith(word):
                if len(word) == len(s):
                    result.append(word)
                else:
                    rest = self.helper(s[len(word):], wordDict, memo)
                    for each in rest:
                        result.append(word + ' ' + each)
        memo[s] = result
        return result

if __name__ == '__main__':
    init = WordBreakII()
    # print(init.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
    print(init.wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))
    # print(init.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
