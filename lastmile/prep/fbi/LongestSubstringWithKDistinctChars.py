from collections import defaultdict


class LongestSubstringWithKDistinctChars:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        freqMap = defaultdict(int)
        ws = 0

        resultMax = -1
        for we, endChar in enumerate(s):
            freqMap[endChar] += 1

            while len(freqMap) > k:
                startChar=s[ws]
                if startChar in freqMap:
                    freqMap[startChar] -= 1
                    if freqMap[startChar]==0:
                        del freqMap[startChar]
                ws += 1

            resultMax = max(we - ws + 1, resultMax)
        return resultMax


if __name__ == '__main__':
    init = LongestSubstringWithKDistinctChars()
    print(init.lengthOfLongestSubstringKDistinct(s="eceba", k=2))  # 3
    print(init.lengthOfLongestSubstringKDistinct(s="aa", k=1))  # 2
    print(init.lengthOfLongestSubstringKDistinct(s="bacc", k=2))  # 3
