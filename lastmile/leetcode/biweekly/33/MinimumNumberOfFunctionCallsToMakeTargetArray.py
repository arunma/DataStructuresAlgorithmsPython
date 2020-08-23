from typing import List


class MinimumNumberOfFunctionCallsToMakeTargetArray:
    def minOperations(self, A: List[int]) -> int:
        ans = 0
        bns = 0
        for x in A:
            b = bin(x)
            ans += b.count('1')
            if x:
                bns = max(bns, len(b) - 2)
        return ans + max(bns-1,0)



if __name__ == '__main__':
    init = MinimumNumberOfFunctionCallsToMakeTargetArray()
    print(init.minOperations([1, 5]))  # , 5))
    print(init.minOperations([2, 2]))  # , 3))
    print(init.minOperations([4,2,5]))  # , 6))
