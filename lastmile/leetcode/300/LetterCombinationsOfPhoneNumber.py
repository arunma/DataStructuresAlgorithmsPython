from typing import List


class LetterCombinationsOfPhoneNumber:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        queue = [""]
        char_map = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for i, d in enumerate(digits):
            while len(queue[0])==i:
                curr=queue.pop(0)
                for c in char_map[int(d)]:
                    queue.append(curr+c)
        return queue


if __name__ == '__main__':
    init = LetterCombinationsOfPhoneNumber()
    print(init.letterCombinations("23"))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(init.letterCombinations(""))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
