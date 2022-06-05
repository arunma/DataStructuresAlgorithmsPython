from collections import defaultdict


class LongestRepeatingCharacterReplacement:
    def characterReplacement(self, s: str, k: int) -> int:
        counter=defaultdict(int)
        N=len(s)
        ws=0
        max_count=0
        result=0
        for we in range (N):
            counter[s[we]]+=1
            max_count=max(max_count, counter[s[we]])
            if we-ws+1 - max_count >k: #(counts of chars that are not the most frequent)>k
                counter[s[ws]]-=1
                ws+=1
            result=max(result, we-ws+1)
        return result









if __name__ == '__main__':
    init = LongestRepeatingCharacterReplacement()
    print(init.characterReplacement(s = "ABAB", k = 2)) #4
    print(init.characterReplacement(s = "AABABBA", k = 1)) #4
