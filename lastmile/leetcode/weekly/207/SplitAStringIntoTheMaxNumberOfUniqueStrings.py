class SplitAStringIntoTheMaxNumberOfUniqueStrings:
    # def maxUniqueSplit(self, s: str) -> int:
    #     result=[]
    #     curr=[]
    #     self.helper(s, result, curr, 0)
    #     return min(result, key=lambda x:len(x))
    #
    # def helper(self, s, result, curr, index):
    #     if index==len(s):
    #         result.append(curr)
    #         return
    #     for i in range(index+1, len(s)):
    #         self.helper(s, result, curr+[s[:i]], i+1)
    #

    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        def backtrack(i):
            if i == len(s):
                return 0
            j = i
            ret = 0
            for j in range(i, len(s)):
                me = s[i:j + 1]
                if me in seen:
                    continue
                seen.add(me)
                ret = max(ret, 1 + backtrack(j + 1))
                seen.remove(me)
            return ret

        return backtrack(0)

if __name__ == '__main__':
    init = SplitAStringIntoTheMaxNumberOfUniqueStrings()
    print(init.maxUniqueSplit("ababccc")) #5
    print(init.maxUniqueSplit("aba")) #2
    print(init.maxUniqueSplit("aa")) #1
