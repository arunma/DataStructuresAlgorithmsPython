class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        longest = ""
        for i in range(1, N + 1):
            odd = self.getLongestFromHere(s, i, i)
            even = self.getLongestFromHere(s, i, i + 1)
            print ("odd:" + odd + ", even: "+ even)
            longest = max(longest, odd, even, key=len)
        return longest

    def getLongestFromHere(self, s, left, right):
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]


if __name__ == '__main__':
    init = LongestPalindromicSubstring()
    print(init.longestPalindrome(s = "babad"))
