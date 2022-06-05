from collections import deque

class ValidParenthesis:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '[{(':
                stack.append(c)
            else:
                if c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True


if __name__ == '__main__':
    init = ValidParenthesis()
    print(init.isValid("([)]")) #False
    print(init.isValid("{[]}")) #True


