from collections import deque
from typing import List


class EvaluateReversePolishNotation:
    # def evalRPN(self, tokens):
    #
    #     stack = []
    #
    #     for token in tokens:
    #
    #         if token not in "+-/*":
    #             stack.append(int(token))
    #             continue
    #
    #         number_2 = stack.pop()
    #         number_1 = stack.pop()
    #
    #         result = 0
    #         if token == "+":
    #             result = number_1 + number_2
    #         elif token == "-":
    #             result = number_1 - number_2
    #         elif token == "*":
    #             result = number_1 * number_2
    #         else:
    #             result = int(number_1 / number_2)
    #
    #         stack.append(result)
    #
    #     return stack.pop()
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "-+*/":
                stack.append(int(token))
                continue
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                result = 0
                if token == '+':
                    result = val1 + val2
                elif token == '-':
                    result = val1 - val2
                elif token == "*":
                    result = val1 * val2
                else:
                    result = int(val1 / val2)

                stack.append(result)
        return stack.pop()


if __name__ == '__main__':
    init = EvaluateReversePolishNotation()
    #print(init.evalRPN(["2", "1", "+", "3", "*"]))  # 9
    #print(init.evalRPN(["4", "13", "5", "/", "+"]))  # 6
    print(init.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
