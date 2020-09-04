from collections import defaultdict
from typing import List

# DOES NOT WORK

class DetectPatternOfLengthMRepeatedKOrMoreTimes:
    # def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
    #     freq=defaultdict(list)
    #     for i in range (0,len(arr), m):
    #         if i>=len(arr): continue
    #         pattern=arr[i:i+m]
    #         freq[tuple(pattern)].append([1, i])
    #
    #     for valueList in sorted(freq.values()):
    #         curr=0
    #         prev_idx=None
    #         for ct, idx in sorted(valueList, key = lambda each: each[1]):
    #             curr+=ct
    #             if prev_idx is None:
    #                 prev_idx=idx
    #             elif idx-prev_idx!=m:
    #                 curr=0
    #                 prev_idx=None
    #             elif curr>=k:
    #                 return True
    #             prev_idx=idx
    #     return False

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for start in range(len(arr)-m*k+1) :
            last_v = 1
            last_n = arr[start:start+m]
            next_start = start+m
            while next_start+m <= len(arr) :
                next_t = arr[next_start:next_start+m]
                if not next_t == last_n :
                    break
                last_v += 1
                next_start += m
            if last_v >= k :
                return True
        return False




if __name__ == '__main__':
    init = DetectPatternOfLengthMRepeatedKOrMoreTimes()
    print(init.containsPattern(arr = [1,2,4,4,4,4], m = 1, k = 3)) #True
    print(init.containsPattern(arr = [2,2,2,2], m = 2, k = 3)) #False
    print(init.containsPattern(arr = [2,2], m = 1, k = 2)) #True
    print(init.containsPattern([2,2,1,2,2,1,1,1,2,1], 2, 2)) #False
    print(init.containsPattern([3,2,2,1,2,2,1,1,1,2,3,2,2], 3, 2)) #True

