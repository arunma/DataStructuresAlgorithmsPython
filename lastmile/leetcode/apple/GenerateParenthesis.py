from typing import List


class GenerateParenthesis:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.bt(n, 0, 0,"", result)
        return result

    def bt(self, n, left, right, curr, result):
        if len(curr)==(n*2):
            result.append(curr)
            return

        if left < n:
            self.bt(n, left+1, right, curr+'(', result)

        if right<left:
            self.bt(n, left, right+1, curr+')', result)




if __name__ == '__main__':
    init = GenerateParenthesis()
    print(init.generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
