from collections import defaultdict


class LongestSubstringWithRepeatingCharacters:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     freq=defaultdict(int)
    #     ws=0
    #     max_length=0
    #     for we in range(len(s)):
    #         freq[s[we]]+=1
    #         if freq[s[we]]>1:
    #             while (freq[s[we]])>1:
    #                 freq[s[ws]]-=1
    #                 ws+=1
    #         max_length=max(max_length, we-ws+1)
    #     return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        freqMap = defaultdict(int)
        ws = 0
        maxLength = 0
        for we, endChar in enumerate(s):
            freqMap[endChar] += 1
            while freqMap[endChar] > 1:
                startChar = s[ws]
                freqMap[startChar] -= 1
                ws += 1

            maxLength = max(maxLength, we - ws + 1)
        return maxLength

if __name__ == '__main__':
    init = LongestSubstringWithRepeatingCharacters()
    print(init.lengthOfLongestSubstring("abcabcbb")) #3
    print(init.lengthOfLongestSubstring("bbbbb")) #1
    print(init.lengthOfLongestSubstring("pwwkew")) #3
