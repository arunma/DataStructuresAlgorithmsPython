class LongestValidParen:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        dp = [0] * (len(s) + 1)
        for i, c in enumerate(s):
            if c == ')' and stack:
                start = stack.pop()
                dp[i + 1] = dp[start] + (i - start + 1)
            elif c == '(':
                stack.append(i)
        return max(dp)


if __name__ == '__main__':
    init = LongestValidParen()
    print(init.longestValidParentheses("(()"))  # 2
    print(init.longestValidParentheses(")()())"))  # 4
