class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        result = ""
        for i in range(n - 1, -1, -1): #Range excludes the top element
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j] and j - i + 1 > len(result):
                    result = s[i:j + 1]

        return result


if __name__ == '__main__':
    init = LongestPalindromicSubstring()
    print(init.longestPalindrome("babad"))
    print(init.longestPalindrome("cbbd"))
    print(init.longestPalindrome("a"))
    print(init.longestPalindrome("bb"))
