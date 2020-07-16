class LongestSubstringWithAtLeastKRepeatingCharacters:
    def longestSubstring(self, s, k):
        freq={}


# def longestSubstring(self, s: str, k: int) -> int:
    #     freq = {}
    #     ws = 0
    #     max_count = -1
    #     for we in range(0, len(s)):
    #         if s[we] not in freq:
    #             freq[s[we]] = 0
    #         freq[s[we]] += 1
    #         if len(freq) > k:
    #             while len(freq) >= k:
    #                 freq[s[ws]] -= 1
    #                 if freq[s[ws]] == 0:
    #                     del freq[s[ws]]
    #                 ws += 1
    #         max_count = max(max_count, we - ws + 1)
    #     return max_count





if __name__ == '__main__':
    init = LongestSubstringWithAtLeastKRepeatingCharacters()
    print(init.longestSubstring(s="aaabb", k=3))  # 3
    print(init.longestSubstring(s="ababbc", k=2))  # 5
