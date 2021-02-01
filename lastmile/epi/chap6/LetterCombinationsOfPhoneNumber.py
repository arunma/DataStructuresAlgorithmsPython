from typing import List


class LetterCombinationsOfPhoneNumber:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.mapping=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        self.result=[]
        self.backTrack(digits, '', 0)
        return self.result

    def backTrack(self, digits, curr, slot):
        if len(curr)==len(digits):
            self.result.append(curr)
            return

        for c in self.mapping[int(digits[slot])]:
            self.backTrack(digits, curr+c, slot+1)


if __name__ == '__main__':
    init = LetterCombinationsOfPhoneNumber()
    print(init.letterCombinations("23"))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(init.letterCombinations(""))  #[]

