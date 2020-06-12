from collections import defaultdict


class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ws = 0
        max_length = 0
        freq = defaultdict(int)
        for we in range(0, len(s)):
            freq[s[we]] = freq[s[we]] + 1
            while freq[s[we]] > 1:
                freq[s[ws]] = freq[s[ws]] - 1
                ws = ws + 1
            max_length = max(max_length, we - ws + 1)
        return max_length


if __name__ == '__main__':
    init = LongestSubstringWithoutRepeatingCharacters()
    print(init.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(init.lengthOfLongestSubstring("bbbbb"))  # 1
    print(init.lengthOfLongestSubstring("pwwkew"))  # 3
