class LetterCasePermutation:
    def letterCasePermutation(self, S):
        self.result=[]
        self.backtrack(S, '', 0)
        return self.result

    def backtrack(self, S, curr, slot):
        if len(curr)==len(S):
            self.result.append(curr)
            return

        if S[slot].isalpha():
            self.backtrack(S, curr+S[slot].lower(), slot+1)
            self.backtrack(S, curr + S[slot].upper(), slot + 1)
        else:
            self.backtrack(S, curr+S[slot], slot+1)

if __name__ == '__main__':
    init = LetterCasePermutation()
    print(init.letterCasePermutation("a1b2")) #["a1b2","a1B2","A1b2","A1B2"]

