import sys


class LongestSubstringWithAtleastKRepeatingCharacters:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        c = min(s, key=s.count)
        if s.count(c) >= k:
            return len(s)
        else:
            return max(self.longestSubstring(sub, k) for sub in s.split(c))


if __name__ == '__main__':
    init = LongestSubstringWithAtleastKRepeatingCharacters()
    print(init.longestSubstring(s="aaabb", k=3))  # 3
    print(init.longestSubstring(s="ababbc", k=2))  # 5
