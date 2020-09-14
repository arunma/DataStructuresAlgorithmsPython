class ValidPalindromeII:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                one = s[left:right]  # Ignore the char on the right
                two = s[left + 1:right + 1]  # Ignore the char on the left
                return one == one[::-1] or two == two[::-1]
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    init = ValidPalindromeII()
    print(init.validPalindrome("aba"))  # True
    print(init.validPalindrome("abca"))  # True
    print(init.validPalindrome("caba"))  # True
