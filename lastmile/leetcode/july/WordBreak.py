class WordBreak:
    def wordBreak(self, s, wordDict):
        memo = dict([])
        wordDictSet = set(wordDict)
        return self.wordBreakHelper(s, wordDictSet, memo)

    def wordBreakHelper(self, s, wordSet, memo):
        if not s:
            return []
        # if s in memo:
        #     return memo[s]

        result = []
        for word in wordSet:
            if not s.startswith(word):
                continue
            elif len(s) == len(word):
                result.append(word)
            else:
                part_result = self.wordBreakHelper(s[len(word):], wordSet, memo)
                for part in part_result:
                    part = word + ' ' + part
                    result.append(part)
        #memo[s] = result
        #print("memo of " + s + " is " + str(memo[s]))
        return result


if __name__ == '__main__':
    init = WordBreak()
    print(init.wordBreak("catsanddog",
                         wordDict=["cat", "cats", "and", "sand", "dog"]))  # ["cats and dog", "cat sand dog"]
