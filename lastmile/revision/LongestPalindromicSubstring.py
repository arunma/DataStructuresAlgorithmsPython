class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        N = len(s)
        longest=s[0]
        for i in range(N - 1):
            odd_palin = self.get_length(s, i, i, -1, N)
            even_palin = self.get_length(s, i, i + 1, -1, N)
            longest= max(longest, odd_palin, even_palin, key=len)
        return longest

    def get_length(self, s, left, right, leftb, rightb):
        while left > leftb and right < rightb and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]


if __name__ == '__main__':
    init = LongestPalindromicSubstring()
    print(init.longestPalindrome("babad"))  # bab
    print(init.longestPalindrome("cbbd"))  # bb
    print(init.longestPalindrome("a"))  # a
    print(init.longestPalindrome("ccc"))  # a
