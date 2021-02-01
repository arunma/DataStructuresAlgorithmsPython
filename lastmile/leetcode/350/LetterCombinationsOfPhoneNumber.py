from typing import List


class LetterCombinationsOfPhoneNumber:
    def letterCombinations(self, digits: str) -> List[str]:
        numdigits = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        self.helper(digits, numdigits, result, "", 0)
        return result

    def helper(self, digits, numdigits, result, curr, slot):
        if len(curr) == len(digits):
            result.append(curr)
            return

        for c in numdigits[digits[slot]]:
            self.helper(digits, numdigits, result, curr + c, slot + 1)


if __name__ == '__main__':
    init = LetterCombinationsOfPhoneNumber()
    print(init.letterCombinations("23"))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(init.letterCombinations(""))  # []
