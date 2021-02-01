class ValidParenthesis:
    def isValid(self, s: str) -> bool:
        pairs = {']': '[', '}': '{', ')': '('}
        stack = []
        for c in s:
            if c in '{([':
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return False if stack else True


if __name__ == '__main__':
    init = ValidParenthesis()
    print(init.isValid("{[]}"))  # True
    print(init.isValid("()[]{}"))  # True
    print(init.isValid("([)]"))  # False
    print(init.isValid(")]"))  # False
