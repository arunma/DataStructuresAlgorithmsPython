class CountSubstrings:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            odd_count = self.expand_from_middle(s, i, i)
            even_count = self.expand_from_middle(s, i, i + 1)
            count += odd_count + even_count
        return count

    def expand_from_middle(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        return count


if __name__ == '__main__':
    init = CountSubstrings()
    print(init.countSubstrings("abc")) #3
    print(init.countSubstrings("aaa")) #6
