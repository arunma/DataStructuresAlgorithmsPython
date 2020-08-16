class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        result = ""

        for i in range(N):
            odd_string = self.expand_from_middle(s, i, i)
            even_string = self.expand_from_middle(s, i, i + 1)
            # if len(result)<len(odd_string):
            #     result=odd_string
            # if len(result)<len(even_string):
            #     result=even_string
            result=max(result, odd_string, even_string, key=len)

        return result

    def expand_from_middle(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1: end]
    # The while loop stops either because l or r is out of range or because the s[l] != s[r],
    # which means neither s[l] nor s[r] can be part of the longest palindrome and the helper function returns s[l+1:r](inclusive on the left and exclusive on the right).


if __name__ == '__main__':
    init = LongestPalindromicSubstring()
    print(init.longestPalindrome("babad"))  # bab
    print(init.longestPalindrome("cbbd"))  # bb
