from typing import List


class GenerateParentheses:
    def generateParenthesis(self, num: int) -> List[str]:
        result = []
        self.generateParenthesisInner(result, num, open=0, close=0, curr="")
        return result

    def generateParenthesisInner(self, result, num, open, close, curr):
        if len(curr) == num * 2:
            result.append(curr)
            return

        if open<num:
            self.generateParenthesisInner(result, num, open+1, close, curr+"(")

        if close<open:
            self.generateParenthesisInner(result, num, open, close+1, curr+")")

if __name__ == '__main__':
    init = GenerateParentheses()
    print(init.generateParenthesis(3))
