class PalindromicSubsequences:

    def palindromeSubsequence(self, s):
        result=set()
        curr=[]
        self.backtrack(s, result, curr, 0)
        return result

    def backtrack(self, s, result, curr, index):
        if self.isPalindrome(curr):
            result.add(''.join(curr))

        for i in range(index,len(s)):
            self.backtrack(s, result, curr+[s[i]], i+1)

    def isPalindrome(self, lst):
        return lst==lst[::-1]

if __name__ == '__main__':
    init = PalindromicSubsequences()
    print(init.palindromeSubsequence("abac")) #["a", "b", "c", "aa", "aba"]
