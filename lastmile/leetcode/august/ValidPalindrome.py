class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        chars= ''.join([c.lower() if c.isalnum() else '' for c in s])
        left = 0
        right = len(chars) - 1

        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    init = ValidPalindrome()
    print(init.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(init.isPalindrome("race a car"))  # false
    print(init.isPalindrome("ma d am"))  # True
    print(init.isPalindrome(".,"))  # false
    print(init.isPalindrome("0P"))  # false
