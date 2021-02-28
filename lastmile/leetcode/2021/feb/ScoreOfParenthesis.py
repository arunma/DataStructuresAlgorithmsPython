class ScoreOfParenthesis:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                curr = stack.pop()
                if curr == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += curr * 2
        return stack[-1]


if __name__ == '__main__':
    init = ScoreOfParenthesis()
    print(init.scoreOfParentheses("(())"))
    print(init.scoreOfParentheses("(()(()))"))
