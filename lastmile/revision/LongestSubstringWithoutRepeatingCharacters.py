from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charmap = defaultdict(int)

        N = len(s)
        ws = 0
        curr_len = 0
        max_len = 0

        for we, echar in enumerate(s):
            charmap[echar] += 1

            while charmap[echar] > 1:
                charmap[s[ws]] -= 1
                ws += 1

            curr_len = we - ws + 1
            max_len = max(max_len, curr_len)

        return max_len


