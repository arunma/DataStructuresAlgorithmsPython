from collections import defaultdict


class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ws=0
        charMap=defaultdict(int)
        maxLength=0

        for we,endChar in enumerate(s):
            charMap[endChar]+=1
            while charMap[endChar]>1:
                startChar=s[ws]
                charMap[startChar]-=1
                ws+=1
            maxLength=max(maxLength, we-ws+1)
        return maxLength



if __name__ == '__main__':
    init = LongestSubstringWithoutRepeatingCharacters()
    print(init.lengthOfLongestSubstring("abcabcbb"))
